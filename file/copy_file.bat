@echo off

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

:: Copy file
echo on
set "path_1_copy_file=%~3"
set "path_2_copy_file=%~4"
set "file_name_copy=%~5"
goto :path_copy_check

:copy_file
set /p "path_1_copy_file=Insira o caminho que o arquivo esta: "
timeout 3

set /p "path_2_copy_file=Insira o caminho para onde o arquivo  vai: "
timeout 3

set /p "file_name_copy=Insira o nome do arquivo (com a extensão do mesmo): "
timeout 3

:path_copy_check
if "%path_1_copy_file%"=="" goto :copy_file
if "%path_2_copy_file%"=="" goto :copy_file
if "%file_name_copy%"=="" goto :copy_file


goto :script_copy_file

:: =============================================

:script_copy_file
echo off
net use s: \\bosch.com\dfsrb\dfsbr\LOC\Ca1 /persistent:no
robocopy "%path_1_copy_file%" "%path_2_copy_file%" "%file_name_copy%"
pause
goto :finish_copy_file

:: =============================================

:finish_copy_file
timeout 2
exit