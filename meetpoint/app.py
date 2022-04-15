from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles
#from database.base import database
from starlette.middleware.cors import CORSMiddleware

from core.endpoints.routes import views

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


#@app.on_event('startup')
#async def startup():
    #await database.connect()

#@app.on_event('shutdown')
#async def shutdown():
    #await database.disconnect()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(views.router)

if __name__ == '__main__':
    uvicorn.run('app:app', port = 8080, reload=True, debug=True)
