@echo off 

set XD=%CD%
set /P MCP=Please enter the path to Forge-MCP on your computer: 
	
cd %MCP%
echo.
echo.
echo Forge path:
echo %CD%
echo.
echo Current path:
echo %XD%
echo.
echo Preparing to copy...

echo.
copy %MCP%\conf\fields.csv %XD%\fields.csv
copy %MCP%\conf\methods.csv %XD%\methods.csv
copy %MCP%\runtime\bin\fernflower.jar %XD%\fernflower.jar
echo.
xcopy %MCP%\runtime\bin\python %XD%\python\ /H /E /G /Q /R /Y
echo.

echo.
pause