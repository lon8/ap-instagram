import json
from fastapi import APIRouter, HTTPException
from kernel import kernel

router = APIRouter()

@router.get('/')
async def info():
    return 'This is InstagramAPI for APIParser'

@router.post('/userInfo')
async def parse_kernel(data : dict):
    try:
        result = kernel(data['username'])

        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

        return result
    except KeyError:
        raise HTTPException(400, "Key error. Check your json data")