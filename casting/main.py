# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
leek_string = "Leek is " + str(leek_price) + " euro per kilo."
print(leek_string)
leek_order = "4 leeks"
leek_order_amount = int(leek_order[:leek_order.find(" leeks")])
leek_sum_total = leek_price * leek_order_amount
print(leek_sum_total)

broccoli_price = 2.34
broccoli_order = "broccoli 1.6"
broccoli_order_amount = float(broccoli_order[broccoli_order.find("1.6"):])
broccoli_sum_total = broccoli_price * broccoli_order_amount
broccoli_string = broccoli_order_amount + "kg broccoli costs " + str(round(broccoli_sum_total, 2)) + "e" 
print(broccoli_string)