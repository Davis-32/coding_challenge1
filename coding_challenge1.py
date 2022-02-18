# ask for miles per gallon, as float to accept decimal
mpg = float(input("Enter miles per gallon: "))

# declare kpl, convert to str to concatenate later
kpl = str(mpg * 1.609344 * 0.2641720524)

# print kpl
print("Kilometers per gallon: " + kpl)


