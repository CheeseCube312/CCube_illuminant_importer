@echo off
:: Check if the virtual environment already exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Install required dependencies
echo Installing dependencies...
pip install pandas numpy

:: Run the Python script
echo Running the Python script...
python illuminantImporter.py

:: Deactivate the virtual environment after script completes
echo Deactivating virtual environment...
deactivate

echo Done!
pause
