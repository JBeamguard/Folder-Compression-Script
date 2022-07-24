:: Purpose: This script will compress all folders inside
::               of the current directory.
:: Written by: Jamie Beamguard
:: Last Revision: 7/2/2022

@ECHO OFF

ECHO Compress all folders inside of %cd%
ECHO.

:: Use loop to iterate through and compress each folder into a .7z file
:: /D  = Only act on Directories
:: %%f = Folder in Question
:: (*) = Current Directory
FOR /D %%f in (*) DO (
    ECHO Now zipping %%f
    "C:\Program Files\7-Zip\7z.exe" a "D:\Listen Up Podcast Episodes\%%f.7z" "%%f"
    ECHO.
    ECHO Remove %%f after compressing
    RMDIR /S /Q "D:\Listen Up Podcast Episodes\%%f"
)

ECHO.
ECHO Done!

:: Tell terminal to remain on screen until closed by user
PAUSE