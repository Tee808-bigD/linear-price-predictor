import pandas as pd
import joblib
import os

def load_model():
    model_path = "model/simple_model.pkl"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")
    
    data = joblib.load(model_path)
    return data['model'], data['feature_cols']

def predict_price(product_name, category):
    try:
        model, feature_cols = load_model()
        
        features = {
            'ProductName_Length': len(str(product_name)),
            'Has_Mountain': 1 if 'mountain' in str(product_name).lower() else 0,
            'Has_Road': 1 if 'road' in str(product_name).lower() else 0,
            'Has_Black': 1 if 'black' in str(product_name).lower() else 0,
            'Has_Silver': 1 if 'silver' in str(product_name).lower() else 0,
            'Has_Blue': 1 if 'blue' in str(product_name).lower() else 0,
        }
        
        for col in feature_cols:
            if col.startswith('cat_'):
                features[col] = 0
        
        cat_col = f'cat_{category}'
        if cat_col in features:
            features[cat_col] = 1
        
        X = pd.DataFrame([features])
        X = X[feature_cols]
        
        prediction = model.predict(X)[0]
        return round(float(prediction), 2)
        
    except Exception as e:
        print(f"Prediction error: {e}")
        return None
