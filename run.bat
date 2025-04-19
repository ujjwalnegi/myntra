@echo off
call venv\scripts\activate
pytest -s -v .\test_cases
pause


