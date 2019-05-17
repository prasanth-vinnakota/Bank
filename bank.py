print("\t\t\t*** Bank ***")

user_data = {}
bank_data = {}


def user_choice():
    print("\n\t\t\t--- Home page ---")
    try:
        choice = int(input("Options to choice: "
                           "\n1.Create a account"
                           "\n2.Login"
                           "\n3.Exit application\n\n"))

        dashboard(choice)
    except ValueError:
        print("Invalid option")
        user_choice()


def dashboard(choice):
    if choice == 1:
        print("\n\t\t\t---Register your details---")
        name = input("Name: ")
        age = int(input("Age: "))
        city = input("City: ")
        account_type = input("Type of account: ")
        amount = int(input("Initial deposited amount: "))
        account_no = int(input("Account no: "))

        user_data['name'] = name
        user_data['age'] = age
        user_data['city'] = city
        user_data['account_type'] = account_type
        user_data['amount'] = amount

        bank_data[account_no] = user_data

        print("\n---Account successfully created---\n\n")
        user_choice()
        dashboard(choice)

    elif choice == 2:
        account_no = int(input("Account no: "))

        if account_no in bank_data:
            print("\n---Login successful---")
            home(account_no, choice)

        else:
            print("No account found with account no.{}\n\n".format(account_no))
            user_choice()
            dashboard(choice)

    elif choice == 3:
        print('\t\t\t---Application closed---')
        exit(0)

    else:
        print("Invalid option")
        user_choice()


def home(account_no, choice):
    print("\n\t\t\t--- Dashboard ---")
    login_choice = int(input("\nOptions to choice: "
                             "\n1.Balance enquiry"
                             "\n2.Deposit amount"
                             "\n3.Withdraw amount"
                             "\n4.View profile"
                             "\n5.Logout\n"))

    if login_choice == 1:
        print("Available balance is {}".format(bank_data[account_no]['amount']))
        home(account_no, choice)

    elif login_choice == 2:
        deposited_amount = int(input("Enter amount: "))
        bank_data[account_no]['amount'] += deposited_amount
        print("\n{} is credited to your account {}.\nAvailable balance is {}"
              .format(deposited_amount, account_no, bank_data[account_no]['amount']))
        home(account_no, choice)

    elif login_choice == 3:
        withdraw_amount = int(input("Enter amount"))

        if withdraw_amount > bank_data[account_no]['amount']:
            print("Insufficient Balance")

        else:
            bank_data[account_no]['amount'] -= withdraw_amount
            print("{} is debited from your account {}.\nAvailable balance is {}"
                  .format(withdraw_amount, account_no, bank_data[account_no]['amount']))

        home(account_no, choice)

    elif login_choice == 4:
        print("\n\t---User information---")
        print("Name : {}".format(bank_data[account_no]['name']))
        print("Age : {}".format(bank_data[account_no]['age']))
        print("City : {}".format(bank_data[account_no]['city']))
        print("\n\t---Account information---")
        print("Account type : {}".format(bank_data[account_no]['account_type']))
        print("Account no : {}".format(account_no))

        home(account_no, choice)

    elif login_choice == 5:
        print('\n\n')
        user_choice()

    else:
        print("Invalid option")
        home(account_no, choice)


user_choice()
