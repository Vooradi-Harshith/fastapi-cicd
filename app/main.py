from fastapi import FastAPI
app = FastAPI(title="FastAPI CI/CD Demo")

@app.get("/health")
def health():
    return {"status": "OK"}
