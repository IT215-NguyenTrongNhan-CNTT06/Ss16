from pydantic import BaseModel

class StudentRequestDTO(BaseModel):
    name : str 
    email : str