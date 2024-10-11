@echo off
setlocal enabledelayedexpansion

rem Loop through each folder from Problem_1 to Problem_10
for /L %%i in (1,1,10) do (
    rem Define the folder name
    set "folder=Problem_%%i"
    
    rem Check if the folder exists and contains the __main__.py file
    if exist "!folder!\__main__.py" (
        echo Running "!folder!\__main__.py" in directory "!folder!"...
        rem Change to the problem folder and run the Python script
        pushd "!folder!" > nul
        python "__main__.py"
        popd > nul
        echo.
    ) else (
        echo Warning: "!folder!\__main__.py" not found or skipping TEMPLATE folder.
    )
)

rem Skip TEMPLATE folder if it exists
if exist "TEMPLATE\__main__.py" (
    echo Skipping TEMPLATE folder.
)

endlocal
pause
