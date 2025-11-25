<#
    run-classifier-conda.ps1
    Wrapper PowerShell para ejecutar runner.py usando un entorno Conda.
    Autor: Manuel Daza Ramirez

    Uso:

      .\run-classifier-conda.ps1 -Text "texto a clasificar"
      .\run-classifier-conda.ps1 -File ".\examples\caso_01_victima_directa.txt"
      .\run-classifier-conda.ps1 -File ".\ejemplo.txt" -NoDB

    Requisitos:
      - Conda instalado y disponible en PATH.
      - Entorno conda creado (por defecto: ubpd_env).
      - OPENAI_API_KEY definida como variable de entorno.
#>

param(
    [string]$Text,
    [string]$File,
    [switch]$NoDB,
    [string]$CondaEnv = "ubpd_env"   # nombre del entorno conda
)

Write-Host "==================================" -ForegroundColor Cyan
Write-Host " UBPD - Clasificador Testimonios (Conda)" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan

# ---------------------------------------
# 1. Verificar API key
# ---------------------------------------
if (-not $env:OPENAI_API_KEY) {
    Write-Host "[ERROR] La variable OPENAI_API_KEY no esta definida." -ForegroundColor Red
    Write-Host "Definela, por ejemplo:" -ForegroundColor Yellow
    Write-Host '  setx OPENAI_API_KEY "sk-xxxx"' -ForegroundColor Yellow
    Write-Host "Luego abre una nueva ventana de PowerShell." -ForegroundColor Yellow
    exit 1
}

# ---------------------------------------
# 2. Verificar que conda este disponible
# ---------------------------------------
$condaVersionOutput = & conda --version 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] 'conda' no esta disponible en esta sesion." -ForegroundColor Red
    Write-Host "Abre 'Anaconda Prompt' o inicializa conda en PowerShell (conda init pwsh)." -ForegroundColor Yellow
    exit 1
}

$condaVersionText = ($condaVersionOutput | Out-String).Trim()
Write-Host "[OK] Conda detectado: $condaVersionText" -ForegroundColor Green

# ---------------------------------------
# 3. Construir comando base con conda run
# ---------------------------------------
$cmd = "conda run -n $CondaEnv python runner.py"

# ---------------------------------------
# 4. Anadir parametros (text / file / no-db)
# ---------------------------------------
if ($Text) {
    # Escapar comillas dobles en el texto
    $escapedText = $Text.Replace('"', '\"')
    $cmd += " --text `"$escapedText`""
}

if ($File) {
    if (-not (Test-Path $File)) {
        Write-Host "[ERROR] No se encontro el archivo: $File" -ForegroundColor Red
        exit 1
    }
    $cmd += " --file `"$File`""
}

if ($NoDB) {
    $cmd += " --no-db"
}

# ---------------------------------------
# 5. Mostrar comando final
# ---------------------------------------
Write-Host ""
Write-Host "Ejecutando en entorno conda '$CondaEnv':" -ForegroundColor Cyan
Write-Host "  $cmd" -ForegroundColor White

Write-Host ""
Write-Host "Procesando..." -ForegroundColor Yellow

# ---------------------------------------
# 6. Ejecutar runner.py via conda run
# ---------------------------------------
Invoke-Expression $cmd

Write-Host ""
Write-Host "[FIN] Ejecucion completada." -ForegroundColor Green
