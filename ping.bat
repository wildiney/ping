@ECHO OFF
set server=google.com.br

:waitloop
  @TIMEOUT /T 60
  ping -n 60 %server% > nul
  if errorlevel 1 goto :noServer

echo %server% is available
goto :EOF

:noServer
echo %server% is not available yet.
goto :waitloop
