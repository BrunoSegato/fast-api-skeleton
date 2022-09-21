import uvicorn
from api.application.server import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', port=9000, reload=True, )
