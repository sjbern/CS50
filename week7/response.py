from validator_collection import validators

def main():
    emailAddy = input("What's your email?")
    try:
        validEmail = validators.email(emailAddy)
        print('Valid')
    except:
        print('Invalid')

if __name__ == "__main__":
    main()