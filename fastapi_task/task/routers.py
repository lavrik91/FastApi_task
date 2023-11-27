from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_task.database import get_async_db
from .schemas import TaskCreate, TaskList, TaskId, TaskResult
from .orm import create_task, get_task, list_tasks
from .utils import result_background_task

router = APIRouter()


@router.post('/calculate', response_model=TaskId)
async def calculate(input_data: TaskCreate, background_tasks: BackgroundTasks,
                    session: AsyncSession = Depends(get_async_db)):
    operators = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}

    if input_data.operator not in operators:
        raise HTTPException(status_code=400, detail="Invalid operator")

    task = await create_task(session=session, input_data=input_data)
    background_tasks.add_task(result_background_task, task, session)
    return {'id': task.id}


@router.get('/calculate/list', response_model=List[TaskList])
async def get_tasks(session: AsyncSession = Depends(get_async_db)):
    tasks = await list_tasks(session=session)
    return [{'id': task.id, 'status': task.status} for task in tasks]


@router.get('/calculate/{task_id}', response_model=TaskResult)
async def get_result(task_id: int, session: AsyncSession = Depends(get_async_db)):
    task = await get_task(task_id=task_id, session=session)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {'result': task.result}
