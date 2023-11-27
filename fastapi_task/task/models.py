import enum
from sqlalchemy import Integer, String, Column, Enum, Float
from ..database import Base


class TaskStatus(enum.Enum):
    pending = 'pending'
    completed = 'completed'


class Task(Base):
    __tablename__ = 'async_tasks'

    id = Column(Integer, primary_key=True, index=True)
    x = Column(Integer)
    y = Column(Integer)
    operator = Column(String)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending, nullable=False)
    result = Column(Float, nullable=True)
