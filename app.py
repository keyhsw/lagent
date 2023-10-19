import os
from subprocess import Popen, PIPE, STDOUT

def exe_shell(command: str, shell: str = '/bin/bash'):
    return Popen(command, stdout=PIPE, stderr=STDOUT, shell=True, executable=shell)

exe_shell('streamlit run examples/react_web_demo.py --server.port 7860')
# os.system('streamlit run examples/react_web_demo.py --server.port 7860')
