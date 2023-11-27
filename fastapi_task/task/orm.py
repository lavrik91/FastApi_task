from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import Task
from .schemas import TaskCreate


async def create_task(input_data: TaskCreate, session: AsyncSession):
    task = Task(x=input_data.x, y=input_data.y, operator=input_data.operator)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


async def get_task(task_id: int, session: AsyncSession):
    result = await session.execute(select(Task).filter(Task.id == task_id))
    task = result.scalars().first()
    return task


async def list_tasks(session: AsyncSession):
    result = await session.execute(select(Task))
    tasks = result.scalars().all()
    return tasks
