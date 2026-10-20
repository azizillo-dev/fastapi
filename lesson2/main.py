from fastapi import FastAPI
from db import Base, engine
from models import Book
from routers import router as book_router

app = FastAPI()
app.include_router(book_router, prefix='/books')

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}



