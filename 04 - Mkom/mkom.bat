@echo off
setlocal

:: Caminho para o diretório onde o arquivo .yxmd está localizado
set "directory=\\192.168.10.21\saturno\24 - MIS\07 - TIM\32 - Base MKOM\01 - Fluxo"

:: Nome do arquivo .yxmd a ser executado
set "file=BASE_MKOM.yxmd"

:: Caminho completo para o arquivo .yxmd
set "yxmd_file=%directory%\%file%"

:: Caminho para o arquivo de log (log.txt no mesmo diretório)
set "log=%directory%\log.txt"

:: Executa o arquivo .yxmd com Alteryx e redireciona a saída para o arquivo de log
"C:\Users\robo_mis_mfd\AppData\Local\Alteryx\bin\AlteryxEngineCmd.exe" "%yxmd_file%" > "%log%" 2>&1

:: Aguarde para que o usuário possa ver a saída (opcional)
pause

endlocal
