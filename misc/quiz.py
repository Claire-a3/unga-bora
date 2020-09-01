def show_menu():
    print("1. ask Qs")
    print("2. Add Qs")
    print("3. Quit")

    option =input("enter option:")
    return option
def ask_questions():
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)

    for question, answer in zip(questions, answers):
        guess = input(question + "> ")
    
    
    
def add_question():
    print("")
    question = input("enter Q\n")
    
    print("")
    print("ok whats the answer?")
    answer = input("{0}\n> ".format(question))
    
    
    file = open("questions.txt", "a")
    file.write(question +"\n")
    file.write(answer +"\n")
    file.close()
    
def game_loop():
    while True:
            option = show_menu()
            if option == "1":
                ask_questions()
            elif option == "2":
                add_question()
            elif option == "3":
                    break
            else:
                print("enter 1, 2 or 3 pls")
            print("")
game_loop()

                    