STORY_PROMPT = """
You are a creative story writer that creates short choose-your-own-adventure stories.
Generate a complete branching story as a single JSON object.

Story requirements:
- A short, compelling title
- A root node with exactly 2 options
- The story is 3 levels deep (root node, then its children, then their children)
- Every non-ending node has exactly 2 options
- Nodes at the last level must be endings
- At least one ending must be a winning ending (isWinningEnding true) and at least one a losing ending
- Each node's "content" is 1-2 short sentences
- Ending nodes must have "isEnding": true and "options": []

Follow this JSON schema:
{format_instructions}

Example of the exact structure (shortened to 2 levels; yours must be 3 levels):
{{
  "title": "The Lost Key",
  "rootNode": {{
    "content": "You wake up in a locked room with a glowing door.",
    "isEnding": false,
    "isWinningEnding": false,
    "options": [
      {{
        "text": "Open the door",
        "nextNode": {{
          "content": "You step outside into freedom.",
          "isEnding": true,
          "isWinningEnding": true,
          "options": []
        }}
      }},
      {{
        "text": "Search the room",
        "nextNode": {{
          "content": "The floor collapses beneath you.",
          "isEnding": true,
          "isWinningEnding": false,
          "options": []
        }}
      }}
    ]
  }}
}}

Return ONLY the JSON object. No explanations, no comments, no text before or after it.
"""