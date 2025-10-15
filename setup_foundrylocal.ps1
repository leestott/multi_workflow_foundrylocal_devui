# PowerShell script to configure FoundryLocal with a fixed port
param(
    [int]$Port = 58123
)

Write-Host "🔧 Configuring FoundryLocal with fixed port..." -ForegroundColor Green
Write-Host ""

# Set FoundryLocal to use a fixed port
Write-Host "Setting FoundryLocal port to $Port..." -ForegroundColor Cyan
try {
    $output = foundry service set --port $Port --show 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ FoundryLocal port configured successfully!" -ForegroundColor Green
        Write-Host "   Service running on: http://127.0.0.1:$Port/" -ForegroundColor White
    } else {
        Write-Host "❌ Failed to configure FoundryLocal port" -ForegroundColor Red
        Write-Host "Error: $output" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "❌ Error configuring FoundryLocal: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Update .env file with the correct endpoint
$envFile = Join-Path $PSScriptRoot ".env"
Write-Host "Updating .env file..." -ForegroundColor Cyan

if (Test-Path $envFile) {
    $envContent = Get-Content $envFile -Raw
    $newEndpoint = "http://127.0.0.1:$Port/v1/"
    
    # Update the endpoint in .env file
    $envContent = $envContent -replace 'FOUNDRYLOCAL_ENDPOINT="[^"]*"', "FOUNDRYLOCAL_ENDPOINT=`"$newEndpoint`""
    
    Set-Content -Path $envFile -Value $envContent -NoNewline
    Write-Host "✅ .env file updated with endpoint: $newEndpoint" -ForegroundColor Green
} else {
    Write-Host "⚠️  .env file not found, creating one..." -ForegroundColor Yellow
    $envContent = @"
FOUNDRYLOCAL_ENDPOINT="http://127.0.0.1:$Port/v1/"
FOUNDRYLOCAL_MODEL_DEPLOYMENT_NAME="deepseek-r1-distill-qwen-7b-qnn-npu:1"
OPENAI_CHAT_MODEL_ID="deepseek-r1-distill-qwen-7b-qnn-npu:1"
"@
    Set-Content -Path $envFile -Value $envContent
    Write-Host "✅ .env file created" -ForegroundColor Green
}

Write-Host ""

# Test the connection
Write-Host "Testing FoundryLocal connection..." -ForegroundColor Cyan
try {
    $response = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/v1/models" -Method Get -TimeoutSec 10
    if ($response.data) {
        Write-Host "✅ FoundryLocal is accessible!" -ForegroundColor Green
        Write-Host "Available models:" -ForegroundColor White
        foreach ($model in $response.data) {
            Write-Host "   - $($model.id)" -ForegroundColor Gray
        }
    }
} catch {
    Write-Host "❌ Could not connect to FoundryLocal" -ForegroundColor Red
    Write-Host "   Make sure FoundryLocal is running and accessible" -ForegroundColor Yellow
    Write-Host "   Error: $_" -ForegroundColor Red
}

Write-Host ""
Write-Host "🎉 Setup complete!" -ForegroundColor Green
Write-Host "Now you can run your application with:" -ForegroundColor White
Write-Host "   python main.py" -ForegroundColor Cyan
Write-Host "   OR" -ForegroundColor White
Write-Host "   ./run_chainlit.ps1" -ForegroundColor Cyan