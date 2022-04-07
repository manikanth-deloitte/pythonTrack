from excel import Excel
import calculateTimings


class Admin(Excel):
    def welcomeAdmin(self):
        print("******Welcome Admin*******\n1. Add New Movie Information\n2. Edit Movie Info\n3. Delete Movies\n4.Logout")

    def addMovie(self, lst):
        super().writeExcel(lst)


def adminAction():
    while True:
        # created obj of admin class
        admin = Admin()
        admin.welcomeAdmin()
        opt = int(input("enter option: "))
        if opt == 1:
            info_new_movie = []
            title = input("enter movie name: ")
            info_new_movie.append(title)
            genre = input("enter genre: ")
            info_new_movie.append(genre)
            length = input("enter the duration in hrs:min format")
            info_new_movie.append(length)
            cast = input("enter Cast: ")
            info_new_movie.append(cast)
            director = input("enter director name: ")
            info_new_movie.append(director)
            admin_rating = input("enter admin rating: ")
            info_new_movie.append(admin_rating)
            language = input("enter language")
            info_new_movie.append(language)
            interval_time = input("enter interval-time should be in number :")
            info_new_movie.append(interval_time)
            shows = input("enter no of shows")
            info_new_movie.append(shows)
            first_show = input("enter first show timing in hr:min:sec format: ")
            info_new_movie.append(first_show)
            gap = input("enter gap b/w the shows: ")
            info_new_movie.append(gap)
            timings = calculateTimings.calTime(shows,first_show,gap,interval_time,length)
            info_new_movie.append(timings)
            capacity = input("enter the total tickets: ")
            info_new_movie.append(capacity)
            admin.addMovie(info_new_movie)
        elif opt == 2:pass
        elif opt == 3:pass
        else:
            break