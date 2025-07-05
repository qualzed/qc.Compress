import time
from modules.sizeof.size import replacements
from modules.type import *

def deByte(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        for old_bytes, new_bytes in reversed(replacements):
            if(new_bytes + b"$\xCC\xC8$" in data):
                data = data.replace(new_bytes + b"$\xCC\xC8$", new_bytes)
            else:
                data = data.replace(new_bytes, old_bytes)

        output_file = file_path.replace(".qc", "")

        with open(output_file, 'wb') as f:
            f.write(data)
            print(cbSucces+"File was decompressed")
            time.sleep(3)

    except FileNotFoundError:
        print(cbError+f"| Error! '{file_path}' not found.")
        time.sleep(3)
    except Exception as e:
        print(cbError+f"| An error {e}")
        time.sleep(3)