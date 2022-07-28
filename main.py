from fastapi import FastAPI
from typing import Dict

app = FastAPI()


@app.post("/check_sex")
async def check_sex(iin: Dict[str, str]) -> bool:
    try:
        val: str = iin["iin"]
        if int(val[6]) % 2 != 0:
            return True
        else:
            return False
    except ValueError:
        print("inappropriate value for iin")


@app.post("/check_birthdate")
async def check_gender(iin: Dict[str, str]) -> int:
    try:
        val: str = iin["iin"]

        if val[6] in '56':
            age: int = 2022 - int('20' + val[:2])
        elif val[6] in '34':
            age: int = 2022 - int('19' + val[:2])
        else:
            age: int = 2022 - int('18' + val[:2])

        if 7 - int(val[2:4]) > 0 or 28 - int(val[4:6]) >= 0:
            return age
        elif 7 - int(val[2:4]) == 0 and 28 - int(val[4:6]) >= 0:
            return age
        else:
            return age - 1

    except ValueError:
        print("inappropriate value for iin")