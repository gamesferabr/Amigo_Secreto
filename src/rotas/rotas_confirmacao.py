from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.config.database import get_db,engine
from src.models import models
from fastapi.responses import HTMLResponse, JSONResponse

#Para criar a tabela no banco de dados
models.Base.metadata.create_all(engine)

#app = FastAPI()
route2 = APIRouter()

templates = Jinja2Templates(directory="templates")

@route2.get("/verifique_seu_email",response_class=HTMLResponse)
def get_verifique_seu_email(request:Request):
   return templates.TemplateResponse("verifique_seu_email.html",{"request":request})

