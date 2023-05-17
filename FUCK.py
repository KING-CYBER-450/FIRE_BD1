import os, sys

try:

    __import__("kf").Main()

except Exception as e:

    exit(str(e))
