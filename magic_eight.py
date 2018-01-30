
import random



all_answers=["It is certain", "It is decidedly so", "Without a doubt",
              "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely",
     "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
     "Ask again later", "Better not tell you now", "Cannot predict now",
     "Concentrate and ask again", "Don't count on it", "My reply is no",
     "My sources say no", "Outlook not so good", "Very doubtful"
     ]


def question():
 print("What is your question?")
 question = input()
 return question

user_question = question()
while(user_question!= "quit"):

    if user_question.endswith("?"):
        answer=print(random.choice(all_answers))

    else:
        print("I’m sorry, I can only answer questions.")

    user_question = question()
