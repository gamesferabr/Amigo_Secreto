from sqlalchemy import select
from sqlalchemy.orm import Session
from models import models
from schemas import schemas

class RepositorioUsuario():
    def __init__(self,session:Session):
        self.session = session
    
    def criar(self, usuario: schemas.Usuario):
        usuario_bd = models.Usuario(name = usuario.name, last_name = usuario.last_name, user = usuario.user, password = usuario.password, email = usuario.email )
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh()
        return usuario_bd
   
    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt)
        return usuarios
    
    def obter():
        pass

    def remover():
        pass