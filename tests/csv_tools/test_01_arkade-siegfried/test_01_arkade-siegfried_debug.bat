@echo off

REM Choose wanted Parameter variables
REM If not used leave blank or ""

REM Python Script
REM set _python=C:\git\debug\python-toolkit\tests\csv_tools\csv_splitter.py
set _python=C:\git\debug\python-toolkit\code\csv_tools\csv_splitter_debug.py

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

REM File Extension column the parse
REM set _extcol=--extcol 0		First column
REM set _extcol=--extcol 1		Second column, etc
set _extcol=--extcol 1

REM File Extension list to separate
REM set _extlist=--extlist txt,xml
set _extlist=--extlist bin,txt,xml

REM Size
REM set _size="size 600"
REM set _size="size 250kB"
REM set _size="size 100MB"
REM set _size="size 1GB"
set _size=

REM Log
REM set _log=C:\git\debug\python-toolkit\tests\csv_tools\test_01_arkade-siegfried\log
set _log=

python %_python% %_source_folder%\%_source_file% %_target_folder% %_rows% %_size% %_extcol% %_extlist% %_log%

@echo on
