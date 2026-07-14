from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base  


employee_project = Table(
    "employee_project", 
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True)
)


class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    
    #  back_populates trỏ đúng tên thuộc tính relationship "department" bên class Employee
    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    

    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")
    
    # SỬA: Thêm uselist=False để giới hạn ORM chỉ trả về 1 đối tượng duy nhất thay vì 1 List
    device = relationship("Device", back_populates="employee", uselist=False)
    
    #  SỬA: Thêm tham số secondary=employee_project để cấu hình bảng trung gian cho quan hệ N-N
    projects = relationship("Project", secondary=employee_project, back_populates="employees")


class Device(Base):
    __tablename__ = "devices"
    
    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String(50), unique=True, nullable=False)
    
    # ĐÃ SỬA: Thêm unique=True ở tầng DB để khóa chặt không cho một Employee liên kết với Device thứ hai
    employee_id = Column(Integer, ForeignKey("employees.id"), unique=True)
    employee = relationship("Employee", back_populates="device")


class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    
    #  SỬA: Thêm tham số secondary=employee_project tương tự như bên class Employee
    employees = relationship("Employee", secondary=employee_project, back_populates="projects")