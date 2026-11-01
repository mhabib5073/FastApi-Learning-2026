from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import Base, engine
from app.models import Employee
from app.emp_api import router as employee_router


app = FastAPI(title="Employee API CRUD")
Base.metadata.create_all(bind=engine)

app.include_router(employee_router)

@app.get("/health")
def get_health():
    return {"message": "Employee API working"}



