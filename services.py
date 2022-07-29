from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")


def get_person_sex(person_data: str) -> bool:
    try:
        if int(person_data[6]) % 2 != 0:
            return True
        else:
            return False
    except ValueError:
        print("inappropriate value for iin")


def get_person_century(person_age: str):
    if person_age[6] in '56':
        return int(d1[6:10]) - int('20' + person_age[:2])
    else:
        return int(d1[6:10]) - int('19' + person_age[:2])


def get_person_age(person_age: str) -> int:
    try:
        age: int = get_person_century(person_age)
        month: int = int(d1[3:5]) - int(person_age[2:4])
        day: int = int(d1[:2]) - int(person_age[4:6])

        if (month > 0 or day >= 0) or (month == 0 and day >= 0):
            return age
        else:
            return age - 1

    except ValueError:
        print("inappropriate value for iin")
