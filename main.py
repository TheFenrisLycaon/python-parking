from utils.ui import banner_large
from src.session import check_login


def main():
    print(banner_large)

    logged_in = 0

    while not logged_in:
        logged_in = check_login()


if __name__ == "__main__":
    main()
