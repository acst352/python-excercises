# Make a program that asks a phone number

def get_phone_number():
    phone_number = input("Please enter your phone number: ")
    return phone_number


def main():
    phone_number = get_phone_number()
    print("You entered the phone number:", phone_number)


if __name__ == "__main__":
    main()