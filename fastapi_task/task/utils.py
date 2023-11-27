from sqlalchemy.ext.asyncio import AsyncSession

from .models import Task, TaskStatus


async def calculate_result(x, y, operator):
    data = f'{x} {operator} {y}'
    result = eval(data)
    return result


async def result_background_task(task: Task, session: AsyncSession):
    result = await calculate_result(x=task.x, y=task.y, operator=task.operator)
    task.status = TaskStatus.completed
    task.result = result
    await session.commit()
    await session.refresh(task)
    return task
