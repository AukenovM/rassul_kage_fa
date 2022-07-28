from fastapi import FastAPI
from typing import Dict
from services import get_person_sex, get_person_age
app = FastAPI()


@app.post("/{iin}/check-sex/")
async def check_sex(iin: str) -> Dict[str, bool]:
    sex: bool = get_person_sex(iin)
    return {"sex": sex}


@app.post("/{iin}/check-birthdate/")
async def check_gender(iin: str) -> Dict[str, int]:
    try:
        age: int = get_person_age(iin)
        return {"age": age}
    except ValueError:
        print("inappropriate value for iin")
