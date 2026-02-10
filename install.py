"""
Simple Python installer - no PowerShell issues
"""
import subprocess
import sys

packages = [
    "pandas==2.1.3",
    "scikit-learn==1.3.2",
    "joblib==1.3.2",
    "fastapi==0.104.1",
    "uvicorn[standard]==0.24.0",
    "numpy==1.24.3"
]

print("Installing Python packages...")
print("-" * 40)

for package in packages:
    print(f"Installing {package}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} installed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")

print("-" * 40)
print("✅ All packages installed!")
print("\nTo run the project: python main.py")