# LangChain Prompt Templates
# Prompt - 1 

## Quiz Generation Prompt

The application uses LangChain PromptTemplate to guide LLM output and reduce hallucinations.

### System Instructions

- Generate quiz ONLY from provided article.
- DO NOT hallucinate information.
- Return ONLY raw JSON.
- Include easy, medium and hard difficulty questions.
- Provide related topics for further reading.

### Output Format

{
"title":"",
"summary":"",
"key_entities":{"people":[],"organizations":[],"locations":[]},
"sections":[],
"quiz":[
{"question":"","options":["","","",""],"answer":"","difficulty":"","explanation":""}
],
"related_topics":[]
}

### Input Variables

- article: Extracted Wikipedia content (max 8000 chars)

### LangChain Usage

PromptTemplate → ChatGroq LLM → StrOutputParser pipeline.


# Prompt - 2

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

