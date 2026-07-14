from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
import app.services.student_service
from app.schemas.schemas import StudentRequestDTO   

student_router = APIRouter(
    prefix="/students",
    tags=["Student"]
)

@student_router.get("/")
def get_all_student(db:Session = Depends(get_db)):
    return {
        "message":"Get Complete",
        "data": app.services.student_service.get_all_student(db)
    }

@student_router.post("/")
def create_student(book:StudentRequestDTO,db:Session = Depends(get_db)):
    db_get = app.services.student_service.create_student(db,book)
    return {
        "message":"Create Complete",
        "data": db_get 
    }


