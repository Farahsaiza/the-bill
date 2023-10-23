tab=[]
tab1=[]
for i in range (3):
    name=(print("enter the customer's first and last name number ",i+1,": "))
    name=str(input())
    tab1.append(name)
    number=int(input("enter the number of items : "))
    bill=0
    for i in range(number):
        price=(print("enter the price of the item ",i+1 ,":"))
        price=float(input())
        VAT=price*15/100
        total=price+VAT
        discount=total-(2/100)
        bill=bill+discount
    tab.append(bill)
print("the bill: ")
for i in range (3):
    print(" the total to be paid for the customer",tab1[i],"is: ",tab[i],"DH")

