import json
import re
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import os


# ===============================
# LLM
# ===============================

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0
)


# ===============================
# STRONG PROMPT (Evaluator Level)
# ===============================

PROMPT = """
You are an expert AI quiz generator.

STRICT RULES:

- Generate quiz ONLY from provided article.
- DO NOT hallucinate information.
- Return ONLY RAW JSON.
- No markdown.
- Generate EXACTLY 7 questions.
- Include mix of EASY, MEDIUM, HARD.
- Each question MUST have 4 options(A-D).
- Use different parts of article content.
- Related topics MUST NOT be empty.

OUTPUT RULES:

- Return ONLY RAW JSON.
- No markdown.
- No explanations outside JSON.

JSON FORMAT:

{{
"title":"",
"summary":"",
"key_entities":{{"people":[],"organizations":[],"locations":[]}},
"sections":[],
"quiz":[
{{"question":"","options":["","","",""],"answer":"","difficulty":"","explanation":""}}
],
"related_topics":[]
}}

ARTICLE:
{article}
"""

prompt_template = PromptTemplate(
    input_variables=["article","sections"],
    template=PROMPT
)

chain = prompt_template | llm | StrOutputParser()


# ===============================
# SAFE GENERATION FUNCTION
# ===============================

def generate_quiz(article, sections):

    response = chain.invoke({
    "article": article[:6000] + "\n\nSECTIONS:\n" + ", ".join(sections)
    })

    print("LLM RAW RESPONSE:", response)

    try:
        match = re.search(r"\{.*\}", response, re.DOTALL)

        if not match:
            return {"error":"No JSON returned"}

        data = json.loads(match.group())

        # HARD ENFORCEMENT (IMPORTANT)

        if not data.get("sections"):
            data["sections"] = sections[:6]

        if not data.get("related_topics"):
            data["related_topics"] = sections[:5]

        return data

    except Exception as e:
        return {"error": f"JSON parsing failed: {str(e)}"}