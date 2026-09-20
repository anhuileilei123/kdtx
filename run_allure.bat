@echo off
chcp 65001 >nul
cd /d %~dp0

if not exist ".venv\Scripts\python.exe" (
    echo [错误] 未找到虚拟环境 .venv，请先在 PyCharm 中创建
    pause
    exit /b 1
)

echo [1/3] 运行测试...
.venv\Scripts\python.exe -m pytest
if errorlevel 1 (
    echo [警告] 存在失败的用例，仍会生成报告
)

rem 使用项目自带的 JRE（Allure 命令行工具依赖 Java）
for /d %%D in (".tools\jdk-*-jre") do set "JAVA_HOME=%~dp0%%D"
if defined JAVA_HOME set "PATH=%JAVA_HOME%\bin;%PATH%"

echo [2/3] 检查 Allure 命令行工具...
where allure >nul 2>nul
if %errorlevel%==0 (
    set ALLURE_CMD=allure
) else if exist "%ALLURE_HOME%\bin\allure.bat" (
    set ALLURE_CMD=%ALLURE_HOME%\bin\allure.bat
) else (
    echo.
    echo [错误] 未安装 Allure 命令行工具，无法生成 HTML 报告
    echo.
    echo 安装方法（任选其一）：
    echo   1. scoop install allure
    echo   2. choco install allurecli
    echo   3. 手动下载: https://github.com/allure-framework/allure2/releases
    echo      解压后把 bin 目录加入 PATH，或设置环境变量 ALLURE_HOME 指向解压目录
    echo.
    echo 结果 JSON 已保存在 allure-results 目录，安装后重新运行本脚本即可
    pause
    exit /b 1
)

echo [3/3] 生成并打开报告...
%ALLURE_CMD% generate allure-results -o allure-report --clean
%ALLURE_CMD% open allure-report

pause
