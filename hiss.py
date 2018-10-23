import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    with open('packs.snek') as f:
        packages = f.readlines()
        packages = [p.strip() for p in packages]
        for pck in packages:
            if pck[0] != '#':
                install(pck)
except Exception as e:
    print('packs.snek file not found!')
