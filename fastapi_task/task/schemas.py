from typing import Optional

from pydantic import BaseModel


class TaskCreate(BaseModel):
    x: int
    y: int
    operator: str


class Task(TaskCreate):
    id: int
    status: str
    result: Optional[float]

    class Config:
        orm_mode = True


class TaskList(BaseModel):
    id: int
    status: str


class TaskId(BaseModel):
    id: int


class TaskResult(BaseModel):
    result: Optional[float]
