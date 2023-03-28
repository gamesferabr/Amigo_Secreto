from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models import models
from src.schemas import schemas
from passlib import hash
import jwt

class RepositorioUsuario():
    def __init__(self,session:Session):
        self.session = session
    
    #criar a função para verificar se tem um email cadastrado e se tiver ele não permite que o novo usuário cadastre o novo email, fazendo ele colocar outro
    def verificar_email(self, usuario: schemas.Usuario, db: Session):
        return db.query(models.Usuario_models).filter(models.Usuario_models.email == usuario.email).first()
    
    def verificar_username(self, usuario: schemas.Usuario, db: Session):
        return db.query(models.Usuario_models).filter(models.Usuario_models.makeuser == usuario.makeuser).first()
    
    def criar(self, usuario: schemas.Usuario):
        usuario_bd = models.Usuario_models(username = usuario.username, lastusername= usuario.lastusername, makeuser = usuario.makeuser, password = usuario.password, password2= usuario.password2, hashed_password = hash.bcrypt.hash(usuario.password),email = usuario.email)
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd
    
    def envia_email(usuario: models.Usuario_models):
    # Define a chave secreta para assinar o token
      # Cria um objeto JWT
      token = usuario.hashed_password
      
      # Envia o token para o email
      return f"Olá, {usuario.username}, precisamos que você confirme o seu cadastro, seu código é "
    #
    
    
    
    #async def autentificar_usuario(self,email):
    #    user = await 

   
    def listar(self):
        stmt = select(models.Usuario_models)
        usuarios = self.session.execute(stmt)
        return usuarios
    
    def obter():
        pass

    def remover():
        pass