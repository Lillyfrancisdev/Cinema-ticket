import datetime

# menu
adults = 20
children = 10
students = 10
seniors = 12
#print the menu
print(f'''\nWelcome to Cineworld Greenwich!\nCHECK THE PRICE LIST PLEASE:\nAdult:£{adults}\nChild:£{children}\nStudent:£{students}\nSenior:£{seniors}\n \nNote:\nValid student card with photo ID REQUIRED.\nProof of senior status REQUIRED.\n''')
#The try and except block will test the block of code.
while True:
    try:
        ticketadult = int(input("How many Adult ticket required: "))
    except ValueError:
        print("You Must Enter a Valid Number: ")
    else:
        break
while True:
    try:
        ticketchild = int(input("How many Child ticket required: "))
    except ValueError:
        print("You Must Enter a Valid Number required: ")
    else:
        break
while True:
    try:
        ticketstudent = int(input("How many Student ticket required: "))
    except ValueError:
        print("You Must Enter a Valid Number: ")
    else:
        break
while True:
    try:
        ticketsenior = int(input("How many Senior ticket required: "))
    except ValueError:
        print("You Must Enter a Valid Number: ")
    else:
        break
#import datetime
MovieTime = datetime.datetime.today().strftime("%d %B %Y %H:%M %p")
Date = datetime.datetime.today().strftime("%d/%m/%Y ")
Time = datetime.datetime.today().strftime("%A %H:%M ")

total = ((ticketadult * adults) + (ticketchild * children) + (ticketstudent * students) + (ticketsenior * seniors))
#The total_cost function will calculate the input values entered by the user.
def total_Cost():
    global Name
    Name = input('\nPlease enter your name: ')
    print(f'''\n    Number of Adult Ticket:{ticketadult}*{adults} = {ticketadult * adults}
    Number of Child Ticket:{ticketchild}*{children} = {ticketchild * children}
    Number of Student Ticket:{ticketstudent}*{students} = {ticketstudent * students}
    Number of Senior Ticket:{ticketsenior}*{seniors} = {ticketsenior * seniors} 
    Total = £{total}\n''')
#The payment function will take the user input option by the users and calculate the returnAmount.
def payment():
    global paid
    paid = 0
    global returnAmount
    print('Payment:')
    print('''[1]card \n[2]cash ''')
    option = int(input('What is your payment option:'))
    if option == 1:
        paid += total
        print(f'Total £{total}.Payment accepted.')
        returnAmount = paid - total
    else:
        print("Machine Only accept £5,£10,£20\n")
    while paid < total:
        while True:
            try:
                notes = int(input("Enter The Notes: "))
            except ValueError:
                print(f"{notes} is not a Valid Notes: ")
            else:
                break
        if notes == 5:
            paid = paid + 5
        elif notes == 10:
            paid = paid + 10
        elif notes == 20:
            paid = paid + 20
        else:
            print("Machine Only accept £5,£10,£20 \n")
    if paid > total:
     returnAmount = paid - total
    else:
     returnAmount = 0
#The  receipt function will print the receipt.
def receipt():
    payment()
    print(f"\nRECEIPT:\nLead Booker: {Name} \nTotal Cost = {total}\nTotal Paid = {paid}\nYour Remaining change is = {returnAmount} \nDate: {Date}\nTime:{Time}\n")
    print("Thank you. Enjoy the Movie!")

if total <= 0:
    print("Thank you for enquiry")
elif total > 0:
    total_Cost()
    receipt()
