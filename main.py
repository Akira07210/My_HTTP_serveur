# Lib
from fastapi import FastAPI, Request
from pydantic import BaseModel
# Mes fichier
from log import log_the_visit_in_CSV

app = FastAPI()
    
###################################################
################## MES ENDPOINTS ##################

# Définition du modèle de données attendu
class Data(BaseModel):
    page: str
    screen : str

@app.get("/log_your_visit")
async def log_visit(data: Data, request: Request):

    client_ip = request.client.host
    user_agent = request.headers.get("user-agent")
    data_track = data.dict()

    print(f"DEBUG : {client_ip}, Data track : {data_track}")
    return {
        "ip": client_ip,
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
