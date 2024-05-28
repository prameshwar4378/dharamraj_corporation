@echo off
cd path\to\your\django\project

echo Starting Django server...
start /B py manage.py runserver

timeout /t 10 /nobreak > nul

echo Opening http://127.0.0.1:8000/ in Google Chrome...
start chrome http://127.0.0.1:8000/

exit
