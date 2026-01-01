@echo off
echo Compiling Kava...

cd /d ../../src

rem Limpa builds antigos
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del Kava.spec 2>nul

set METADATA=..\art\buildScripts\metadata.txt

if exist "%METADATA%" (
    echo Metadata found. Building with version info...
    python -m PyInstaller ^
    --onefile ^
    --name Kava ^
    --icon ..\art\Icon.ico ^
    --version-file "%METADATA%" ^
    Interp.py
) else (
    echo Metadata not found. Building without version info...
    python -m PyInstaller ^
    --onefile ^
    --name Kava ^
    --icon ..\art\Icon.ico ^
    Interp.py
)

pause
