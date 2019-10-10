
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
      "Try your",
      "Own text here",
      "It can be anything",
      "You want it to be"
      ))

#heres some new strange stuff

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApril\nMay\nJun\nJul\nAug"
print("Here are the days:", days)
print ("Here are the months:", months)
print("""
      There's something going on here.
      With the three double-quotes.
      We'll be able to "type" as much as we like.
      Even 4 lines if we want, or 5, or 6.""")
print("")
print('')

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
blackslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\f* Cat food
\f* Fishies
\f* Catnip\n\f* Grass
"""
print(tabby_cat)
print(persian_cat)
print(blackslash_cat)
print(fat_cat)

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight}lbs.")


def zay():
     x = input("Give me a number: ")
     y = input("Give me another number: ")
     z = input("What do you want to do: 'add', 'subtract', 'multiply' or 'divide'\t\n")
     if z == 'add':
           print("You added", int(x) + int(y), "Nice!")
           if int(x) + int(y) > 100:
                 print("Whoa there!")
     elif z == 'subtract':
           print("You subracted", int(x) - int(y), "Nice!")
           if int(x) - int(y) - -100:
                 print("Get low!")
     elif z == 'multiply':
           print("You multiplied", int(x) * int(y), "Nice!")
           if int(x) * int(y) > 1000000:
                 print("This number is huge!")
           else:
                  print("Number is kinda low!")
     elif z == 'divide':
           print("You divided", int(x) / int(y), "Nice!")
           if int(x) / int(y) < .0001:
                 print("What is this?")
     else:
           print("I quit")
           exit()
           
            
#math()


def asd():
      anime = 'anime soul'
      print("What's the best discord server?")
      server = input()
      if server != anime:
            print("wrong")
      else:
            print(f"So you think {server} is the best?")
            zay()
            exit()

asd()

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print(f"So, you're {age} old, {height}, tall and {weight}lbs.")

from sys import argv


#script, first, second, third = argv     #unpacking argv for 4 varibales
#print("The script is called:", script)
#print("The first variable is:", first)
#print("The second variable is:", second)
#print("The third variable is:", third)

#dog, cat = argv                #one or the other unpack with 2 variables needs script for some reason
#print("This is: ", script)
#print("The first is: ", dog)
#print("The second is: ", cat)
#pet = input("What are these animals? ")
#pets = 'pets'
#if pet == pets:
#      print('correct')
#else:
#      print('wrong')


#script, user_name = argv
#do_something = '>>>'
#print(f"Hi {user_name}, I'm the {script}, script.")
#print("I'd like to ask you a few question.")
#print(f"Do you like me {user_name}?")
#likes = input(do_something)
#print(f"Where do you live {user_name}")
#lives = input(do_something)
#print("What kind of computer do you have?")
#computer = input(do_something)
#print(f"Whats you're favorite video game?")
#game = input(do_something)
#print(f"""
 #     Alright, so you said {likes} about liking
 #     me. You live in {lives}. Not sure where
 #     that is. And you have a {computer} computer. Nice
 #     I really like {game} too!""")

#script, filename = argv #defining two variables as argv 
#txt = open(filename) #assigning txt to open something here it is something called file name
#print(f"Here's your file {filename}:") #this is going to print the name of the file its going to read in the next line
#print(txt.read()) #this is reading whats in the file 
#print("Type the filename again:") #type the same filename again
#file_again = input(">") #assigning file_name to user input and putting a ">" for giggles
#txt_again = open(file_again) #assigning txt_again to open your "file_again"
#print(txt_again.read()) #printing whats in your file again



#filename is some file we are working with
#print(f"We're going to erase {filename}.") #^^^^^script is there because we are working with some file^^^ above i didnt know 
#print("If you don't want to do that, hit CRTL-C")
#print("If you dont care, hit RETURN")
#input("?")
#print("Opening file.....")
#target = open(filename, 'w') #so we're gonn use target to doing something and that use it to open some filename with a w not sure if thats write perms or not >>>it is just found out
#print("Truncating the file. Goodbye!")
#target.truncate() #the file we used as an argument when running the script is being emptied, check it
#print("Now Im going to ask you for three lines")
#line1 = input("line 1:") #these next three lines is input for the "new file" same file different contents
#line2 = input("line 2:")
#line3 = input("line 3:")

#print("I'm going to write these to the file.")

#target.write(line1) #target was assigned to open something
#target.write("\n") #the open(filename) above 
#target.write(line2) #here we're also gonna use write to write to the file
#target.write("\n") #these lines were already specified above 
#target.write(line3) #and now its being written to the file
#target.write("\n")

#print("And finally we close it.")
#target.close() #closing file

from sys import argv
from os.path import exists #impoting somthing new to work with

#script, from_file, to_file = argv
 
#print(f"Copying from {from_file} to {to_file}") #printing that i might be able to copy somthing to something else
#what
#in_file = open(from_file) #in_file here is given to open my from_file, the first arg i give my script, ive been using new.txt
#indata = in_file.read() #even though i just assigned in_file to open my from_file i just passed it to indata and gave it read perms
#print(f"The input file is {len(indata)} bytes long") #using len to count characters in my from_file 
#print(f"Does the output file exist? {exists(to_file)}") #still not sure what exists does but i get it 
#print("Read, hit RETURN to continue, CRTL-C to abort")
#input()
#out_file  = open(to_file, 'w') #my out_file is the second arg i give my script, so whatever name i want it to be it'll be created, use .txt im opening it with write perms
#out_file.write(indata) #ok, i just told out_file to write whats in indata, remember indata was give to in_file.read() which is the first arg i run with my script
#print("Alright, all done")
#out_file.close() #closing
#in_file.close() #closing

def print_two(*args):
      arg1, arg2 = args
      print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
      print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
      print(f"arg1: {arg1}")

def print_none():
      print("I got nothin")

print_two("anime", "soul")
print_two_again("anime", "soul")
print_one("First!")
print_none()

def cheese_and_crackers(cheese_count, boxes_of_crackers):#this is a few ways to give values to some varaibles 

      print(f"You have {cheese_count} cheeses!")
      print(f"You have {boxes_of_crackers} boxes of crackers!")
      print("Get a blanket. \n")

      print("We can just give the function numbers directly:")
      cheese_and_crackers(20,30)
 
      print("Or, we can use variables from our script:")
      amount_of_cheese = 10
      amount_of_crackers = 50
      cheese_and_crackers(amount_of_cheese, amount_of_crackers)

      print("We can even do the math inside too:")
      cheese_and_crackers(10 + 20, 5 + 6)

      print("And we can combine the two, variables and math:")
      cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


#cheese_and_crackers(10,10)

def game_lib(steam, origin):

      steam = input("What library first?:\n") #print(f"There are {steam} steam games and {origin} origin games")

      origin = input("What library next?: \n")

      if steam == 'steam':
            steam = input("How many steam games do you have?:\n")
      else:
            print("Not a library!")
            exit()

      if origin == 'origin':
            origin = input("How many origin games do you have?:\n")
      else:
            return

      print(f"There are {steam} steam games and {origin} origin games")

      games = int(steam) + int(origin) #converted this to an int even before book got there hehe

      print(f"A total of {games} games!")    


game_lib(10,10)








































































































































































































































































