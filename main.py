import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/')
def home():
    return {
        'message': 'Say hello to my LIL FRIEND!!'
    }


uvicorn.run(api)
