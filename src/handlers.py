import asyncio
import json
from fastapi import APIRouter, HTTPException
from src.kernel import kernel

from celery_worker import process_task

router = APIRouter()


@router.post('/')
async def parse_kernel(info: dict):
    result = process_task.delay(info)
    task_result = await get_result(result)  # Ждем завершения задачи
    return {"task_id": result.id, "task_result": task_result}

async def get_result(result):
    while not result.ready():
        await asyncio.sleep(1)  # Ждем, пока задача не будет завершена
    return result.result