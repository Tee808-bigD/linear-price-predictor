import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

def train_simple_model():
    print("Training simple linear regression model...")
    
    # Load data
    url = "https://raw.githubusercontent.com/MicrosoftLearning/mslearn-databricks/main/data/products.csv"
    df = pd.read_csv(url)
    
    # Save locally
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/products.csv", index=False)
    
    # Simple features
    df['ProductName_Length'] = df['ProductName'].str.len()
    df['Has_Mountain'] = df['ProductName'].str.contains('Mountain', case=False).astype(int)
    df['Has_Road'] = df['ProductName'].str.contains('Road', case=False).astype(int)
    df['Has_Black'] = df['ProductName'].str.contains('Black', case=False).astype(int)
    df['Has_Silver'] = df['ProductName'].str.contains('Silver', case=False).astype(int)
    df['Has_Blue'] = df['ProductName'].str.contains('Blue', case=False).astype(int)
    
    # One-hot encode Category
    category_dummies = pd.get_dummies(df['Category'], prefix='cat', drop_first=True)
    df = pd.concat([df, category_dummies], axis=1)
    
    # Prepare features
    feature_cols = ['ProductName_Length', 'Has_Mountain', 'Has_Road', 
                   'Has_Black', 'Has_Silver', 'Has_Blue'] + list(category_dummies.columns)
    
    X = df[feature_cols]
    y = df['ListPrice']
    
    # Split and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    score = model.score(X_test, y_test)
    print(f"Model R² score: {score:.4f}")
    
    # Save
    os.makedirs("model", exist_ok=True)
    joblib.dump({
        'model': model,
        'feature_cols': feature_cols,
        'score': score
    }, "model/simple_model.pkl")
    
    print("✅ Model trained and saved!")
    return model, feature_cols, score

if __name__ == "__main__":
    train_simple_model()
