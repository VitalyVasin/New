import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)

with open('Lesson 001/Aleksey/A_os_info.txt', 'w') as ff:
    ff.write(info)