import time
from modules.sizeof.size import replacements
from modules.type import *

def Byte(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            adat = len(data)

        for old_bytes, new_bytes in replacements:
            if new_bytes in data:
                data = data + b"$\xCC\xC8$"

            data = data.replace(old_bytes, new_bytes)

        try:
            with open(file_path + ".qc", 'wb') as f:
                f.write(data)

            print(cbSucces+"File was compressed")
            time.sleep(3)

        except Exception as e:
            print(cbError+f"An error while compress: {e}")

    except FileNotFoundError:
        print(cbError+f"| Error! {file_path} not found.")