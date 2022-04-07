from adminClass import adminAction


class Welcome:
    def welcome(self):
        print("******Welcome to BookMyShow*******\n1.Login\n2.Register\n3.Exit")


def option():
    option = int(input("enter option: "))
    return option


def main():
    admin_dic = {
        'pass': 'admin123'
    }
    while True:
        # created obj of welcome class
        wel = Welcome()
        wel.welcome()
        opt = option()
        if opt == 1:
            user = input("enter login id: ")
            password = input("enter password:")
            if user == 'Admin':
                if admin_dic['pass'] == password:
                    adminAction()
        elif opt == 2:
            pass
        else:
            break


if __name__ == "__main__":
    main()