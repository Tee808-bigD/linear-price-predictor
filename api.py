from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from model.predict import predict_price

app = FastAPI(title="Simple Price Predictor", version="1.0")

class ProductRequest(BaseModel):
    product_name: str
    category: str

class PredictionResponse(BaseModel):
    product_name: str
    category: str
    predicted_price: float
    message: str

@app.get("/")
def read_root():
    return {"message": "Simple Price Prediction API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
def predict(product: ProductRequest):
    try:
        price = predict_price(product.product_name, product.category)
        
        if price is None:
            return PredictionResponse(
                product_name=product.product_name,
                category=product.category,
                predicted_price=0.0,
                message="Prediction failed"
            )
        
        return PredictionResponse(
            product_name=product.product_name,
            category=product.category,
            predicted_price=price,
            message="Success"
        )
        
    except Exception as e:
        return PredictionResponse(
            product_name=product.product_name,
            category=product.category,
            predicted_price=0.0,
            message=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
