from src.api_utils import app
from src.api_utils import SentimentResponse
from src.api_utils import TextRequest
from src.api_utils import Depends
from src.api_utils import get_token
from src.models.sa_model import sentiment_analyzer


@app.get("/", tags=["root"])
def hello():
    return "Sentiment Analysis API deployed with Docker Compose"


@app.post("/get_sentiment/", response_model=SentimentResponse, tags=["get_sentiment"])
def analyze_sentiment(request: TextRequest, token: str = Depends(get_token)):
    result = sentiment_analyzer(request.text)[0]
    sentiment = result["label"]
    confidence = result["score"]

    return SentimentResponse(sentiment=sentiment, confidence=confidence)


if __name__ == "__main__":
    from src.api_utils import uvicorn
    from src.api_utils import LOGGING_CONFIG

    uvicorn.run(
        app,
        port=80,
        host="0.0.0.0",
        log_config=LOGGING_CONFIG,
    )
