import sys

f = open("secrets.py","w+")

f.write("server     =   \"<IP Address of Server>\"\n")
f.write("auth       =   \"<Basic Auth Key>\"")
f.close()
