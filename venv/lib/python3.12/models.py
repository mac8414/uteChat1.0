from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from dataBase import Base

class Sport(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    keywords = relationship("KeyWord", back_populates="sport")
    
    def get_content(self):
        return self.content

class KeyWord(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    sport_id = Column(Integer, ForeignKey('sports.id'))
    sport = relationship("Sport", back_populates="keywords")
    answers = relationship("Answer", back_populates="keyword")

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    keyword_id = Column(Integer, ForeignKey('keywords.id'))
    keyword = relationship("KeyWord", back_populates="answers")

