import sys
import os

print("=" * 50)
print("PYTHON DIAGNOSTICS")
print("=" * 50)

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path[:3]}...")

print("\nChecking pip...")
try:
    import pip
    print(f"✅ pip version: {pip.__version__}")
except:
    print("❌ pip not found")

print("\nTrying to install pandas...")
try:
    import subprocess
    result = subprocess.run([sys.executable, "-m", "pip", "install", "pandas"], 
                          capture_output=True, text=True)
    if "Successfully installed" in result.stdout:
        print("✅ pandas installed successfully")
    else:
        print(f"Output: {result.stdout[:200]}...")
        print(f"Error: {result.stderr[:200]}...")
except Exception as e:
    print(f"❌ Error: {e}")

input("\nPress Enter to exit...")