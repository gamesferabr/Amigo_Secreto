from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.config.database import get_db,engine
from src.schemas.schemas import Usuario 
from sqlalchemy.orm import Session
from src.repositorios.repositorio_user import RepositorioUsuario
from src.models import models
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse, JSONResponse

#Para criar a tabela no banco de dados
models.Base.metadata.create_all(engine)

#app = FastAPI()
route = APIRouter()

templates = Jinja2Templates(directory="templates")

@route.get('/cadastro', response_class=HTMLResponse)
async def get_basic_form(request:Request):
  return templates.TemplateResponse("index.html", {"request":request})

@route.post('/cadastro',response_class=HTMLResponse,status_code=status.HTTP_201_CREATED, response_model=Usuario)
async def post_basic_form(request: Request,usuario: Usuario = Depends(Usuario.user), session: Session = Depends(get_db)):
   #Verifica se o email não existe no banco de dados se existir ele pede para o novo usuário preencher de novo
   db_user = RepositorioUsuario(session).verificar_email(usuario,session)
   db_user2 = RepositorioUsuario(session).verificar_username(usuario,session)
   if db_user:
        error_message = "Este email já está cadastrado. Por favor, insira um email válido."
        return  JSONResponse(content={"detail": error_message}, status_code=status.HTTP_400_BAD_REQUEST)
   if db_user2:
        error_message = "Este nome já está cadastrado. Por favor, insira um nome válido."
        return  JSONResponse(content={"detail2": error_message}, status_code=status.HTTP_409_CONFLICT)

   usuario_criado =RepositorioUsuario(session).criar(usuario)
   return templates.TemplateResponse("verifique_seu_email.html",{"request":request,"new_user":usuario_criado})
