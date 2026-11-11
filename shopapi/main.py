from fastapi import FastAPI
from db import Base, engine
from users.routers import router as users_router
app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(users_router)


@app.get('/')
def hello():
    return {"message" : "Hello FastAPI"}


