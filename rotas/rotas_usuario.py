from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from configuracao.database import get_db
from schemas.schemas import Usuario 
from sqlalchemy.orm import Session
from repositorios.repositorio_user import RepositorioUsuario
from models import models
from configuracao.database import engine

#Para criar a tabela no banco de dados
models.Base.metadata.create_all(engine)

#app = FastAPI()
route = APIRouter()

templates = Jinja2Templates(directory="templates")

@route.get('/basic', response_class=HTMLResponse)
async def get_basic_form(request:Request):
  return templates.TemplateResponse("index.html", {"request":request})

@route.post('/basic',response_class=HTMLResponse,status_code=status.HTTP_201_CREATED, response_model=Usuario)
async def post_basic_form(request: Request,usuario: Usuario = Depends(Usuario.user), session: Session = Depends(get_db)):
   usuario_criado = RepositorioUsuario(session).criar(usuario)
   return templates.TemplateResponse("index.html",{"request":request,"new_user":usuario_criado})
