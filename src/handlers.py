import asyncio
import json
from fastapi import APIRouter, HTTPException
from src.kernel import kernel

from src.celery_worker import process_task
from src.views import calculate_analytics

router = APIRouter()

json_data = {
    'search_query': 'some_search_query',
}

@router.post('/')
async def parse_kernel(info: dict):
    # result = process_task.delay(info)
    # task_result = await get_result(result)  # Ждем завершения задачи
    # return {"task_id": result.id, "task_result": task_result}
    result = kernel(info['search_query'])
    
    # with open('result.json', 'r', encoding='utf-8') as file:
    #     result = json.load(file)
    
    result_stats = calculate_analytics(result, info['user_id'])
    json_data['search_query'] = info['search_query']
    json_data['data'] = result_stats
    
    with open('stats_result.json', 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)
        
    return json_data

async def get_result(result):
    while not result.ready():
        await asyncio.sleep(1)  # Ждем, пока задача не будет завершена
    return result.result