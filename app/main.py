from fastapi import FastAPI

app = FastAPI(title="Tasks manager")

@app.get("/")
def read_root():
    return {"message": "Hello World!"}