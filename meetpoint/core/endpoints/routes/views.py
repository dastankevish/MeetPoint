from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import asyncio

from models.input_model import InputFile
from core.parse_input_file import get_data_from_file
from core.engine.parsing.price import get_prices


templates = Jinja2Templates(directory='templates')
router = APIRouter()


@router.get('/')
def home_page(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@router.get('/main/')
def main_page(request: Request):
    return templates.TemplateResponse('main.html', {'request': request})


@router.post('/main/')
async def upload_and_parse_file(file: InputFile = Depends(InputFile.as_file)):
    data_from_file = get_data_from_file(file.name, file.content)


@router.get('/result/{session_id}')
def func(request: Request, session_id: int):
    return templates.TemplateResponse('result.html', {'request': request, 'arrival_airport': arrival_airport})
