
from operator import index
from sqlite3 import Cursor, connect
from fastapi import Body, FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .import models, schema
from .database import engine, get_db
from sqlalchemy.orm import Session
from .import routes

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(routes.router)