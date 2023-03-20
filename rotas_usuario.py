import uvicorn
from fastapi import APIRouter, status, Depends, FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from configuracao.database import get_db
from schemas.schemas import Usuario 
from sqlalchemy.orm import Session
from repositorios.repositorio_user import RepositorioUsuario
from models import models
from configuracao.database import Base,engine
from schemas.schemas import Usuario

#Para criar a tabela no banco de dados
models.Base.metadata.create_all(engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get('/basic', response_class=HTMLResponse)
async def get_basic_form(request:Request):
  return templates.TemplateResponse("index.html", {"request":request})

@app.post('/basic',response_class=HTMLResponse,status_code=status.HTTP_201_CREATED, response_model=Usuario)
async def post_basic_form(request: Request, usuario:Usuario, session: Session = Depends(get_db), username: str = Form(...) , lastusername: str = Form(...) , makeuser: str = Form(...), password: str= Form(...), email: str = Form(...)):
   usuario_criado = RepositorioUsuario(session).criar(usuario)
   return templates.TemplateResponse("index.html",{"request":request,"username":username,"lastusername":lastusername,"makeuser":makeuser,"password":password,"email":email})

if __name__ == '__main__':
  uvicorn.run(app)
