import json
from google import generativeai as genai

def run_transformation_agent(api_key: str, markdown_text: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-flash-latest")

    prompt = f"""
    You are a professional market analyst.
    Analyze the following Markdown text and convert it into a structured JSON report with this schema:

    {{
        "headline": "A short, compelling title",
        "top_news": [{{"title":"...","summary":"...","relevance":"...","link":"..."}}],
        "players": [{{"title":"...","summary":"...","impact":"...","link":"..."}}],
        "competitors": [{{"title":"...","summary":"...","implication":"...","link":"..."}}],
        "risks": {{"geopolitical":"...","technological":"...","regulatory":"..."}},
        "strategy": {{"trends":"...","action_immediate":"...","action_medium":"...","action_long":"..."}},
        "provocation": "Final thought"
    }}

    Input Markdown:
    ---
    {markdown_text}
    """

    response = model.generate_content(prompt)
    clean_json = response.text.replace("```json","").replace("```","").strip()
    return json.loads(clean_json)