import requests
import time

while(1):
    x = requests.post("http://ganesh.icmc.usp.br/mitm.php", {"flag_input":r"Ganesh{Hello_World}"})
    print(x.status_code)
    time.sleep(120)
