from utils.ui import banner_large
from src.session import check_login


# s = datetime.now() + timedelta(hours=1)
# e = datetime.now() + timedelta(hours=3)
# res = reservations.Reservation("00", "78", 420.69, False, s, e)

# print(res)


def main():
    print(banner_large)

    logged_in = 0

    while not logged_in:
        logged_in = check_login()


if __name__ == "__main__":
    main()
