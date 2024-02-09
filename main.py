from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import dotenv_values
from pymongo import MongoClient
import certifi

from routes import router

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    app.mongodb_client = MongoClient(config["ATLAS_URI"], tlsCAFile=certifi.where())
    app.db = app.mongodb_client[config["DB_NAME"]]

    yield # serve the API

    # shutdown
    app.mongodb_client.close()

app = FastAPI(lifespan=lifespan)
app.include_router(router, tags=["posts"], prefix="/posts")
