from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(text: InputText):
    sentiment = predict_sentiment(text.text)
    return {"sentiment": sentiment}
