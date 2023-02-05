import uvicorn
from fastapi import FastAPI
from api.api_v1.router import router

app = FastAPI()
app.include_router(router)


# default root path
@app.get('/')
async def root():

    message = {
        'message': 'This is german NER api v1.0. Please, open /docs endpoint to open swagger (format) '
                   'documentation '
    }

    return message


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3345)