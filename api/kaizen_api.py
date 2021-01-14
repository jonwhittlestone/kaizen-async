import fastapi

router = fastapi.APIRouter()
from services import sjd_service, email_service, book_service, article_service

@router.get('/api/kaizen')
async def kaizen():
   company_profits = await sjd_service.main()
   inbox_count = await email_service.inbox_count()
   books_read_this_year = await book_service.Client().books_on_shelf_count()
   article_count = await article_service.article_count()
   return {
       'AIM HIGHER': {
        'COMPANY PROFITS': company_profits,
        'YEARLY BOOKS READ': books_read_this_year,
       },
       'AIM LOWER': {
        'INBOX COUNT': inbox_count,
        'ARTICLE COUNT': article_count
       }
    }
