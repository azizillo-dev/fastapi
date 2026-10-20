from fastapi import FastAPI
from routers.students import router as student_router
from database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(student_router, prefix='/students')






