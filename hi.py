import random 
words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of/from"},
    {"spanish": "que", "english": "that/which"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to/at"},
    {"spanish": "en", "english": "in/on"},
    {"spanish": "un", "english": "a/an"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself/itself"},
    {"spanish": "no", "english": "no/not"},
    {"spanish": "haber", "english": "to have (auxiliary)"},
    {"spanish": "por", "english": "for/by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his/her/your/their"},
    {"spanish": "para", "english": "for/to"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "him/her/you (indirect object)"},
    {"spanish": "lo", "english": "it/him/you (direct object)"}
]


def quiz_users(words):
    random.shuffle(words)
    score = 0
    for word in words:
        print(f"What is the English Translation of '{word['spanish']}'?")
        print("Or Press 1 to leave the Quiz")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()
        if(user_answer == correct_answer):
            print("Correct!!\n")
            score += 1

        elif(user_answer == '1'):
            break
        
        else:
            print(f"Wrong answer,The correct answer is {word['english']}.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")            


def main() :
    print("Welcome to Language Learning App!")
    input(("Press Enter to start the Quiz..."))
    quiz_users(words)

if __name__ == "__main__":
    main()
    
