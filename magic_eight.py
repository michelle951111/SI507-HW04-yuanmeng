
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
