import sys

sys.tracebacklimit = 0

try:
    fileinput = sys.argv[1]
except IndexError:
    fileinput = None
    print("Usage: py see.py <filename>")
    exit()

numlines = len(open(fileinput).readlines(  ))

if numlines >= 5000:
    print("This file exceeds the maximum limit of 5000 lines.")
else:
    with open(fileinput,'r',encoding='utf8') as f:
        print("[ ",fileinput," ]")
        lines = f.read()
        print(lines)
