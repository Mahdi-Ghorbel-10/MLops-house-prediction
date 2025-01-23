from fastapi import FastAPI, HTTPException
import uvicorn
import pandas as pd
import joblib
from pydantic import BaseModel

app = FastAPI(title="House Price Prediction API", description="Predicts house prices.", version="1.0")

# Load the trained model
try:
    model = joblib.load("house_price_model.pkl")
except FileNotFoundError:
    raise RuntimeError("Model file not found. Make sure 'house_price_model.pkl' exists in the same directory.")

# Define the input data model using Pydantic
class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int
    guestroom: int
    basement: int
    hotwaterheating: int
    airconditioning: int
    parking: int
    prefarea: int
    furnishingstatus: int



@app.post("/predict")
async def predict_price(house_data: HouseData):
    try:
        # Convert Pydantic model to DataFrame for prediction
        input_df = pd.DataFrame([house_data.dict()])

        # Make prediction
        predicted_price = model.predict(input_df)[0]

        return {"predicted_price": predicted_price}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # Changed port to 8000