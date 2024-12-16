from sqlalchemy.orm import Session
from models import KeyWord, Answer, Sport
from dataBase import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_keyword(db: Session, sport_id: int, content: str):
    keyword = KeyWord(content=content, sport_id=sport_id)
    db.add(keyword)
    db.commit()
    db.refresh(keyword)
    return keyword

def add_answer(db: Session, keyword_id: int, content: str):
    answer = Answer(content=content, keyword_id=keyword_id)
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer

def add_sport(db: Session, content: str):
    sport = Sport(content=content)
    db.add(sport)
    db.commit()
    db.refresh(sport)
    return sport

def remove_sport(db: Session, content: str):
    sport = db.query(Sport).filter(Sport.content == content).one()
    db.delete(sport)
    db.commit()
    return sport

def remove_keyword(db: Session, content: str):
    keyword = db.query(KeyWord).filter(KeyWord.content == content).first()
    if keyword:
        db.delete(keyword)
        db.commit()
    return keyword

def remove_answer(db: Session, content: str):
    answer = db.query(Answer).filter(Answer.content == content).first()
    if answer:
        db.delete(answer)
        db.commit()
    return answer

def get_sports(db: Session):
    return db.query(Sport).all()

def get_keywords(db: Session, sport_id: int):
    return db.query(KeyWord).filter(KeyWord.sport_id == sport_id).all()

def get_answers(db: Session, keyword_id: int):
    return db.query(Answer).filter(Answer.keyword_id == keyword_id).all()

def get_sport_by_content(db: Session, content: str):
    return db.query(Sport).filter(Sport.content == content).first()

def get_keyword_by_content(db: Session, content: str):
    return db.query(KeyWord).filter(KeyWord.content == content).first()

def add_keyword_to_sport(db_session, sport_id, keyword_id):
    # Retrieve the sport and keyword objects
    sport = db_session.query(Sport).filter_by(id=sport_id).first()
    keyword = db_session.query(KeyWord).filter_by(id=keyword_id).first()

    # Check if the keyword is already associated with the sport
    if keyword not in sport.keywords:
        sport.keywords.append(keyword)
        db_session.commit()
    else:
        print(f"Keyword '{keyword.content}' is already associated with sport '{sport.content}'.")