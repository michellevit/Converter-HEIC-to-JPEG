@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Running HEIC to JPEG converter script...
python heic-converter.py

echo Deactivating virtual environment...
call venv\Scripts\deactivate

echo Script execution finished.
pause
