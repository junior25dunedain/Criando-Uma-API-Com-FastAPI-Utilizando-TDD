from fastapi import FastAPI 
from core.config import settings
from store.routers import api_router

class App(FastAPI):
    def __init__(self, *arfs,**kwargs) -> None:
        super().__init__( *arfs,**kwargs,version='0.0.1',title=settings.PROJECT_NAME,root_path=settings.ROOT_PATH)

app = App()
app.include_router(api_router)