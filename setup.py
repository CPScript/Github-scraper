import os
import time
from os import system

# ugly asf
print("installing:")
print("""* requests
* beautifulsoup4
In 5 seconds...
ctrl+C to stop
""")
time.sleep(6)
os.system('pip install -r requeirments.txt -y')
print("""
Done, type `python main.py` to execute the script
""")
