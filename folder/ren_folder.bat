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

:: Rename folder
echo on 
set "path_folder=%~3"
set "folder_name=%~4"
set "new_folder_name=%~5"
goto :path_ren_check

:ren_folder
set /p "path_folder=Insira o caminho da pasta: "
timeout 3

set /p "folder_name=Insira o nome da pasta: "
timeout 3

set /p "new_folder_name=Insira o novo nome da pasta: "
timeout 3

:path_ren_check
if "%path_folder%"=="" goto :ren_folder
if "%folder_name%"=="" goto :ren_folder
if "%new_folder_name%"=="" goto :ren_folder

goto :script_ren_folder

:: =================================================

:script_ren_folder
echo off 
S:
cd "%path_folder%"
rename "%folder_name%" "%new_folder_name%"
pause
goto :finish_ren_folder

:: =================================================

:finish_ren_folder
timeout 2
exit 