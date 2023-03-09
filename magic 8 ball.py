#TrungDong
#U42594715
#use the random module to get a random number, main function to get input for questions and answer to questions
#response function contatin a list of response and return the response base on the order

import random 

def response(x):
    magic_ball = ["It is certain.", "It is decidely so.", "Without a doubt.", "Yes - definitely.", 
    "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
    "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
    "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
    "My sources say no.", "Outlook not so good.", "Very doubtful."]

    return magic_ball[x]

def main():
    question = input("What is your question? ")
    x = random.randint(0, 19)
    print(response(x))
    repeat = input("Would you like to ask another question? ").lower()
    while repeat != "no":
        question = input("What is your question? ")
        x = random.randint(0, 19)
        print(response(x))
        repeat = input("Would you like to ask another question? ").lower()

if __name__ == '__main__': 
    main()
    
