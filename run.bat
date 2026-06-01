@REM if $($(Get-Command deactivate -ErrorAction SilentlyContinue).CommandType -eq "Function") {
@REM     echo "Hello"
@REM }
@echo off

FOR /F "usebackq delims=" %%A IN (`python -c "import sys; print(sys.prefix)"`) DO (
    set "prefix=%%A"
)

FOR /F "usebackq delims=" %%A IN (`python -c "import sys; print(sys.base_prefix)"`) DO (
    set "base_prefix=%%A"
)

set "venvstr=venv"

@REM set AHHHHH=/f python -c "exec(\"import sys\nprint(sys.prefix)\")"
if NOT "%base_prefix%"=="%prefix%" (
    if NOT "%prefix:%venvstr%=%" == "%prefix%" (
        echo We are in the VENV
        pip install -e .
        python -m overwatch_hero_stats
    ) else (
        echo We might not be in the venv so quitting -  not named .venv or venv
    )
) else (
    echo We are definitley not in the VENV
)



