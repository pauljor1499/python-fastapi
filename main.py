from telnetlib import STATUS
from fastapi import FastAPI
from pydantic import ValidationError
from Model import (SignUp, Credentials)
from common.lib import Validator
from starlette.status import HTTP_400_BAD_REQUEST
from fastapi import FastAPI, status, HTTPException, Header
from starlette.responses import Response
from fastapi.params import Body


app = FastAPI(title="LMS", version="0.0.1")


@app.get("/")
def home():
    return {"message": "Welcome to Paul Jor API"}

# Method 2
@app.post("/login", status_code=status.HTTP_201_CREATED)
async def login(payload: dict = Body(...)):
    try:
        login = Credentials.Credentials(**payload)
        return_statement = {
            "Username": login.email_address,
            "Passwrod": login.password
        }
        email = Validator(login.email_address)
        if(email.validate_email()):
            return return_statement
        else:
            return 
    except ValidationError as error:
        print(f"Error->login(): {error}")
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f"There are required fields that needs to be address.")

@app.post("/sign_up_student", status_code=status.HTTP_201_CREATED)
async def sign_up_student(student: SignUp.Student):
    try:
        return_statement = {
            "First name": student.first_name,
            "Middle initial": student.middle_init,
            "Last name": student.last_name,
            "Title": student.title,
            "School": student.school,
            "School email": student.school_email,
            "Password1": student.password1,
            "Password2": student.password2
        }
        return return_statement
    except ValidationError as error:
        print(f"Error->login(): {error}")
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f"There are required fields that needs to be address.")

