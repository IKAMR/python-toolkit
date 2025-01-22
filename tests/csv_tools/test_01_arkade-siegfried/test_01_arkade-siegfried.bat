@echo off

REM Choose wanted Parameter variables
REM If not used leave blank or ""

REM Python Script
REM set _python=C:\git\debug\python-toolkit\tests\csv_tools\csv_splitter.py
set _python=C:\git\debug\python-toolkit\code\csv_tools\csv_splitter.py

REM Source Folder and File

REM set _source_folder=C:\git\debug\python-toolkit\tests\csv_tools\test_01_arkade-siegfried\source
set _source_folder=C:\git\debug\python-toolkit\tests\csv_tools\test_01_arkade-siegfried\source

REM set _source_file=test_01_filformatinfo.csv
set _source_file=test_01_filformatinfo.csv

REM Target Folder
REM set _target_folder=C:\git\debug\python-toolkit_bk\tests\csv_tools\test_01_arkade-siegfried\target
set _target_folder=C:\git\debug\python-toolkit_bk\tests\csv_tools\test_01_arkade-siegfried\target

REM Rows
REM set _rows=1000
REM set _rows=100000
set _rows=--rows 30

REM Feil Extension
REM set _ext=0		First row
REM set _ext=1		Second row, etc
set _ext=--ext 1

REM Size
REM set _size="size 600"
REM set _size="size 250kB"
REM set _size="size 100MB"
REM set _size="size 1GB"
set _size=

REM Log
REM set _log=C:\git\debug\python-toolkit\tests\csv_tools\test_01_arkade-siegfried\log
set _log=

python %_python% %_source_folder%\%_source_file% %_target_folder% %_rows% %_size% %_ext% %_log%

@echo on
