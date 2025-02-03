principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("Enter the principle amount: "))
    if principle<=0:
        print("The principle amount should be greater than zero")


while rate<=0:
    rate=float(input("Enter the interest rate: "))
    if rate<=0:
        print("The interest rate should be greater than zero")

        
while time<=0:
    time=float(input("Enter the time period: "))
    if time<=0:
        print("The time period should be greater than zero")

total=principle*pow((1+rate/100),time)
compoundinterest=total-principle 
print("The compound interest is: ", compoundinterest)