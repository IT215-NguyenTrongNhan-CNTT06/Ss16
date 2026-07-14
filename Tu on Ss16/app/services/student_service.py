from sqlalchemy.orm import Session
from app.models.student_model import StudentModel
from app.schemas.schemas import StudentRequestDTO
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

def get_all_student(db:Session):
    return db.query(StudentModel).all()

def create_student(db:Session,book:StudentRequestDTO):
    try: 
        new_student = StudentModel(
            name = book.name,
            email = book.email
        )

        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student
    except SQLAlchemyError as e : 
        db.rollback()
        raise HTTPException(status_code=422,detail=f"Error:{str(e)}")
