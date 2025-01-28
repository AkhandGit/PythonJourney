weight=int(input("Enter the weight: "))
units=input("Killogram or Pounds (K or L): ")

if units=="K":
    weight=weight*2.205
    units="Lbs"
elif units=="L":
    weight=weight/2.205
    units="Kgs"
else:
    print(f"{units} is not valid!")
print(f"Your weight is:{weight:.2f} {units}")