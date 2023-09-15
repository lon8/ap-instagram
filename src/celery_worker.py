import json
from celery import Celery
from src.kernel import kernel
from src.views import calculate_analytics

celery = Celery(
    'myapp',
    broker='redis://localhost:6389/0',  # URL Redis сервера для Celery (ПОРТ ИЗМЕНЁН НА +10)
    backend='redis://localhost:6389/0'  # URL Redis сервера для результатов выполнения задач (ПОРТ ИЗМЕНЁН НА +10)
)

json_data = {
    'search_query': 'some_search_query',
}


@celery.task()
def process_task(info : dict):
    result = kernel(info['search_query'])
    
    result_stats = calculate_analytics(result, info['user_id'])
    json_data['search_query'] = info['search_query']
    json_data['data'] = result_stats
    
    with open('stats_result.json', 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)
        
    return json_data

if __name__ == '__main__':
    celery.start()