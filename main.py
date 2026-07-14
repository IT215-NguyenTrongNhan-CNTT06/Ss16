from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base  


student_course = Table(
    "student_course", 
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True)
)


class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    
    # SỬA LỖI 1-N: back_populates phải trỏ đến tên thuộc tính relationship "department" bên class Student
    students = relationship("Student", back_populates="department")


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    
    # Cấu hình chuẩn cho quan hệ 1 - N với Department
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="students")
    
    # SỬA LỖI 1-1: Thêm uselist=False để ORM hiểu đây là quan hệ một-một, không trả về danh sách
    profile = relationship("Profile", back_populates="student", uselist=False)
    
    # SỬA LỖI N-N: Bổ sung tham số secondary trỏ vào bảng trung gian student_course
    courses = relationship("Course", secondary=student_course, back_populates="students")


class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String(255))
    
    # SỬA LỖI 1-1: Thêm unique=True ở tầng DB để đảm bảo mỗi Student chỉ có duy nhất một Profile
    student_id = Column(Integer, ForeignKey("students.id"), unique=True)
    student = relationship("Student", back_populates="profile")


class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    
    # SỬA LỖI N-N: Bổ sung tham số secondary trỏ vào bảng trung gian student_course
    students = relationship("Student", secondary=student_course, back_populates="courses")