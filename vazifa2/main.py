from fastapi import FastAPI
from routers import *
from db import Base, engine


app = FastAPI()


app.include_router(router, prefix='/students')
Base.metadata.create_all(bind=engine)