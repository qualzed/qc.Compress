import os
import time
from modules.byte import Byte
from modules.debyte import deByte

menu = """
> Compress file [1]
> Deompress file [2]
> Exit [3]
"""

def qc():
    while True:
        os.system("cls")
        print(menu)
        setting = int(input(">> "))
        match setting:
            case 1:
                os.system("cls")
                setting = input("Path to file >> ")
                try:
                    Byte(setting)
                except Exception as e:
                    print("An error {e}")
            case 2:
                os.system("cls")
                setting = input("Path to .qc file >> ")
                try:
                    deByte(setting)
                except Exception as e:
                    print(f"An error {e}")
            case 3:
                os.system("cls")
                print("Goodbye")
                time.sleep(3)
                exit(0)

if __name__ == '__main__':
    qc()