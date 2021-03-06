import json
import os
from pathlib import Path
from app.services import (sjd_service, email_service, book_service, article_service)

import fastapi
import uvicorn

from app.api import kaizen_api
from app.views import home

app = fastapi.FastAPI()
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def configure():
    configure_routing()
    configure_settings()

def configure_routing():
    app.include_router(home.router)
    app.include_router(kaizen_api.router)

def configure_settings():
    file = Path(os.path.join(PROJECT_DIR, 'settings.json')).absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found, you cannot continue. Please see settings_template.json")
        raise Exception("settings.json file not found. Please see settings_template.json.")

    with open(file) as fin:
        settings = json.load(fin)
        sjd_service.username = settings.get('sjd_username')
        sjd_service.password = settings.get('sjd_password')

        email_service.username = settings.get('email_username')
        email_service.password = settings.get('email_password')

        book_service.key = settings.get('goodreads_key')
        book_service.secret = settings.get('goodreads_secret')

        article_service.consumer = settings.get('pocket_consumer')
        article_service.access = settings.get('pocket_access')


if __name__ == '__main__':
    configure()
    uvicorn.run(app, port=8000, host='127.0.0.1')
else:
    configure()
