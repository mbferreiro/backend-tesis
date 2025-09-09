from fastapi import FastAPI

app = FastAPI(title="Tesis Backend API")

@app.get("/")
def root():
    return {"message": "Backend Tesis funcionando 🚀"}
