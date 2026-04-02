# Lib
from fastapi import FastAPI, Request
from pydantic import BaseModel
from user_agents import parse
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
    browser= user_agent.browser.family,
    browser_version= user_agent.browser.version_string,
    os= user_agent.os.family,
    os_version= user_agent.os.version_string,
    device= user_agent.device.family,
    is_mobile= user_agent.is_mobile,
    is_tablet= user_agent.is_tablet,
    is_pc= user_agent.is_pc
    data_track = data.dict()

    print(f"DEBUG : {client_ip},{browser},{os},{device},mobile : {is_mobile}, PC : {is_pc}\n Data track : {}")
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