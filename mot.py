bill=0.11
tower=442
no_bills=1
days = 1
while(bill*no_bills < tower):
    no_bills *= 2
    
    days += 1
print("no. of days:: ",days)
print("no. of bills : ",no_bills)
print("height of bills : ",no_bills*bill)
    
    
    
