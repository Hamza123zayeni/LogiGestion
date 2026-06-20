from fastapi import FastAPI
from database import Base, engine
import models
from routes import tickets

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(tickets.router)