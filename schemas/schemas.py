from fastapi import Form
from pydantic import BaseModel,constr,EmailStr
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    username : constr(min_length=1,max_length=50)
    lastusername : constr(min_length=1,max_length=50)
    makeuser : constr(min_length=1,max_length=50)
    password : constr(min_length=8,max_length=50)
    email : EmailStr
    @classmethod
    def user(
        cls,
        username: str = Form(...),
        lastusername: str = Form(...),
        makeuser: str = Form(...),
        password: str = Form(...),
        email: str = Form(...),
        ):
          return cls(
               username= username,
               lastusername= lastusername,
               makeuser = makeuser,
               password= password,
               email=email
          )
    

    class Config: 
        orm_mode = True