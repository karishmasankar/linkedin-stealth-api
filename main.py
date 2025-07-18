
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from linkedin_bot import LinkedInBot

app = FastAPI()
bot = LinkedInBot()

class LoginRequest(BaseModel):
    username: str
    password: str

class ConnectRequest(BaseModel):
    profile_url: str
    message: str = ""

@app.post("/login")
def login(request: LoginRequest):
    try:
        bot.login(request.username, request.password)
        return {"status": "Logged in"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/connect")
def connect(request: ConnectRequest):
    try:
        result = bot.connect_or_message(request.profile_url, request.message)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/logout")
def logout():
    try:
        bot.close()
        return {"status": "Logged out"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
