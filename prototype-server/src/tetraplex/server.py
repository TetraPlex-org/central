from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
async def greet():
    return {"welcome" : "tetraplex"}

if __name__== "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")