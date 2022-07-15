import fileinput
def password_validate(password):
    pass_lower, pass_upper, pass_special, pass_digits = 0, 0, 0, 0
    # Length – minimum of 10 characters.
    if len(password) >= 10:
        for i in password:

            # counting lowercase alphabets
            if i.islower():
                pass_lower += 1

            # counting uppercase alphabets
            if i.isupper():
                pass_upper += 1

            # counting digits
            if i.isdigit():
                pass_digits += 1

                # counting the mentioned special characters
            if i == '@' or i == '$' or i == '_':
                pass_special += 1
    if pass_lower >= 1 and pass_upper >= 1 and pass_special >= 1 and pass_digits >= 1 and pass_lower + \
            pass_special + pass_upper + pass_digits == len(password):
        return 0
    else:
        if len(password) < 10:
            print('length should be at least 10')
            return 1
        if pass_lower == 0:
            print('Password should have at least one lowercase letter')
        if pass_upper == 0:
            print('Password should have at least one uppercase letter')
        if pass_special == 0:
            print('Password should have at least one of the symbols $@#')
        if pass_digits == 0:
            print('Password should have at least one numeral')

        return 1


def main():
    for line in fileinput.input():
        if password_validate(line) == 0:
            print("\033[92m {}\033[00m".format("Valid Password"))
        else:
            print("\033[91m {}\033[00m".format("Invalid Password"))


if __name__ == '__main__':
    main()
# MyP@ssw0rd!
