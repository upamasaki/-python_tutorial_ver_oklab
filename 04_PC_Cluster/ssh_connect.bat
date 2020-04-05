@echo off
 
for /f "tokens=1-4 delims=," %%a in (datasets/pc_slave_list.txt) do (
  echo %%a %%b %%c
  start ssh %%b@%%a
  start %%d
)
