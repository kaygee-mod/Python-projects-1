#professional email generator

first = input("Please enter first name ").strip()#asks for input and also uses strip method to remove any spaces
second = input("Please enter your surname ").strip()

username = f"{first[0]}{second}"#creating the username using string manipulation

print(f"Your email is: {username.lower()} @university.co.za")#printing the email