import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class StoryGenerator:

    @classmethod
    def _get_llm(cls):
        return ChatOpenAI(
            base_url=os.getenv("LM_STUDIO_BASE_URL", "http://127.0.0.1:1234/v1"),
            api_key=os.getenv("LM_STUDIO_API_KEY", "lm-studio"),
            model=os.getenv("LM_STUDIO_MODEL", "qwen2.5-coder-1.5b-instruct"),
            temperature=0.3,
            max_tokens=2048,   # 256 from the README would cut your story JSON off mid-way
            timeout=300,       # small local models can be slow
            max_retries=1,
        )

    @classmethod
    def generate_story(cls, db: Session, session_id: str, theme: str = "fantasy") -> Story:
        llm = cls._get_llm()
        story_parser = PydanticOutputParser(pydantic_object=StoryLLMResponse)

        prompt = ChatPromptTemplate.from_messages([
            ("system", STORY_PROMPT),
            ("human", "Create the story with this theme: {theme}"),
        ]).partial(format_instructions=story_parser.get_format_instructions())

        # Small models often produce invalid JSON, so retry a few times
        story_structure = None
        last_error = None
        for _ in range(3):
            raw_response = llm.invoke(prompt.invoke({"theme": theme}))
            response_text = getattr(raw_response, "content", raw_response)
            try:
                story_structure = story_parser.parse(response_text)
                break
            except Exception as e:
                last_error = e

        if story_structure is None:
            raise ValueError(f"LLM failed to return valid story JSON: {last_error}")

        story_db = Story(title=story_structure.title, session_id=session_id)
        db.add(story_db)
        db.flush()

        root_node_data = story_structure.rootNode
        if isinstance(root_node_data, dict):
            root_node_data = StoryNodeLLM.model_validate(root_node_data)

        cls._process_story_node(db, story_db.id, root_node_data, is_root=True)

        db.commit()
        return story_db