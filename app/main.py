from fastapi import FastAPI
import os
app = FastAPI(title="FastAPI CI/CD Demo")

@app.get("/health")
def health():
    return {"status": "OK"}
