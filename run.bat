@echo off

:: Step 1: Go to project directory (skip if Jenkins is already there)
cd /d C:\Users\admin\Python\myntra

:: Step 2: Pull latest changes from GitHub
git pull origin main

:: Step 3: Activate virtual environment
call venv\Scripts\activate

:: Step 4: Install dependencies (good even if already installed, prevents failures)
pip install -r requirements.txt

:: Step 5: Run tests using the tag passed from Jenkins (like smoke, regression)
pytest -s -v -m %TEST_TAG% --alluredir=reports/

:: Step 6: Generate Allure report (optional but professional)
allure generate reports/ --clean -o allure-report

pause
