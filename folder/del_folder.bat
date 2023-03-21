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

:: Del Folder
set "folder_path_del=%~3"
goto :path_del_check

:del_folder
set /p "folder_name_del=Insira o caminho one a pasta está: "
timeout 2

:path_del_check
if "%folder_path_del%"=="" goto :del_folder

goto :script_del_folder

:: =============================================

:script_del_folder
echo off
rmdir /s /q "%folder_path_del%"
timeout 1
goto :finish_del_folder

:: =============================================

:finish_del_folder
timeout 2
exit