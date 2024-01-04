@echo off
where pythonw > nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas trouvé ! Tu peux l'installer depuis le Microsoft store ou en ouvrant un CMD et en tapant " python " !
    pause
    exit /b 1
)
echo Tu peux fermer cette fenetre apres le lancement du programme ! 
pythonw .\assets\naeStats.py > output.txt 2>&1
pause
