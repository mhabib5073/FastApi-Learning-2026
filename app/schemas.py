from pydantic import BaseModel, ConfigDict

class EmployeeCreate(BaseModel):
    name:str
    department:str
    salary: int
class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    salary:int

    model_config = ConfigDict(from_attributes=True)



