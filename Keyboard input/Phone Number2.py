def format_phone_number(phone_number):
    # Remove any non-digit characters from the input
    digits_only = "".join(filter(str.isdigit, phone_number))

    # Check if the number is 10 digits long
    if len(digits_only) == 10:
        # Format the number as (XXX) XXX-XXXX
        formatted_number = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
        return formatted_number
    else:
        return "Invalid phone number format"


def main():
    phone_number = input("Please enter your phone number: ")
    formatted_number = format_phone_number(phone_number)
    print("Formatted phone number:", formatted_number)


if __name__ == "__main__":
    main()