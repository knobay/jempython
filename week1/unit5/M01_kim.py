#Ask the user for their full name and return it with initials added in round brackets.
userName=input("Enter full name")
#find out where the space is
pos=userName.index(' ')
print(userName+ " ("+ userName[0]+ userName[pos+1]+ ")")

