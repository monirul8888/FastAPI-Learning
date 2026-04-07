from sqlalchemy import Column, Integer, Float, String
from . database import Base

class Student(Base):
    __tablename__ = "student1"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    dept = Column(String, nullable = False)

