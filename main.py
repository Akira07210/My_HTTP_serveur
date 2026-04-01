from fastapi import FastAPI, Request

app = FastAPI()

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