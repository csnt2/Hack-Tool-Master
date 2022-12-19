import sys
import logging
import requests
import subprocess

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s',
                    filename='HTM.log', filemode='a+', datefmt='%d/%m/%Y %H:%M:%S')

v = open("version", "r")
my_version = v.read()

def start():
    try:
        if requests.get('https://raw.githubusercontent.com/Aleks746/Database-HTM-test-/main/version').text>my_version:
            logging.info(f'Found a new version of the code')
            code = requests.get("https://raw.githubusercontent.com/Aleks746/Database-HTM-test-/main/htm_code").text
            logging.info(f'Loading..')
            c = open("code.py", "w+", encoding="utf-8")
            c.write(code)
            c.close
            version = requests.get('https://raw.githubusercontent.com/Aleks746/Database-HTM-test-/main/version').text
            v1 = open("version", "w+")
            v1.write(version)
            v1.close
            print("Готово")
            logging.info(f'Updated version to {version}')
            code_2 = subprocess.Popen([sys.executable,"code.py"])
            code_2.wait()
        else:
            code_2 = subprocess.Popen([sys.executable,"code.py"])
            code_2.wait()
    except Exception as l:
        print("Ошибка")
        logging.error(f'{l} | Contact support on our discord server: https://discord.gg/sMEucQEaY7')
start()