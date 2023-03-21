@echo off

net use s: \\bosch.com\dfsrb\dfsbr\LOC\Ca1 /persistent:no

:: Fetch param1
set "param1=%~1"
goto :param1Check
:param1Prompt
set /p "param1=User: "
:param1Check
if "%param1%"=="" goto :param1Prompt

:: Fetch param2
set "param2=%~2"
goto :param2Check
:param2Prompt
set /p "param2=Password: "
:param2Check
if "%param2%"=="" goto :param2Prompt

:: =================================================
:: =================================================



:: Del file
set "file_name_del=%~3"
goto :path_del_check

:del_file
set /p "file_name_del=Insira o nome do arquivo (com a extensão do mesmo): "
timeout 3

:path_del_check
if "%file_name_del%"=="" goto :del_file

goto :script_del_file

:: =============================================

:script_del_file
echo off
del /f "%file_name_del%"
pause
goto :finish_del_file

:: =============================================

:finish_del_file
timeout 2
exit