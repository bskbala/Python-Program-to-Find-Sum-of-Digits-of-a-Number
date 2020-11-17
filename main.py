# Python Program to Find Sum of Digits of a Number 3

Number = int (input("Please Enter any Digits :"))
sum =0
while(Number >0):
    rem =Number%10
    sum =sum+rem
    Number = Number //10
print("\n sum of the Digits of given  Number =%d"%sum)