from fastapi import Form
from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    name : str
    last_name : str
    user : str
    password : str
    email : str
    @classmethod
    def user(
        cls,
        name: str = Form(...),
        last_name: str = Form(...),
        user: str = Form(...),
        password: str = Form(...),
        email: str = Form(...),
        ):
          return cls(
               name= name,
               last_name= last_name,
               user = user,
               password= password,
               email=email
          )
    

    class Config: 
        orm_mode = True