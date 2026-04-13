from fastapi import FastAPI
from app.api.routes.satellites import router as satellites_router

app = FastAPI(title="Satellite Coverage Simulator API")

app.include_router(satellites_router)


@app.get("/")
def root():
    return {"message": "Satellite Coverage Simulator API is running"}