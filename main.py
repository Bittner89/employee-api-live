from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status":"all good and dandy"}