.............mport os
from datetime import datetime  

os.system("cls")
print(datetime.now())
hora = datetime.now().hour

if hora < 12:
    mensagem = "bom dia☀️"
    print(mensagem)
elif hora < 18:
    mensagem = "boa tarde☀️"

else:
    mensagem = "boa noite🌙"
    print(mensagem)
os.system(f"start cmd /k echo {mensagem}")
