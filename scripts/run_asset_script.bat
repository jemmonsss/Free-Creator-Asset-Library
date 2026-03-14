@echo off
REM Run the generator relative to this script's directory.
python "%~dp0generate_asset_structure.py" %*
pause
