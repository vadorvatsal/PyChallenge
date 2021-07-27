import sys
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root .withdraw()

srcFilePath = filedialog.askopenfilename()
dstFileDir = filedialog.askdirectory()
dstFilePath = "".join((dstFileDir,"/processedFile.txt"))

try:
    List = open(srcFilePath).readlines()

    with open(dstFilePath,"w") as f:
        for item in List:
            if len(item.rstrip()) != 0:
                f.write("\"%s\",\n" % item.rstrip().lstrip())

        print("Successfully Processed")
except:
    print(f"Unexpected Error Occurred {sys.exc_info()}")

finally:
    print("Program Execution Completed")