from fastapi import FastAPI
from lesson1.accounts.routers import router as accounts_router
app = FastAPI()


@app.get('/')
def get_info():
    return {
        "msg" : "Salom bu mening fastAPi dagi birinchi codim"
    }


@app.get('/me') 
def me():
    return {
        "name" : "Azizillo"
}

app.include_router(accounts_router)






