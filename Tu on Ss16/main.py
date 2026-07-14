from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import get_db,engine,Base
from app.models.student_model import StudentModel,ProfileModel
from app.routers.student_router import student_router


app = FastAPI(
    title="Test"
)

Base.metadata.create_all(bind = engine)
    
@app.get("/")
def get_root():
    return {
        "message":"Hay"
    }

app.include_router(student_router)
