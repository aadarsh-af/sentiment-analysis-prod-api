from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status
from uvicorn.config import LOGGING_CONFIG

import typing as t
import uvicorn
import os

load_dotenv(override=True)

api_metadata = [
    {
        "name": "root",
        "description": "Home Page of the API",
    },
    {
        "name": "get_sentiment",
        "description": "Returns the sentiment of the input phrase",
    },
]

app = FastAPI(title="Sentiment Analysis API", openapi_tags=api_metadata)

default_datetime_format = "%Y-%m-%d %H:%M:%S"
LOGGING_CONFIG["formatters"]["default"]["datefmt"] = default_datetime_format
LOGGING_CONFIG["formatters"]["access"]["datefmt"] = default_datetime_format
LOGGING_CONFIG["formatters"]["default"][
    "fmt"
] = "%(asctime)s %(levelprefix)s %(message)s"
LOGGING_CONFIG["formatters"]["access"][
    "fmt"
] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'


AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
known_tokens = {AUTH_TOKEN}
get_bearer_token = HTTPBearer(auto_error=False)


class UnauthorizedMessage(BaseModel):
    detail: str = "Bearer token missing or unknown"


def get_token(
    auth: t.Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
) -> str:
    if auth is None or (token := auth.credentials) not in known_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=UnauthorizedMessage().detail,
        )
    return token


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float
