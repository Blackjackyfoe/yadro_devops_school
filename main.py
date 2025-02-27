from fastapi import FastAPI
from app.config import settings
import uvicorn
from app.routes import routers

app = FastAPI()

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
  uvicorn.run("main:app", reload=True, port=settings.PORT)