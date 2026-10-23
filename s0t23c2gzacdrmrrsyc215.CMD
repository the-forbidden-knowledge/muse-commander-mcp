@echo off
setlocal

cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo [ERRO] Python nao encontrado no PATH. Instale o Python 3 e rode de novo.
  pause
  exit /b 1
)

set TOKENFILE=%USERPROFILE%\.config\muse-commander-agent\token

if not exist "%TOKENFILE%" (
  echo [INFO] Primeira execucao: gerando instalacao e token...
  echo.
  python hr67y7j3bfdtjvi4vys6dj.py install
  if errorlevel 1 (
    echo.
    echo [ERRO] Falha na instalacao.
    pause
    exit /b 1
  )
  echo.
  echo [INFO] Guarde o token acima. Ele nao sera mostrado de novo.
  echo.
)

echo [INFO] Conectando: bind automatico no tailnet, com rotacao sozinha...
echo [INFO] Mantenha esta janela aberta. Ctrl+C para encerrar.
echo.
python hr67y7j3bfdtjvi4vys6dj.py run --bind tailnet

echo.
echo [INFO] Agente encerrado.
pause
endlocal
