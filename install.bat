@echo off
echo "script for install python and yt-dlp, have fun ^_^"

set PATH=%PATH%;%LOCALAPPDATA%\Microsoft\WindowsApps

winget install Python.Python.3.14
winget install yt-dlp.yt-dlp

del ./install.bat && del ./install.sh

echo yt-dlp and python installed *_*