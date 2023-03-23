from fastapi import Form
from pydantic import BaseModel,constr,EmailStr,validator
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    username : constr(min_length=1,max_length=50)
    lastusername : constr(min_length=1,max_length=50)
    makeuser : constr(min_length=1,max_length=50)
    password : constr(min_length=8,max_length=50)
    password2 : constr(min_length=8,max_length=50)
    email : EmailStr
    
    @classmethod
    def user(
        cls,
        username: str = Form(...),
        lastusername: str = Form(...),
        makeuser: str = Form(...),
        password: str = Form(...),
        password2: str = Form(...),
        email: str = Form(...),
        ):
          return cls(
               username= username,
               lastusername= lastusername,
               makeuser = makeuser,
               password= password,
               password2 = password2,
               email=email
          )
    
    # Tirar os espaços vazios do começo e do final de cada campo
    @validator('*', pre=True)
    def remove_whitespace(cls, value):
         if isinstance(value,str):
              return value.strip()
         return value
         

    class Config: 
        orm_mode = True