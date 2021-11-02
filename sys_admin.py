"""
    Author: Lori White
    Purpose: Showing how to use os.system() and subprocess.run() in python.
"""
import platform
osystem = platform.system()
print(f"My OS is: {osystem}")
command = ""
commandArguement = ""
# Using os.system
import os
if osystem == "Windows":
    os.system("dir")
else:
    os.system("ls")
# Using subprocess.run
import subprocess
if osystem == "Windows":
    subprocess.run(["powershell.exe","dir"])
else:
    subprocess.run(["ls"])
# Using subprocess.run with One Argument
if osystem == "Windows":
    subprocess.run(["powershell.exe","dir","-r"])
else:
    subprocess.run(["ls","-l"])
# Using subprocess.run with Two Arguments
if osystem == "Windows":
    subprocess.run(["powershell.exe","dir","|","fw"])
else:
    subprocess.run(["ls","-l","Data_Files"])
# Retrieving System Information
if osystem == "Windows":
    command = "systeminfo"
    print(f'Gathering system information with command: {command}')
    subprocess.run([command])
else:
    command = "uname"
    commandArguement = "-a"
    print(f'Gathering system information with command: {command} {commandArguement}')
    subprocess.run([command, commandArguement])
# Retrieving Diskspace Information
if osystem == "Windows":
    command = "systeminfo"
    print(f'Gathering diskspace information with command: {command}')
    subprocess.run([command])
else:
    command="df"
    commandArguement="-l"
    print(f'Gathering diskspace information with command: {command} {commandArguement}')
    subprocess.run([command,commandArguement])
# Retrieving Actice Process Information
if osystem == "Windows":
    command = "tasklist"
    print(f'Gathering active process information with command: {command}')
    subprocess.run([command])
else:
    command="ps"
    commandArguement="-x"
    print(f'Gathering active process information with command: {command} {commandArguement}')
    subprocess.run([command,commandArguement])
