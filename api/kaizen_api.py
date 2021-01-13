import fastapi

router = fastapi.APIRouter()
from services import sjd_service

@router.get('/api/kaizen')
async def kaizen():
    return {'all_the_':'metrics'}
    # metric = await sjd_service.get_metric_async()