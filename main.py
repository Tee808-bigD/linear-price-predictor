"""
Main script to train model and run API
"""
import sys
import subprocess
import os

def check_requirements():
    """Check if packages are installed"""
    try:
        import pandas
        import sklearn
        import fastapi
        import uvicorn
        return True
    except ImportError:
        return False

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def train_model():
    """Train the model"""
    print("Training model...")
    from model.train import train_simple_model
    train_simple_model()

def run_api():
    """Run the API"""
    print("Starting API...")
    import uvicorn
    from app.api import app
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

def main():
    """Main function"""
    print("=" * 50)
    print("SIMPLE PRICE PREDICTOR")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        print("Requirements not installed. Installing...")
        install_requirements()
    
    # Train model (if not already trained)
    if not os.path.exists("model/simple_model.pkl"):
        train_model()
    else:
        print("Model already trained.")
    
    # Run API
    print("\n✅ Ready! Starting API server...")
    print("🌐 Open: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    print("🛑 Press Ctrl+C to stop")
    print("=" * 50)
    
    run_api()

if __name__ == "__main__":
    main()