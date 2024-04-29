import sys
import time
import pyfiglet
from colorama import init
from pyfiglet import figlet_format
from termcolor import colored

def print_slow_1(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.04)
    
list = ['1', '2', '3', '4', '5']

# Greeting in Font
init(autoreset=False, convert=None, strip=None, wrap=True)
print((colored(figlet_format("Welcome to my Haunted Escape room!"), color = 'red')))


def last():
  
  
    print(list)
    opt = input("")
  
    if opt == '1':
      print("\nYou open the door slowly.. it leads to plummiting dark hole. thats definiatly the wrong door\n ")
      print("You Lose.")
      list.remove('1')
    
      
    elif opt == '2':
      print("\nThis door is sealed shut and cant even be opened.\n ")
      print("You Lose.")
      list.remove('2')
   

    elif opt == '3':
      print_slow_1("When opening the door you feel a strong gust of wind on yor face and you hear the house shake...")
      print_slow_1("\nCongradulations you have completed the escape room!!")

    elif opt == '4':
      print("\nYou open the door and find the bones and remains of a human being that had been traped. The skull stares down into your soul.. ")
      print("\nthis is not the correct door..")
      print("You Lose.")
      list.remove('4')
      
    elif opt == '5':
      print("\n This door contained nothing except some old clothes?! it might be some old colset.")
      print("Whats that doing there??? You lose.")
      list.remove('5')
     
      
# introduction text
def begin():
  print_slow_1("\nThis is your escape room.")
  print_slow_1("\n\nyou must solve 3 puzzles to exit the game, until then you cannot exit the game no matter what the consequences will end in DEATH.")
  print_slow_1("\nYou open the door to the manshion belived to hold spirits that have haunted the house for years...\n")

begin()




# Start of pathway 1
door = input("As you enter you are given two options, take the stairs or follow a dark hallway, which one do you take? S or H: ")
door = door.upper()

# S Pathway
if door == "S":
  print_slow_1("\nAs you slowly make your way up the stairs you hear whispers coming from all around, the surrounding air around you feels as cold as ice and the oxegen feels low as if your gasping for air.\n ")
  print_slow_1("\nwhen you calm your nerves you see one dimly lit light next to a note that reads... \nyou have made it to stage 1, you must find the key to the next floor in order to move further into the escape room...\n")



  # stage 1
  dres = input("You find a dresser do you want search it? ")
  dres.upper()
  
  if dres == "YES":
    
    print_slow_1("\n\nyou search the dresser and find a strange key maybe it can be used to open the door...\n\n")
  elif dres == "NO":
    
    print_slow_1("\nThere isnt much to look for the dresser seems like your only option.")
    print_slow_1("\nYou find a key in the dresser, that you were to reluctant to look in...\n")


  #stage 2
  print_slow_1("As you open the door you are met with another note next to a lit candle.. it reads, You must solve the puzzle and find the correct password or else celing will crush you...\n ")

  print_slow_1("You need to find the hidden password in this room. If the password is wrong you will be crushed.\n")

  password = input("There are 4 pices of funiture do you wish to inspect them? ")
  password.upper()
  
  if password == "yes":
    
    print("\nunder the table you find the letter C written in inc.")
    print("\nyou also find the letter O inside the sofa\n")
    print("And you found a paper with the letter D on the back of the door you came out of.\n")
    print("And finally you looked above you and on the celineg wrote the letter E.")

    print("\nWhat is the password? ")
    stage2 = input("")
    stage2 = stage2.upper()

    if stage2 == "CODE":
      print("\n\nCorrect you move on to the next stage")

      print("This is the third and final stage. suprised you made it this far." )
      print("in the next room there is a note with 5 doors.")
      print("You must select the correct door to 3scape.")
      
      last()

    elif stage2 != "CODE":
      print("Incorrect, the ceailing starts closing down lower and lower....")
      print("You have been crushed.")
      

  elif password == "no":
    
    print("well you dont have much else to do unless you want to be crushed..")
    password = input("do you want to inspect the furniture? ")

    if password == "yes":
    
      print("\nunder the table you find the letter C written in inc.")
      print("\nyou also find the letter O inside the sofa\n")
      print("And you found a paper with the letter D on the back of the door you came out of.\n")
      print("And finally you looked above you and on the celineg wrote the letter E.")

    print("\nWhat is the password? ")
    stage2 = input("")
    stage2 = stage2.upper()

    if stage2 == "CODE":
      print("\n\nCorrect you move on to the next stage")

      print("This is the third and final stage. suprised you made it this far." )
      print("in the next room there is a note with 5 doors.")
      print("You must select the correct door to 3scape.")
      #stage 3
      last()

    elif stage2 != "CODE":
      print("Incorrect, the ceailing starts closing down lower and lower....")
      print("You have been crushed.")

# H pathway
elif door == "H":
  print_slow_1("\nAs you slowly make your way down the dark hallway you hear whispers coming from all around, the surrounding air around you feels as cold as ice and the oxegen feels low as if your gasping for air.\n ")
  print_slow_1("\nwhen you calm your nerves you see one dimly lit light next to a note that reads... \nyou have made it to stage 1, you must find the key to the next floor in order to move further into the escape room...\n")



  
  dres = input("You find a dresser do you want search it? ")
  if dres == "yes":
    dres.upper()
    print("\nyou search the dresser and find a strange key maybe it can be used to open the door...\n")
  elif dres == "no":
    dres.upper()
    print("\nThere isnt much to look for the dresser seems like your only option.")
    print("\nYou find a key in the dresser, that you were to reluctant to look in...\n")

  print("As you open the door you are met with another note next to a lit candle.. it reads, You must solve the puzzle and find the correct password or else celing will crush you if you dont move fast enough...\n ")

  print("You need to find the hidden password in this room. If the password is wrong you will be crushed.\n")

  password = input("There are 4 pices of furniture do you wish to inspect them? ")
  
  if password == "yes":
    password.upper()
    print("\nunder the table you find the letter C written in inc.\n")
    print("\nyou also find the letter O inside the sofa\n")
    print("\nAnd you found a paper with the letter M on the back of the door you came out of.\n")
    print("And finally you looked above you and on the celineg wrote the letter P.")

    print("\nWhat is the password? ")

  elif password != "yes":
    print("well you dont have much else to do unless you want to be crushed..")
    password = input("do you want to inspect the furniture? ")

  if password == "yes":
    password.upper()
    print("\nunder the table you find the letter C written in inc.\n")
    print("you also find the letter O inside the sofa\n")
    print("And you found a paper with the letter M on the back of the door you came out of.\n")
    print("And finally you looked above you and on the celineg wrote the letter P.")

    print("\nWhat is the password? ")
    
    stage2 = input("")
    stage2 = stage2.upper()

    if stage2 == "COMP":
      print_slow_1("Correct you move on to the next stage")

      print_slow_1("This is the third and final stage. suprised you made it this far." )
      print_slow_1("in the next room there is a note with 5 doors.")
      print_slow_1("You must select the correct door to escape.")
      
      last()

    elif stage2 != "COMP":
      print_slow_1("Incorrect, the ceailing starts closing down lower and lower....")
      print_slow_1("You have been crushed.")
      