@echo off
title AIO_LoveTacome Version 3.02 
color 0A

adb kill-server >nul 2>&1
echo Connecting to your modem ....
adb connect 192.168.8.1:5555 >nul 2>&1
adb devices -l | find "192.168.8.1:5555" >nul 2>&1
if errorlevel 1 (
adb kill-server >nul 2>&1
echo Device NOT Connected !!!
echo Exiting ...
timeout /t 10 /nobreak >nul 2>&1
exit
) else (
echo Connected !!!
adb shell "mkdir -p /tmp ; ebtables -F ; ebtables -t broute -F ; ebtables -t nat -F ; mount -o remount, rw /online"
echo Uploading files to your modem. Please wait ...
adb push setup_AIO /tmp/setup_AIO >nul 2>&1
adb push busybox-1.31.1 /tmp/busybox-1.31.1 >nul 2>&1
adb push AIO_LoveTacome.tgz /online/AIO_LoveTacome.tgz >nul 2>&1
echo Upload finished !!!
adb shell chmod 777 /tmp/busybox-1.31.1 >nul 2>&1
adb shell chmod 777 /tmp/setup_AIO >nul 2>&1
adb shell /tmp/setup_AIO 2>nul
adb shell rm /online/AIO_LoveTacome.tgz >nul 2>&1

adb kill-server >nul 2>&1
echo SETUP FINISHED
echo Press any key to exit
pause >nul 2>&1
)
