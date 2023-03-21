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

:: Rename file
echo on 
set "path_file=%~3"
set "file_name=%~4"
set "new_file_name=%~5"
goto :path_ren_check

:ren_file
set /p "path_file=Insira o diretório do arquivo: "
timeout 3

set /p "file_name=Insira o nome do arquivo: "
timeout 3

set /p "new_file_name=Insira o novo nome do arquivo: "
timeout 3

:path_ren_check
if "%file_name%"=="" goto :ren_file
if "%new_file_name%"=="" goto :ren_file

goto :script_ren_file

:: =================================================

:script_ren_file
echo off
S:
cd "%path_file%"
ren "%file_name%" "%new_file_name%"
pause
goto :finish_ren_file

:: =================================================

:finish_ren_file
timeout 2
exit 