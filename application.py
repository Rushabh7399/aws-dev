from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def test():
    DB_NAME = os.getenv("DB_NAME", "Rushabh Shah"}
    return {"status": f"working: {DB_NAME}"}
