import os, sys
os.system("git pull")
try:
    __import__("compile").main()
except Exception as e:
    exit(str(e))
