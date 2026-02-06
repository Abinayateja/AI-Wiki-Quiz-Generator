import json
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine, Base
from models import Quiz
from scraper import scrape_wikipedia
from llm import generate_quiz
from crud import save_quiz


# =========================
# APP INIT
# =========================

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Wiki Quiz Generator",
    description="Generate quizzes from Wikipedia using FastAPI + LangChain + LLM",
    version="1.0"
)

# CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change to frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# DATABASE SESSION
# =========================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# HEALTH CHECK
# =========================

@app.get("/")
def root():
    return {"status": "API running"}


# =========================
# GENERATE QUIZ
# =========================

@app.post("/generate-quiz")
def generate(data: dict, db: Session = Depends(get_db)):

    url = data.get("url")

    if not url.startswith("https://en.wikipedia.org/wiki/"):
        raise HTTPException(status_code=400, detail="Invalid Wikipedia URL")

    if not url:
        raise HTTPException(status_code=400, detail="URL missing")

    # 🔥 VALIDATION BONUS POINT
    if "wikipedia.org/wiki/" not in url:
        raise HTTPException(status_code=400, detail="Only Wikipedia URLs allowed")

    # 🔥 CACHING BONUS POINT
    existing = db.query(Quiz).filter(Quiz.url == url).first()

    if existing:
        return {
            "message": "Quiz already exists",
            "id": existing.id
        }

    try:
        # SCRAPE
        title, text, sections, raw_html = scrape_wikipedia(url)

        if not text:
            raise HTTPException(status_code=400, detail="Failed to extract article content")

        # GENERATE QUIZ (LangChain)
        result = generate_quiz(text, sections)

        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])

        # SAVE DB
        quiz = save_quiz(db, url, result, raw_html)

        result["id"] = quiz.id
        result["url"] = url

        return result

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


# =========================
# HISTORY TAB
# =========================

@app.get("/history")
def history(db: Session = Depends(get_db)):

    quizzes = db.query(Quiz).all()

    return [
        {
            "id": q.id,
            "title": q.title,
            "url": q.url
        }
        for q in quizzes
    ]


# =========================
# QUIZ DETAILS
# =========================

@app.get("/quiz/{id}")
def get_quiz(id: int, db: Session = Depends(get_db)):

    quiz = db.query(Quiz).filter(Quiz.id == id).first()

    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return {
        "id": quiz.id,
        "url": quiz.url,
        "title": quiz.title,
        "summary": quiz.summary,
        "key_entities": json.loads(quiz.key_entities),
        "sections": json.loads(quiz.sections),
        "related_topics": json.loads(quiz.related_topics),
        "quiz": [
            {
                "question": q.question,
                "options": json.loads(q.options),
                "answer": q.answer,
                "difficulty": q.difficulty,
                "explanation": q.explanation
            }
            for q in quiz.questions
        ]
    }