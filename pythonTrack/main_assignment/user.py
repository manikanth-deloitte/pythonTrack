import openpyxl


class User:
    def __init__(self):
        self.path = "\\Users\\amanikanth\\PycharmProjects\\pythonTrack\\main_assignment\\excelfiles\\movieDetails.xlsx"
        self.wb = openpyxl.load_workbook(self.path)
        self.sh1 = self.wb['Sheet1']

    def todoAction(self):
        print("1.Book Tickets\n2.Cancel Tickets\n3.Give User Rating")

    @staticmethod
    def moviesList():
        path = "\\Users\\amanikanth\\PycharmProjects\\pythonTrack\\main_assignment\\excelfiles\\movieDetails.xlsx"
        wb = openpyxl.load_workbook(path)
        sh1 = wb['Sheet1']
        r = sh1.max_row
        print("movie lists:")
        for i in range(2, r+1):
            val = sh1.cell(i, 1).value
            print(i, f".{val}")
        print(r+1,".logout")

    def movieDetails(self,opt):
        row = opt
        c = self.sh1.max_column
        mov_dic = {}
        for col in range(1,c+1):

            # add to dictionary
            attr = self.sh1.cell(1, col).value
            mov_dic[attr]=self.sh1.cell(row, col).value

            if col == 1 or col ==2 or col == 3 or col == 4 or col == 5 or col == 6:
                print(f"{attr}:",self.sh1.cell(row, col).value)
            if col == 12:
                print(f"{attr}:", self.sh1.cell(row, col).value)
            if col == c+1:
                print(f"{attr}:",self.sh1.cell(row, col).value)

        return mov_dic

    def updateCap(self,val,opt):
        r=1
        row = opt
        c = self.sh1.max_column
        for col in range(1,c+1):
            if col == 13:
                self.sh1.cell(row, col).value =val

        self.wb.save(self.path)
        print("up val:", self.sh1.cell(row, 13).value)


def userAction(user1):
    user = User()
    print(f"******Welcome {user1} *******")
    user.moviesList()
    opt1 = int(input('enter movie: '))
    details = user.movieDetails(opt1)
    user.todoAction()
    opt = int(input("select above options: "))
    if opt == 1:
        print(f"******Welcome {user1} *******")
        timings = details['Timings']
        lst = timings.split(',')
        dic_ti ={}
        print("movie timings : ")
        for i in range(len(lst)):
            print(i+1, ".", lst[i])
            dic_ti[i+1]=lst[i]

        # select timing
        sel = int(input("select timing: "))
        timing = dic_ti[sel]
        print("Timing:", timing)
        seats = details['Capacity']
        print("Remaining Seats:", seats)
        sel_seats = input("enter the no of seats to be selected:")
        upt_seats = int(seats)-int(sel_seats)
        user.updateCap(upt_seats,opt1)


def userlogin(username,password):
    path = "\\Users\\amanikanth\\PycharmProjects\\pythonTrack\\main_assignment\\excelfiles\\movieDetails.xlsx"
    wb = openpyxl.load_workbook(path)
    sh2 = wb['Sheet2']
    r = sh2.max_row
    col = 1
    for row in range(1, r + 1):
        user_name = sh2.cell(row, col).value
        if username == user_name:
            pass_word = sh2.cell(row, 5).value

            if pass_word == password:
                print("logged in successful!")
                userAction(user_name)
                break
            else:
                print("password doesn't match")
                break
    else:
        print("register before logging in ")