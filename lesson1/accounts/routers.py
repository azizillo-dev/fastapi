from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def get_info():
    return {
        "msg" : "Salom bu mening fastAPi dagi birinchi codim"
    }



