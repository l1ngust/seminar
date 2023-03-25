p1 = int(input())
p2 = int(input())
p3 = int(input())

if ((p1 < p2) and (p1 < p3)) and (p2 < p3):
    print("К сумме:", (p1+p2+p3)/2)

elif ((p3 < p2) and (p3 < p1)) and (p2 < p1):
    print("К сумме:", (p1+p2+p3)/3)

else:
    print("К сумме:", (p1+p2+p3))