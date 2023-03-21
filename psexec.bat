@echo off


:: param1 e param2 estão sendo passados no teste.py
:: Fetch param1
set "param1=%~1"
goto :param1Check
:param1Prompt
set /p "param1=Enter parameter 1: "
:param1Check
if "%param1%"=="" goto :param1Prompt

:: Fetch param2
set "param2=%~2"
goto :param2Check
:param2Prompt
set /p "param2=Enter parameter 2: "
:param2Check
if "%param2%"=="" goto :param2Prompt

psexec -u "%param1%" -p "%param2%" psexec.bat


:: ===================================================
:: ===================================================

:: Fetch param3
set "param3=%~3"
goto :param3Check
:param3Prompt
set /p "param3=Enter the operation (copy/del): "
timeout 2
:param3Check
if "%param3%"=="" goto :param3Prompt
if "%param3%"=="copy" goto :copy_folder
if "%param3%"=="del" goto :del_folder



:: =============================================
:: =============================================

echo on

:: Copy Folder
set "path_1_copy=%~4"
set "path_2_copy=%~5"
set "folder_name_copy=%~6"
goto :path_copy_check

:copy_folder
echo.
echo Copiando uma pasta
echo Copie o caminho onde se encontra a pasta

start explorer
set /p "path_1_copy=Insira o caminho que a pasta esta: "
tskill explorer
timeout 3

echo.
echo Copie o caminho para one a pasta vai
start explorer
set /p "path_2_copy=Insira o caminho para onde a pasta vai: "
tskill explorer
timeout 3

:: VOLTA AQUIIIIII
:: PRECISA FAZER A VEIRIFCAÇÃO DO PATH_COPY_CHECK
:path_copy_check
if "%path_1_copy%"=="" goto :copy_folder
if "%path_2_copy%"=="" goto :copy_folder
goto :script_copy

:: =============================================

:script_copy
echo Executando comando de copia
echo off
robocopy %path_1_copy% %path_2_copy% /e
pause
goto :finish_copy

:: =============================================

:finish_copy
echo on
echo Comando de copia concluido
timeout 2
exit

:: =============================================

:path_copy_check
if "%path_1_copy%"=="" goto :copy_folder
if "%path_2_copy%"=="" goto :copy_folder
if "%folder_name_copy%"=="" goto :copy_folder


:: =============================================
:: =============================================

:: Del Folder
set "path_1_del=%~7"
set "folder_name_del=%~8"
goto :path_del_check

:del_folder
echo.
echo Deletando uma pasta
echo Copie o caminho onde se encontra a pasta

start explorer
set /p "path_1_del=Insira o caminho que a pasta esta: "
tskill explorer
timeout 3

echo.
set /p "folder_name_del=Insira o nome da pasta: "
timeout 2
goto :script_del

:: =============================================

:script_del
echo.
echo Executando comando Del
echo off
cd "%path_1_del%"
rmdir "%folder_name_del%" /s /q
timeout 1
goto :finish_del

:: =============================================

:finish_del
echo on
echo Comando del concluido
timeout 2
exit

:: =============================================

:path_copy_check
if "%path_1_del%"=="" goto :del_folder
if "%folder_name_del%"=="" goto :del_folder

:: =============================================
:: =============================================


