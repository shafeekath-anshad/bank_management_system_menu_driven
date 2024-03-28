import os
import pathlib
import pickle
import time

from plyer import notification


class Account:  # created class
    acc_no = 0
    name = ''
    address = ''
    deposit = 0
    acc_type = ''
    pin_no = 0

    def add_user(self):
        self.acc_no = int(input("Enter the account no:"))
        self.name = input(print("Enter the name:"))
        self.address = input(print("Enter the address:"))
        self.deposit = int(input(print("Enter the deposit amount (Do not be less than 1000):")))
        self.acc_type = input(print("Enter the account type (savings/current):"))
        self.pin_no = int(input("Enter the pin code:"))
        if __name__ == "__main__":
            notification.notify(
                title="Welcome To the bank",
                message="Congrats!, your account has been created.",
                timeout=3
            )
        time.sleep(10)

    def deposite(self, amount):
        self.deposit += amount

    def withdraw_amt(self, amount):
        self.deposit -= amount

    def change_pin_no(self):
        print("Account Number : ", self.acc_no)
        self.pin_no = int(input("Enter new pin code:"))

    def getAccountNo(self):
        return self.acc_no

    def getUserName(self):
        return self.name

    def getAccountType(self):
        return self.acc_type

    def getDeposit(self):
        return self.deposit

    def getPin_code(self):
        return self.pin_no


def create_account():
    account_obj = Account()
    account_obj.add_user()
    write_accounts_File(account_obj)


def write_accounts_File(account):
    file = pathlib.Path("accounts.data")  # creating a file
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]  # array to store the data into the file
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def deposite_and_withdrawal(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.acc_no == num1:
                if num2 == 1:
                    amount = int(input(print("Enter the amount to be deposited:")))
                    item.deposit += amount
                    if __name__ == "__main__":
                        notification.notify(
                            title="Welcome To the bank",
                            message=" your have been credited into your account."
                                    "For further enquiries please contact bank manager",
                            timeout=3
                        )
                    time.sleep(10)
                elif num2 == 2:
                    amount = int(input("Enter the amount to be withdraw:"))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        if __name__ == "__main__":
                            notification.notify(
                                title="Welcome To the bank",
                                message="sorry!, insufficient balance.please check your account",
                                timeout=3
                            )
                        time.sleep(10)
    else:
        print("No Records found..")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def change_pn_number(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.acc_no == num:
                item.name = input("Enter the new pin code:")

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        if __name__ == "__main__":
            notification.notify(
                title="Welcome To the bank",
                message="You changed your pin code.",
                timeout=3
            )
        time.sleep(10)


def balance_enquiry(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.acc_no == num:
                print("Your account Balance is Rs. ", item.deposit)
                found = True
    else:
        print("Incorrect account no..")
    if not found:
        if __name__ == "__main__":
            notification.notify(
                title="Welcome To the bank",
                message="Incorrect Account no.. please try again..",
                timeout=3
            )
        time.sleep(10)


def view_account_users():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:

            print(item.acc_no, "      ", item.name, "     ", item.acc_type, "      ", item.deposit, "      ", item.pin_no)
        infile.close()
    else:
        print("No records to display")


def close_account(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.acc_no != num:
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        if __name__ == "__main__":
            notification.notify(
                title="Welcome To the bank",
                message="The account is closed..Thank you for your trust..",
                timeout=3
            )
        time.sleep(10)



# program #

result = ''
num = 0
while result != 2:
    print("Welcome to BANK..")
    print("======================")
    print("Please enter the number...")
    print("1.Add Account")
    print("2.Add Deposite")
    print("3. Withdraw Amount")
    print("4.Change pin no.")
    print("5. Balance Enquiry")
    print("6. View All Users")
    print("7. Close the account")
    print("8. EXIT")

    result = input()
    if result == '1':
        create_account()
    elif result == '2':
        num = int(input(print("Enter the account no:")))
        deposite_and_withdrawal(num, 1)
    elif result == '3':
        num = int(input("Enter the account no:"))
        deposite_and_withdrawal(num, 2)
    elif result == '4':
        num = int(input("Enter the account no:"))
        change_pn_number(num)
    elif result == '5':
        num = int(input(print("Enter the account no:")))
        balance_enquiry(num)
    elif result == '6':
        print("acc no", " ", "name", " ", "acc type", " ", "deposite", " ", "pin code")
        view_account_users()
    elif result == '7':
        num = int(input("Enter the account_no:"))
        close_account(num)
    elif result == '8':
        if __name__ == "__main__":
            notification.notify(
                title="Thank you forthe visit",
                message="For more information visit your nearby branch.",
                timeout=3
            )
        time.sleep(10)
    else:
        print("invalid number..")
