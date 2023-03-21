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

:: Copy Folder
set "path_1_copy_folder=%~3"
set "path_2_copy_folder=%~4"
goto :path_copy_check

:copy_folder
set /p "path_1_copy_folder=Insira o caminho que a pasta esta: "
timeout 3

set /p "path_2_copy_folder=Insira o caminho para onde a pasta vai: "
timeout 3

:path_copy_check
if "%path_1_copy_folder%"=="" goto :copy_folder
if "%path_2_copy_folder%"=="" goto :copy_folder

goto :script_copy_folder

:: =============================================

:script_copy_folder
echo off
robocopy "%path_1_copy_folder%" "%path_2_copy_folder%" /e
robocopy "%path_1_copy_folder%" "%path_2_copy_folder%"
pause
goto :finish_copy_folder

:: =============================================

:finish_copy_folder
echo on
timeout 2
exit