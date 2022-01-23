import sys
from tkinter.constants import X
import zipfile
import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory
import errno

root = tk.Tk()
root.withdraw()

modpak_dir = askdirectory(title='Select the folder that contains the ModPak.zip')

steam_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\Valheim\\"
#steam_dir = "C:\\temp\\"


os.chdir(modpak_dir)

with zipfile.ZipFile('modpak.zip', 'r') as modpak_zip:
    modpak_zip.extractall('ModPak')


modpak_unzip = os.path.abspath("ModPak\\ModPak\\")


try:
    shutil.copytree(modpak_unzip, steam_dir, dirs_exist_ok=True)
except OSError as err:
 
    # error caused if the source was not a directory
    if err.errno == errno.ENOTDIR:
        shutil.copy2(modpak_unzip, steam_dir)

    else:
        print("Error: % s" % err)

cleanup = os.path.abspath("ModPak")

try:
    print (cleanup)
    shutil.rmtree(cleanup)
except OSError as e:
    print("Error: %s : %s" % (cleanup, e.strerror))
