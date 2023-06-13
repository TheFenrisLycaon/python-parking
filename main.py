from src import reservations
from datetime import datetime, timedelta
from utils import banner, ui
from src.session import login, signup

# s = datetime.now() + timedelta(hours=1)
# e = datetime.now() + timedelta(hours=3)
# res = reservations.Reservation("00", "78", 420.69, False, s, e)

# print(res)


def main():
    print(banner.banner_large)

    user_check = int(input("[1] Login / [2] Sign Up\n\tEnter you choice::\t"))

    if user_check == 1:
        ui.clear()
        print(banner.banner_small)
        print("Logging in...")
        login()
    elif user_check == 2:
        ui.clear()
        print(banner.banner_small)
        print("Signing Up...")
        signup()
    else:
        ui.clear()
        print(banner.banner_small)
        print("Wrong Choice...\t Exiting...")


if __name__ == "__main__":
    main()
