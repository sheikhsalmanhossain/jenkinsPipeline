from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "123, I'm salman. I am a DevOps engineer"}
