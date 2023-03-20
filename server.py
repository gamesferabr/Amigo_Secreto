import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from . import rotas_usuario

app = FastAPI()
app.add_middleware(CORSMiddleware, 
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

#Usuários
#app.include_router(rotas_usuario.router)

if __name__ == '__main__':
  uvicorn.run(app)
