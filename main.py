# Lib
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from pydantic import BaseModel
import datetime
# Mes fichier
from log import log_the_visit_in_CSV

app = FastAPI()

# Autorisation des methodes OPTIONS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


###################################################
################## MES ENDPOINTS ##################

# Définition du modèle de données attendu
class Data(BaseModel):
    page: str
    screen : str

@app.post("/log_your_visit")
async def log_visit(data: Data, request: Request):
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent").replace(";",",")
    
    dictionnaire = data.dict()
    dictionnaire["Heure"] = datetime.datetime.now().strftime('%H:%M')
    dictionnaire["IP"]= client_ip
    dictionnaire["Agent"]= user_agent
    log_the_visit_in_CSV(dictionnaire)

    return {
	"IP": client_ip ,
	"Agent": user_agent,
    "received": data.dict()  # transforme le Pydantic model en dict
    }
    
    
    
    
###################################################
################## TUTO API FAST ##################

@app.get("/")
def read_root():
    return {"message": "Hello API 🚀"}

@app.post("/data")
def receive_data(data: dict):
    return {"received": data}
   

@app.get("/")
async def get_ip(request: Request):
    client_ip = request.client.host
    return {"ip": client_ip}
