from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "GameNexus API is alive and kicking!"}
