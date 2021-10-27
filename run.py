import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('store-sales')


def start():
    """
    Start menu that the user can choose between 6 different tasks.
    """
    print("""
                --------MENU--------
                1. Add new item\n\
                2. View all items\n\
                3. Delete an item\n\
                4. Search item\n\
                5. Reset items\n\
                6. Exit\n
                    """)

    while True:
        choise = input("Choose the number of the task you want to do: \n")
        if choise == '1':
            print(" Add new item...\n")
            add_new_item()
            break
        elif choise == '2':
            print("View all item...\n")
            show_all_item()
            break
        elif choise == '3':
            print(" Delete an item...\n")
            print("You have to search for the contact you want to delete\n")
            search_item()
            break
        elif choise == '4':
            print("Search menu...\n")
            search_item()
            break
        elif choise == '5':
            print("Reset items...\n")
            validate_reset()
            break
        elif choise == '6':
            print("Exit programme...")
            exit_programme()
            break
        else:
            print("Not a valid input please enter a number 1-6")


def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
     
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_sales_data()