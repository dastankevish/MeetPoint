from starlette.config import Config

config = Config('.env')

DATABASE_NAME = config('MP_DATABASE_NAME', cast=str, default='')
DATABASE_URL = config('MP_DATABASE_URL', cast=str, default='')
