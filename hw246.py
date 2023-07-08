from tkinter import *
from web3 import Web3

root = Tk()
root.title("My Ethereum App")
root.geometry("600x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum gas fee in other currencies", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)

value_in_ether = Label(root, bg="white", font=("bold", 14))
value_in_ether.place(relx=0.5, rely=0.28, anchor=CENTER)

value_in_dollar = Label(root, bg="white", font=("bold", 10))
value_in_dollar.place(relx=0.5, rely=0.48, anchor=CENTER)

value_in_rupees = Label(root, bg="white", font=("bold", 10))
value_in_rupees.place(relx=0.5, rely=0.58, anchor=CENTER)

value_in_pounds = Label(root, bg="white", font=("bold", 10))
value_in_pounds.place(relx=0.5, rely=0.68, anchor=CENTER)

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

# Task 1: Get the current gas price
def ethereum_block():
    wei_price = web3.eth.gas_price
    gwei_price = wei_price/(10**9)
    gas_price_ether = (gwei_price/10**9)
    gas_price_dollar = gas_price_ether * 3000  # Assuming the conversion rate is 1 ETH = 3000 USD
    gas_price_rupees = gas_price_ether * 225000  # Assuming the conversion rate is 1 ETH = 225,000 INR
    gas_price_pounds = gas_price_ether * 2500  # Assuming the conversion rate is 1 ETH = 2500 GBP

    value_in_ether.config(text=f"Gas Price: {gas_price_ether} ETH")
    value_in_dollar.config(text=f"Gas Price: {gas_price_dollar} USD")
    value_in_rupees.config(text=f"Gas Price: {gas_price_rupees} INR")
    value_in_pounds.config(text=f"Gas Price: {gas_price_pounds} GBP")

search_btn = Button(root, text="Search currency fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)

root.mainloop()