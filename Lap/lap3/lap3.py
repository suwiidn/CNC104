inputstrr  = " proDuct: wireless Mouse | price: 259.9 | qty: 3 "


product = inputstrr.split("|")[0].split(':')[1].strip().lower()
price = inputstrr.split("|")[1].split(':')[1].strip().lower()
qty = inputstrr.split("|")[2].split(':')[1].strip().lower()
total = price + qty



print("Product:" ,product.split())
print("Price:",price + " THB")
print("Qty:",qty + " THB")
print("Total:", total)