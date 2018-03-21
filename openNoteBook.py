import os
import glob
import datetime


MainFolder = r"D:\ALPHABETICAL\N\Notepad_Collection"

today_time = datetime.datetime.now()


fileName = "{:d}_{:02d}_{:02d}.txt".format(today_time.year,today_time.month,today_time.day)
monthName = {1: 'JAN', 2: 'FEB', 3: 'MAR',
             4: 'APR', 5: 'MAY', 6: 'JUN',
             7: 'JUL', 8: 'AGU', 9: 'SEP',
             10: 'OCT', 11: 'NOV', 12: 'DEC'}




folderName = os.path.join(MainFolder,monthName[today_time.month])

if not os.path.isdir(folderName):
    os.makedirs(folderName)

fileName= os.path.join(folderName,fileName)

line ="--------------------------------------------\n"
openFile = "DATE OF OPEN " \
           "  {:d}-{:02d}-{:02d}  {:d}-{:02d}-{:02d} \n".format(
    today_time.year, today_time.month, today_time.day,
    today_time.hour, today_time.minute, today_time.second)

remark_msg =input("Any Remark")
remark  = "REMARK : {:s}\n".format(remark_msg)
if os.path.isfile(fileName):
    try :
        fileHandler = open(fileName, 'a')
        fileHandler.write("\n")
        fileHandler.write(line)
        fileHandler.write(openFile)
        fileHandler.write(remark)
        fileHandler.write(line)
        fileHandler.close()

    finally:
        fileHandler.close()
else:
    fileHandler = open(fileName, 'w')
    fileHandler.write(line)
    fileHandler.write(openFile)
    fileHandler.write(remark)
    fileHandler.write(line)
    fileHandler.close()




command_To_Open_File = "notepad++ {:s}".format(fileName)

os.system(command_To_Open_File)



