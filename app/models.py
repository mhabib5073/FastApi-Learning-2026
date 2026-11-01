from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    department:Mapped[str] = mapped_column(String(50))
    salary:Mapped[int] = mapped_column(Integer)
