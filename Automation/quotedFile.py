import sys,os,time
import tkinter as tk
from tkinter import filedialog
try:
    if sys.version_info[0]<3:
        raise Exception
except:
    print("Warning you are not using python version 3")
    time.sleep(2)

root = tk.Tk()
root .withdraw()

os.system('cls' if os.name == 'nt' else 'clear')
print("Select source file")
srcFilePath = filedialog.askopenfilename()
os.system('cls' if os.name == 'nt' else 'clear')
print("Selected file : {}".format(srcFilePath.split("/")[-1]))
print("Select destination directory")
dstFileDir = filedialog.askdirectory()
os.system('cls' if os.name == 'nt' else 'clear')
print("Selected file : {}".format(srcFilePath.split("/")[-1]))
print("Selected directory : {}".format(dstFileDir.split("/")[-1]))
dstFilePath = "".join((dstFileDir,"/processedFile.txt"))
time.sleep(3)

try:
    List = open(srcFilePath).readlines()

    with open(dstFilePath,"w") as f:
        for item in List:
            if len(item.rstrip()) != 0:
                f.write("\"%s\",\n" % item.rstrip().lstrip())

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Successfully Processed at : {}".format(dstFilePath))
        time.sleep(2)
except:
    print("Unexpected error {} occurred.".format(sys.exc_info()))

finally:
    print("Program Execution Completed")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')