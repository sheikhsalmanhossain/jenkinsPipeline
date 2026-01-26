from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "123, This is salman. I am a DevOps engineer"}