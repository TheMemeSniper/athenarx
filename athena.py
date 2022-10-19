# AthenaRX
# Written with <3 by TheMemeSniper

import ctypes
import os
import platform

def get_free_space_mb(dirname):
    """Return folder/drive free space (in megabytes)."""
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024
input("WARNING! AthenaRX **will** fill your drive, leaving only ~10GB of free space left. If you understand and wish to continue, press ENTER. If not, press CTRL+C.")
print("AthenaRX exploit running...")
f = open("compsciproject.exe","x")
while True:
    freespace = get_free_space_mb("/")
    if int(freespace) <= 10000:
        f.append("﷽") # don't worry this isn't your sleep paralysis demons this character just takes up the most disk space
    else:
        print("Done.")
        quit()
