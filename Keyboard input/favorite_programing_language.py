# Make a program that asks the users preferred programming language.

def get_programming_language():
    programming_language = input("Enter your favorite programming language: ")
    return programming_language


def main():
    programming_language = get_programming_language()
    print(f"You said {programming_language} is your favorite programming language")

if __name__ == "__main__":
    main()