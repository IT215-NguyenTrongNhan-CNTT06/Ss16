from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class StudentModel(Base):
    __tablename__  = "Students"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name =Column(String(100),nullable=False)
    email = Column(String(100),nullable=False)

    profile = relationship("ProfileModel",back_populates="student",uselist=False)

class ProfileModel(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    bio = Column(String(100),nullable=False)
    
    student_id = Column(Integer,ForeignKey("Students.id"),unique=True)
    student = relationship("StudentModel",back_populates="profile")