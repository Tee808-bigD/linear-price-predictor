"""
Simple test script for the price prediction model
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

print("=" * 60)
print("TESTING PRICE PREDICTION MODEL")
print("=" * 60)

def test_data_loading():
    print("\n1. Testing data loading...")
    try:
        # Load sample data
        url = "https://raw.githubusercontent.com/MicrosoftLearning/mslearn-databricks/main/data/products.csv"
        df = pd.read_csv(url)
        print(f"✅ Data loaded successfully!")
        print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        print(f"   Columns: {list(df.columns)}")
        print(f"   Sample data:")
        print(df.head(3))
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def test_feature_engineering(df):
    print("\n2. Testing feature engineering...")
    try:
        # Create simple features
        df['ProductName_Length'] = df['ProductName'].str.len()
        df['Has_Mountain'] = df['ProductName'].str.contains('Mountain', case=False).astype(int)
        df['Has_Road'] = df['ProductName'].str.contains('Road', case=False).astype(int)
        
        print(f"✅ Features created!")
        print(f"   New columns: ProductName_Length, Has_Mountain, Has_Road")
        print(f"   Sample features:")
        print(df[['ProductName', 'ProductName_Length', 'Has_Mountain', 'ListPrice']].head(3))
        return df
    except Exception as e:
        print(f"❌ Error creating features: {e}")
        return None

def test_model_training(df):
    print("\n3. Testing model training...")
    try:
        # Prepare features
        feature_cols = ['ProductName_Length', 'Has_Mountain', 'Has_Road']
        X = df[feature_cols]
        y = df['ListPrice']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Evaluate
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        
        print(f"✅ Model trained successfully!")
        print(f"   Features used: {feature_cols}")
        print(f"   Training R² score: {train_score:.4f}")
        print(f"   Testing R² score: {test_score:.4f}")
        print(f"   Coefficients: {model.coef_}")
        print(f"   Intercept: {model.intercept_:.2f}")
        
        return model, feature_cols
    except Exception as e:
        print(f"❌ Error training model: {e}")
        return None, None

def test_predictions(model, feature_cols, df):
    print("\n4. Testing predictions...")
    try:
        # Test some predictions
        test_products = [
            {"name": "Mountain-100 Silver, 38", "expected": "high"},
            {"name": "Road Bike Blue", "expected": "medium"},
            {"name": "Water Bottle", "expected": "low"}
        ]
        
        print("   Testing predictions:")
        for product in test_products:
            # Create features for this product
            features = {
                'ProductName_Length': len(product['name']),
                'Has_Mountain': 1 if 'mountain' in product['name'].lower() else 0,
                'Has_Road': 1 if 'road' in product['name'].lower() else 0
            }
            
            # Convert to DataFrame
            X_new = pd.DataFrame([features])
            X_new = X_new[feature_cols]  # Ensure correct column order
            
            # Predict
            prediction = model.predict(X_new)[0]
            
            print(f"   - '{product['name']}'")
            print(f"     → Predicted price: ${prediction:.2f}")
            print(f"     → Expected: {product['expected']}")
        
        return True
    except Exception as e:
        print(f"❌ Error making predictions: {e}")
        return False

def save_model(model, feature_cols):
    print("\n5. Saving model...")
    try:
        # Create model directory if it doesn't exist
        os.makedirs("model", exist_ok=True)
        
        # Save model
        joblib.dump({
            'model': model,
            'feature_cols': feature_cols,
            'model_type': 'LinearRegression'
        }, "model/price_model.pkl")
        
        print(f"✅ Model saved to: model/price_model.pkl")
        print(f"   File size: {os.path.getsize('model/price_model.pkl') / 1024:.1f} KB")
        return True
    except Exception as e:
        print(f"❌ Error saving model: {e}")
        return False

def load_and_test_model():
    print("\n6. Loading and testing saved model...")
    try:
        if not os.path.exists("model/price_model.pkl"):
            print("❌ Model file not found!")
            return False
        
        # Load model
        model_data = joblib.load("model/price_model.pkl")
        model = model_data['model']
        feature_cols = model_data['feature_cols']
        
        print(f"✅ Model loaded successfully!")
        print(f"   Model type: {model_data.get('model_type', 'Unknown')}")
        print(f"   Features: {feature_cols}")
        
        # Test prediction with loaded model
        test_name = "Test Mountain Bike Pro"
        features = {
            'ProductName_Length': len(test_name),
            'Has_Mountain': 1 if 'mountain' in test_name.lower() else 0,
            'Has_Road': 1 if 'road' in test_name.lower() else 0
        }
        
        X_test = pd.DataFrame([features])[feature_cols]
        prediction = model.predict(X_test)[0]
        
        print(f"   Test prediction for '{test_name}': ${prediction:.2f}")
        return True
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False

def main():
    # Step 1: Test data loading
    df = test_data_loading()
    if df is None:
        return
    
    # Step 2: Test feature engineering
    df = test_feature_engineering(df)
    if df is None:
        return
    
    # Step 3: Test model training
    model, feature_cols = test_model_training(df)
    if model is None:
        return
    
    # Step 4: Test predictions
    test_predictions(model, feature_cols, df)
    
    # Step 5: Save model
    save_model(model, feature_cols)
    
    # Step 6: Load and test saved model
    load_and_test_model()
    
    print("\n" + "=" * 60)
    print("✅ MODEL TEST COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")