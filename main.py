import json
from pathlib import Path
from services import sjd_service

import fastapi
import uvicorn

from api import kaizen_api
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_settings()

def configure_routing():
    api.include_router(home.router)
    api.include_router(kaizen_api.router)

def configure_settings():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found, you cannot continue. Please see settings_template.json")
        raise Exception("settings.json file not found. Please see settings_template.json.")
    
    with open('settings.json') as fin:
        settings = json.load(fin)
        sjd_service.username = settings.get('sjd_username')
        sjd_service.password = settings.get('sjd_password')



if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
