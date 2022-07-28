from fastapi import FastAPI
from typing import Dict
from services import get_person_sex, get_person_age
app = FastAPI()


@app.post("/check-sex")
async def check_sex(person_data: Dict[str, str]) -> Dict[str, bool]:
    sex: bool = get_person_sex(person_data["iin"])
    return {"sex": sex}


@app.post("/check-birthdate")
async def check_gender(person_data: Dict[str, str]) -> Dict[str, int]:
    try:
        age: int = get_person_age(person_data["iin"])
        return {"age": age}
    except ValueError:
        print("inappropriate value for iin")
