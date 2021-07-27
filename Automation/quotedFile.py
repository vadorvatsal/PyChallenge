import sys,os,time
import tkinter as tk
from tkinter import filedialog
try:
    if sys.version_info[0]<3:
        raise Exception
except:
    print("Not python version 3")
    time.sleep(2)

root = tk.Tk()
root .withdraw()

os.system('cls' if os.name == 'nt' else 'clear')
print("Select source file")
srcFilePath = filedialog.askopenfilename()
print("Select destination directory")
dstFileDir = filedialog.askdirectory()
dstFilePath = "".join((dstFileDir,"/processedFile.txt"))

try:
    List = open(srcFilePath).readlines()

    with open(dstFilePath,"w") as f:
        for item in List:
            if len(item.rstrip()) != 0:
                f.write("\"%s\",\n" % item.rstrip().lstrip())

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Successfully Processed {} in {}".format(srcFilePath,dstFilePath))
        time.sleep(2)
except:
    print(sys.exc_info())

finally:
    print("Program Execution Completed")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')