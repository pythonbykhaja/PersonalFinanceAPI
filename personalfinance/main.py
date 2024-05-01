"""This is main method of fastapi
"""
from fastapi import FastAPI
from personalfinance.investment.apis.investment import router as investment_router
from personalfinance.models import Base
from personalfinance.database import engine

Base.metadata.create_all(bind=engine)



# create an instance of FastAPI
app = FastAPI()

app.include_router(investment_router, tags=['investment'], prefix="/api/investments")

@app.get("/api/healthchecker")
def health_checker():
    """
    Healthchecker endpoint
    """
    return {"status": "ok"}
