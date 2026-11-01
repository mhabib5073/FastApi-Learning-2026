from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeResponse

router = APIRouter(prefix="/employee", tags=["Employees"])

@router.post("/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(
        name=employee.name,
        department=employee.department,
        salary=employee.salary

    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

@router.get("/", response_model=list[EmployeeResponse])
def get_employees(db: Session=Depends(get_db)):
    emp = db.query(Employee).all()
    return emp

@router.get("/{emp_id}", response_model=EmployeeResponse)
def get_employee(emp_id:int, db: Session=Depends(get_db)):
    emp = db.get(Employee, emp_id)
    if not emp:
        raise HTTPException(
            status_code=404,
            detail="Not found"
        )
    return emp

@router.put("/{emp_id}", response_model=EmployeeResponse)
def update_emp(emp_id: int, upd_emp: EmployeeCreate, db: Session=Depends(get_db)):
    emp = db.get(Employee,emp_id)
    if not emp:
        raise HTTPException(
            status_code=404,
            detail="Employee Not found"
        )
    emp.name = upd_emp.name
    emp.department = upd_emp.department
    emp.salary = upd_emp.salary

    db.commit()
    db.refresh(emp)
    return emp

@router.delete("/{emp_id}")
def delete_employee(emp_id: int, db: Session=Depends(get_db)):
    emp = db.get(Employee, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted successfully"}