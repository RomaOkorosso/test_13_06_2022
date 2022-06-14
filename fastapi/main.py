from fastapi import (
    FastAPI,
)
from fastapi.database import models
from fastapi.database.database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
