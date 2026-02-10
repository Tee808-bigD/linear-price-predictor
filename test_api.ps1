# PowerShell script to test the API
Write-Host "Testing Price Prediction API" -ForegroundColor Green
Write-Host "=" * 50

# Wait a moment for API to start
Start-Sleep -Seconds 2

# Test 1: Health endpoint
Write-Host "`n1. Testing health endpoint..." -ForegroundColor Cyan
try {
    $health = Invoke-RestMethod -Uri "http://localhost:8000/health" -Method Get
    Write-Host "   ✅ Health: $($health.status)" -ForegroundColor Green
    Write-Host "   Model loaded: $($health.model_loaded)" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Health check failed: $_" -ForegroundColor Red
    Write-Host "   Make sure the API is running!" -ForegroundColor Yellow
    exit
}

# Test 2: Make predictions
Write-Host "`n2. Making predictions..." -ForegroundColor Cyan

$testProducts = @(
    @{product_name = "Mountain-100 Silver, 38"},
    @{product_name = "Road Bike Blue Professional"},
    @{product_name = "Water Bottle 1L"},
    @{product_name = "Mountain Bike Helmet Black"},
    @{product_name = "Road Cycling Jersey"}
)

foreach ($product in $testProducts) {
    $body = $product | ConvertTo-Json
    
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:8000/predict" `
            -Method Post `
            -Body $body `
            -ContentType "application/json"
        
        Write-Host "   ✅ $($response.product_name)" -ForegroundColor White
        Write-Host "      Price: `$$($response.predicted_price)" -ForegroundColor Green
        Write-Host "      Confidence: $($response.confidence)" -ForegroundColor Yellow
        
        # Show features
        $features = $response.features | ConvertTo-Json -Compress
        Write-Host "      Features: $features" -ForegroundColor Gray
        
    } catch {
        Write-Host "   ❌ Failed: $($product.product_name)" -ForegroundColor Red
        Write-Host "      Error: $_" -ForegroundColor Red
    }
    
    Write-Host ""
}

# Test 3: Test the docs page
Write-Host "`n3. Testing documentation..." -ForegroundColor Cyan
try {
    $docs = Invoke-WebRequest -Uri "http://localhost:8000/docs" -Method Head
    Write-Host "   ✅ API Documentation is available" -ForegroundColor Green
    Write-Host "   📚 Open: http://localhost:8000/docs" -ForegroundColor Cyan
} catch {
    Write-Host "   ⚠️ Docs page might not be accessible via script" -ForegroundColor Yellow
}

Write-Host "`n" + "=" * 50
Write-Host "API TEST COMPLETE!" -ForegroundColor Green
Write-Host "=" * 50