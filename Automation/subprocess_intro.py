import subprocess
import time

for i in range(3):
    subprocess.check_call(['python', 'hello_python.py'])
    print("................")
    time.sleep(2)

# challenge is figure out how to clear screen for this script after subprocess call
