__author__ = 'ddpha2'
problem = ''
problem2 = ''
a = '1'
print("Hello, I am David. What is your name?")
name = input()
print('Hello,' + ' ' + name)
print('How are you today?')

while a == '1':
    mood = input()
    mood = mood.lower()
    if 'you' in mood or 'yourself' in mood:
        print('I am feeling good')
        break
    elif 'sad' in mood or 'bad' in mood or 'not good' in mood or 'angry' in mood or 'annoyed' in mood:
        print('Oh. Sorry to hear that.')
        break
    elif 'happy' in mood or 'great' in mood or 'good' in mood or "well" in mood:
        print('That is good!')
        break
    else:
        print('You did not answer my question.')
        print('How is your day?')

print('Do you want help today?')
question = input()
question = question.lower()

while a == "1":

    if 'yes' in question:
        print("Do you have a problem?")
        problem = input()
        problem = problem.lower()
        break
    elif 'no' in question:
        print("Ok. Have a nice day.")
        break
    else:
        print("Can you please rephrase that? CHEERS")
        question = input()
        question.lower()


if "yes" in problem or "help" in problem:
    print("What is your problem?")
    problem2 = input()
    problem2 = problem2.lower()
elif "no" in problem:
    print("Ok.")

if "lost" in problem2:
    print("I will now make you unlost")
    print("Coding unlost program........")
    print("You are now unlost" + " " + name)
    print("Thank you for using me. Have a nice day")


elif 'nothing' in problem2:
    print("Ok. Thank you for using the chat bot. :)")
elif "life" in problem2:
    print("Life is 42. Please live it to the fullest, " + " " + name + '.')
    print("You are encouraged to live and stay strong.")
elif "thinking" in problem2:
    print("Thinking involves a healthy mental status and an ability to think healthy, " + name + '.')

else:
    print("Well. I guess you do not want help.")


print("Anyways, lets play a game. Do you want to play?")
gameplay = input()
gameplay = gameplay.lower()

if "yes" in gameplay:
    print("Ok. Here is the list.")
    print('There is: word chain, Marco & Polo, Pizza topping and Where is wally.')
    print("Type the name of the game in which you would like to play.")
    game = input()
    game = game.lower()
elif "no" in gameplay:
    print("Ok.")
    print("Goodbye.")

if "word chain" in game:
    print("Welcome to word chain. The rules are as followed: You start by saying a word than you use the ending letter and use that as the new starting word. Eg: word, dog, god, dumb, etc.")
    print("Have fun :). To exit just type EXIT.")
    while a == "1":
        valid = input('Word: ')
        word = input('Word: ')
        while word != '':
            if valid[-1] == word[0]:
                valid = word
                word = input("Word: ")
            elif word == "EXIT" or valid == 'EXIT':
                break
            else:
                print('Nope!')
                word = input('Word: ')


if "marco & polo" in game:
    print("Welcome to Marc & Polo. The rules are simple: You say Marc and I say Polo. Just something to keep you entertained.")
    print("Have fun :). To exit just type EXIT.")
    while a == "1":
        answer = input("Text:")
        if answer == 'Marco!':
            print('Polo!')
        elif answer == 'EXIT':
            print("Ok. Bye!")
            break
        else:
            print("Are you following the rules mate?")


if "pizza topping" in game:
    print("Welcome to Pizza Topping. The rules are simple. Just say a pizza topping than. After you finish press enter to exit the game with the final result. ")
    toppings = []
    top = input('Toppings: ')
    toppings.append(top)
    while top != '':
        top = input('Toppings: ')
        if top == "EXIT":
            break
        elif top not in toppings:

            toppings.append(top)
        else:
            print("Got that already!")

        hello = ''
        for mental in toppings:
            hello = hello + mental + ', '
        print(hello.strip(', '))




if "where is wally" in game:
    print("Welcome to Where is Wally. The rules are as simple as the game. Just type a sentence containing wally or anything and it will check it. Type in GIVE UP. ")
    while a == "1":
        text = input("Enter come text: ")
        text = text.lower()
        if "wally" in text:
            print("Found him!")
        elif "give up" in text:
            break
        else:
            print("Still looking...")


joke = input("Do you want to hear a joke?")
if "no" in joke:
    print("Ok. I guess my time is up than. Good bye" + ' ' + name + '.')
elif "yes" in joke:
    print("Ok. Do you lift?")
    lift_answer = input("")
else:
    print("Did you even answer my question?")
    print("Anyways. Enough talk for today. Live life to the fullest and be safe. Have fun" + " "+ name)

if "yes" in lift_answer:
    print("Very good sir. Continue your ways and you'll be like me :)")
    print("Hope I solved all your problems mate. Hope you have a good one.")
elif "no" in lift_answer:
    print("Well, start lifting and you can be like me.")
    print("Guess me service is finished. Have a good one" + " "+ name + "!")






















