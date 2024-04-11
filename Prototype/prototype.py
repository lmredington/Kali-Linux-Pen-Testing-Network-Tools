'''
Requirement of Installed tools:
    * git
    * nmap
    * netdiscover
    * wapiti
    * nikto
'''

import xml.etree.ElementTree as ET
import csv
import subprocess
import html
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, Border, Side
import json
import re
import os
import pandas as pd

def run_command(command):
    print("Running ", command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        # Command was successful
        print("Output:", output.decode())
        print("Command executed successfully\n")
        
    else:
        # Command failed
        print("Error output:", error.decode())
        print(f"Error executing command. Return code: {return_code}")
        
    return return_code, output.decode()

network_command = "arp -a"
#network_command = "sudo netdiscover -i eth0"
print("\nFinding Interface Options ...")
run_command(network_command)

print("\n ---------------------------------------------------- \n")

host_discover_command = "nmap -sn 150.201.194.0/22"

run_command(host_discover_command)

print("\n ---------------------------------------------------- \n")

nslookup_command = "nslookup semo.edu"

run_command(nslookup_command)

print("\n ---------------------------------------------------- \n")

nikto_command = "nikto -h 150.201.192.22"

run_command(nikto_command)

print("\n ---------------------------------------------------- \n")

nmap_command = "nmap 150.201.192.22"

run_command(nmap_command)

print("\n ---------------------------------------------------- \n")

wapiti_command = "wapiti -u http://150.201.194.22"

run_command(wapiti_command)

print("\n ---------------------------------------------------- \n")
