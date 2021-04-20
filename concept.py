from fastapi import FastAPI, Request, Response, status
import hashlib
from pydantic import BaseModel
from datetime import date, timedelta, datetime


class User(BaseModel):
    name: str
    surname: str


class RegisteredUser():
    instances = []

    def __init__(self, name, surname, register_date):
        self.id = len(self.instances) + 1
        self.name = name
        self.surname = surname
        self.register_date = register_date
        self.vaccination_date = self.generate_vacc_date()
        self.instances.append(self)

    def generate_vacc_date(self):
        delay = len(self.name) + len(self.surname)
        vaccination_date = datetime.fromisoformat(self.register_date) + timedelta(days=delay)
        return vaccination_date.date()

    def register_user(self):
        res = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "register_date": self.register_date,
            "vaccination_date": self.vaccination_date
        }
        return res

    @classmethod
    def get_patient_by_id(cls, instance_id):
        for obj in cls.instances:
            if obj.id == instance_id:
                return obj
        return None


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!"}


@app.get("/auth")
def decrypt(response: Response, password: str = '', password_hash: str = ''):
    encrypted_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
    if password_hash == encrypted_password:
        response.status_code = status.HTTP_204_NO_CONTENT
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
    return response


@app.post("/register")
def create_user(request: Request, response: Response, user: User):
    try:
        date_as_datetime = datetime.strptime(request.headers['date'], '%a, %d %b %Y %H:%M:%S %Z')
        register_date = date_as_datetime.strftime('%Y-%m-%d')
    except KeyError:
        register_date = str(date.today())

    result = RegisteredUser(user.name, user.surname, register_date)
    response.status_code = status.HTTP_201_CREATED

    return result.register_user()


@app.get("/patient/{patient_id}")
def get_patient(patient_id: str, response: Response):
    try:
        patient_id = int(patient_id)
    except ValueError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response

    if patient_id < 1:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response

    patient = RegisteredUser.get_patient_by_id(patient_id)
    if patient:
        return patient
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
