
from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class ExpenseCreate(BaseModel):
    amount: float
    description: str
    category: str = "Other"
    payment_method: str
    expense_date: date


class ExpenseUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None
    payment_method: Optional[str] = None
    expense_date: Optional[date] = None
