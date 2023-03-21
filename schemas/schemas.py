from fastapi import Form
from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    username : str
    lastusername : str
    makeuser : str
    password : str
    email : str
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