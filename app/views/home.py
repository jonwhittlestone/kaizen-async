import fastapi
from starlette.requests import Request
router = fastapi.APIRouter()

@router.get('/')
def index(request: Request):
    base_url = request.base_url._url
    return {"Kaizen": f"Personal metrics server - {base_url}api/kaizen"}
