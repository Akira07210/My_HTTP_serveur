**Lancer le serveur :** python3 -m uvicorn main:app --reload


from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/userinfo")
async def get_user_info(request: Request):
    user_agent = request.headers.get("user-agent")
    client_host = request.client.host
    client_port = request.client.port

    return {
        "user_agent": user_agent,
        "ip": client_host,
        "port": client_port
    }
	
	
	
	
	
from fastapi import FastAPI, Request
from user_agents import parse

app = FastAPI()






@app.get("/userinfo")
async def get_user_info(request: Request):
    ua_string = request.headers.get("user-agent")
    user_agent = parse(ua_string)

    return {
        "browser": user_agent.browser.family,
        "browser_version": user_agent.browser.version_string,
        "os": user_agent.os.family,
        "os_version": user_agent.os.version_string,
        "device": user_agent.device.family,
        "is_mobile": user_agent.is_mobile,
        "is_tablet": user_agent.is_tablet,
        "is_pc": user_agent.is_pc
    }