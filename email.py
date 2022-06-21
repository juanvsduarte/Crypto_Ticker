from asyncore import read
from tkinter import X
from readcrypto import btc , eth



from IPython.display import display
import pandas as pd
import win32com.client as win32



# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)

# configurar as informações do seu e-mail
email.To = "juansduarte02@gmail.com"
email.Subject = "Preço das Criptomoedas"
email.HTMLBody = f"""

<p>Segue o valor das principais criptomoedas</p>

<p>{btc}</p>
<p>{eth}</p>

<p>Abs,</p>
<p>Crypto Ticker</p>

"""

email.Send()
print("Email Enviado")
