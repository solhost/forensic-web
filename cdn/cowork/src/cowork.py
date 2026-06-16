import sys
import subprocess
from colorama import Fore
import shutil

file = sys.argv[1]

with open(file) as f:
    code = f.read()

class Cowork:
    def __init__(self):
        self.mode = ""
    def evaluate(self, obj):
        if obj == "[pypi]":
            self.mode = "pip"
        elif obj == "[npm]":
            self.mode = "npm"
        else:
            if self.mode == "pip":
                where_pip = shutil.which("pip")
                print(Fore.LIGHTYELLOW_EX + "Forensic Cowork: Installing " + obj + " from PyPI" + Fore.WHITE)
                subprocess.run([where_pip, "install", obj])
            elif self.mode == "npm":
                where_npm = shutil.which("npm")
                print(Fore.LIGHTYELLOW_EX + "Forensic Cowork: Installing " + obj + " from npm" + Fore.WHITE)
                subprocess.run([where_npm, "install", obj])
            else:
                print(Fore.RED + "Forensic Cowork: undefined" + Fore.WHITE)

code = code.strip().split("\n")
cowork = Cowork()
for line in code:
    cowork.evaluate(line.strip().lower())
