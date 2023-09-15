import json
from fastapi import APIRouter, HTTPException
from src.kernel import kernel

router = APIRouter()

# @router.get('/')
# async def info():
#     return 'This is InstagramAPI for APIParser'

@router.post('/')
async def parse_kernel(data : dict):
<<<<<<< HEAD:handlers.py
	result = kernel(data['uid'])
=======
    try:
        result = kernel(data['search_query'])
>>>>>>> bb8971e (pre-release):src/handlers.py

	with open('result.json', 'w', encoding='utf-8') as file:
	    json.dump(result, file, indent=4, ensure_ascii=False)

	return result
