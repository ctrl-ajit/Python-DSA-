#program to convert from celcius to fehrenheit and vice versa.
temp = float(input("Enter the tempreature :"))
unit = input("Enter unit of input tempreature , for celcius enter 'C' and 'F' for fahrenheit ")
if unit == "C":
    result = round((9*temp) / 5+32 ,2)
    print("The tempreature in fahrenheit is :",result)
elif unit == "F":
    result = round((temp-32)*5/9,2)
    print(" The tempreature in celsius is :",result)
else :
    print ("You have entered wrong tempreature unit.")




