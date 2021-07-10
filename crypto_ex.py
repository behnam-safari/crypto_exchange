
'''you should get new free api from :  https://docs.coinapi.io/?python#trades
because you can use this api for a day'''

import requests
from tkinter import *
from os import getcwd
#-------------------------***front of project***-----------------------------------------------
win = Tk()
win['bg']='white'
win.title('exchange ecrypto to IRR')
lst = []
lst2 = []
#---------------------------***get api***-----------------------------------------------------
def coin():
#url for get coin price
    url = f'https://rest.coinapi.io/v1/assets?filter_asset_id={entry.get()}'

    headers = {'X-CoinAPI-Key' : '53EBD096-B5B8-4274-9738-29991E5D2E03'}

    res= requests.get(url, headers=headers) 

#url2 for exchnge usd to irr

    url2 = 'https://raters.ir/exchange/api/currency/usd'
    res2 = requests.get(url2)

    res_crypto = res.json()
    res_dollar = res2.json()['data']['prices']

    for j in res_dollar:
        price=j['live']
        dollar_price = int(''.join(price.split(',')))
        
    for i in res_crypto:
        lst.append(f"name coin: {i['name']}\n price of coin :{i['price_usd']*dollar_price:,.0f} IRR\n") 

        label.config(text=''.join(lst))

#-----------------------------------***tkinter part***-----------------------------------------------------------------
win.geometry('400x198')
img = PhotoImage(file = getcwd() + '/img'+'/2.png')
lbl = Label(win,image = img,bg='white').place(x=-7,y=-7)

entry = Entry(win,bg ='#100b5e',fg ='white',highlightcolor='#100b5e',font='tahoma 10')
entry.place(x=75,y=35,height=32)

button = Button(win,text='show',borderwidth=0,bg='#272284',activebackground='#272281',highlightbackground='#272281',activeforeground='white',command=coin)
button.place(x=5,y = 35)

label = Label(win,text='',bg ='#322d7e',fg = 'white',highlightcolor='#322d7e',font = 'dyuthi 11 bold')
label.place(x = 5 , y = 100)


win.mainloop()