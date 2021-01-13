import fastapi
from starlette.requests import Request
router = fastapi.APIRouter()

@router.get('/')
def index(request: Request):
    return {"Kaizen": "Personal metrics server - http://127.0.0.1:8000/api/kaizen"} 