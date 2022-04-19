from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import asyncio

from models.input_model import InputFile
from core.engine.session.generator_session import get_session
from core.engine.session.reader_session_data import get_session_data
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
    session = get_session(file.name, file.content)
    return RedirectResponse(f'/result/{session}')


@router.post('/result/{session_id}')
async def func(request: Request, session_id: str):
    session_data = get_session_data(session_id)
    print(session_data)
    data = {
        'endpoints_and_people': [['qwer', 21], ['trew', 2]],
        'start_date': '1234',
        'end_date': '4321'
    }
    # add ..., 'result': result...
    return templates.TemplateResponse('result.html', {'request': request, 'session_data': data})
