import json
from models import Quiz,Question

def save_quiz(db,url,data,raw_html):

    quiz=Quiz(
        url=url,
        title=data["title"],
        summary=data["summary"],
        key_entities=json.dumps(data["key_entities"]),
        sections=json.dumps(data["sections"]),
        related_topics=json.dumps(data["related_topics"]),
        raw_html=raw_html
    )

    db.add(quiz)
    db.commit()
    db.refresh(quiz)

    for q in data["quiz"]:

        question=Question(
            quiz_id=quiz.id,
            question=q["question"],
            options=json.dumps(q["options"]),
            answer=q["answer"],
            difficulty=q["difficulty"],
            explanation=q["explanation"]
        )

        db.add(question)

    db.commit()

    return quiz