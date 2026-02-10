import requests
import json

# API URL
API_URL = "http://localhost:8000/predict"

# Test products
test_products = [
    "Mountain-100 Silver, 38",           # From original dataset
    "Road-150 Red, 44",                  # From dataset
    "Mountain Bike Pro Carbon",          # Realistic
    "Road Racing Bike Lightweight",      # Realistic  
    "Bike Helmet Black",                 # Accessory
    "Water Bottle",                      # Cheap item
    "Electric Mountain Bike Pro 2024",   # E-bike
    "Kids Bike 16 inch",                 # Children's
    "Bike Repair Kit Tool Set",          # Accessory kit
    "Carbon Fiber Road Bike Frame",      # Component
]

print("=" * 70)
print("QUICK PRICE PREDICTION TEST")
print("=" * 70)

for product in test_products:
    try:
        # Make prediction request
        response = requests.post(
            API_URL,
            json={"product_name": product},
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ {product[:40]:<40} → ${data['predicted_price']:>8.2f}")
            print(f"   Features: Length={data['features']['ProductName_Length']}, "
                  f"Mountain={data['features']['Has_Mountain']}, "
                  f"Road={data['features']['Has_Road']}, "
                  f"Confidence: {data['confidence']}")
        else:
            print(f"❌ {product[:40]:<40} → Failed (Status: {response.status_code})")
            
    except Exception as e:
        print(f"❌ {product[:40]:<40} → Error: {str(e)[:50]}")

print("=" * 70)
print(f"Tested {len(test_products)} products")
print("Open http://localhost:8000/docs for interactive testing")
print("=" * 70)