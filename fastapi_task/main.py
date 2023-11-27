from fastapi import FastAPI, Depends
import asyncio
from database import async_session, Base, async_engine, get_async_db, create_async_db
from fastapi_task.task.routers import router as router_calculate


async def run_async_db_creation():
    await create_async_db()


app = FastAPI()

app.include_router(router_calculate, dependencies=[Depends(get_async_db)])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_async_db_creation())
