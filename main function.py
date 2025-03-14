import sys
from display_function import add_item, display_items, search_item , delete_item , return_date , check_fine , update_item ,return_status, update_fine, payment_status

# Variables for user types
a = 'Student'
b = 'Staff'

# Preset data for different categories
library_items = {
    "Novel": [
        ['Novel', 'The Notebook', 'Nicholas Sparks', '1996','return'],
        ['Novel', 'It Ends With Us', 'Colleen Hoover', '2016','not return'],
        ['Novel', 'Book Lovers', 'Emily Henry', '2022','return'],
        ['Novel', 'Twilight Saga Series', 'Stephanie Meyer', '2005 - 2006','return'],
        ['Novel', 'Harry Potter Series', 'J.K. Rowling', '1997','return'],
        ['Novel', 'Me before You', 'Jojo Moyes', '2012','return'],
        ['Novel', 'Outlander', 'Diana Gabaldon', '1991','return'],
        ['Novel', 'The Fault in Our Stars', 'John Green', '2012','not return'],
        ['Novel', 'Happy Place', 'Emily Henry', '2023','return'],
        ['Novel', 'Pride and Prejudice', 'Jane Austen', '1813','not return']
    ],
    "Magazine": [
        ['Magazine', 'Fast Company', '-', '1995','not return'],
        ['Magazine', 'Forbes India', '-', '2008','not return'],
        ['Magazine', 'Business Today', '-', '2001','return'],
        ['Magazine', 'Vogue Magazine', '-', '1856 - 1906','return'],
        ['Magazine', 'Harvard Business Review', '-', '1922','not return']
    ],
    "Dictionary": [
        ['Dictionary', 'Collins English Dictionary', 'Collins Dictionaries', '2009','return'],
        ['Dictionary', 'Arabic - English Bilingual Visual Dictionary', 'Dorling Kindersley', '2009','return'],
        ['Dictionary', 'Mandarin Chinese-English Bilingual Visual Dictionary', 'DK Pub', '2015','return'],
        ['Dictionary', 'Oxford Advanced Learner Dictionary 9th Edition', 'A.S. Hornby', '2015','not return'],
        ['Dictionary', 'Malay Dictionary: English-Malay, Malay-English', 'Othman Sulaiman', '1989','not return']
    ],
    "Book": [
        ['Book', 'Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones', 'James Clear', '2018','return'],
        ['Book', 'Thinking, Fast and Slow', 'Daniel Kahneman', '2011','not return'],
        ['Book', 'Think and Grow Rich', 'Napoleon Hill', '1937','not return'],
        ['Book', 'The Power of Habit', 'Charles Duhigg', '2012','not return'],
        ['Book', 'Good Economics for Hard Times', 'Esther Duflo', '2019','return'],
        ['Book', 'The Wealth of Nations', 'Adam Smith', '1776','not return'],
        ['Book', 'Hidden Order', 'David Friedman', '1996','return'],
        ['Book', 'The Lean Startup', 'Eric Ries', '2011','return'],
        ['Book', 'Start with Why: How Great Leaders Inspire Everyone to Take Action', 'Simon Sinek', '2009','return'],
        ['Book', 'The Hard Thing About Hard Things', 'Ben Horowitz', '2014','return']
    ]
}

# Combine all categories into a single list
combined_items = []
for category, items in library_items.items():
    for item in items:
        combined_items.append([category] + item[1:])

# Sort combined_items by title (index 1)
combined_items.sort(key=lambda x: x[1])

# Main Menu
def main_menu():
    print("\n\n-----------------------------------------------------\n")
    print("\n\t\tLibrary Management System\n")
    print("-----------------------------------------------------\n")
    print("[1] " + a)
    print("[2] " + b)
    
    print("\n-----------------------------------------------------\n")
    choice = input("\nEnter your choice : ")
    
    try:
        choice = int(choice)
        
        if choice == 1:  # For Student
         while True:
            print("\n\n-----------------------------------------------------\n")
            print("\t\tWelcome " + a)
            print("\n-----------------------------------------------------\n")
            print("[i]    Add books/magazines/novels/dictionaries to borrow list")
            print("[ii]   Search available items")# letak status available ke tak, update status, return date etc dkt preset data
            print("[iii]  Delete items")
            print("[iv]   Display All items")
            print("[v]    Check return date")
            print("[vi]   Check fine")
            print("[vii]  Close program")
            print("[viii] Return to homepage")
            
            user_input = input("\nEnter your choice : ")  # User input for student
            if user_input == 'i':
                 add_item(library_items)
            elif user_input == 'ii':
                title = input("Enter the title to search: ")
                result = search_item(combined_items, title)
                if result:
                    print("Item found:", result)
                else:
                    print("Item not found.")
            elif user_input == 'iii':
                delete_item(library_items,combined_items)
            elif user_input == 'iv':
                display_items(combined_items)
            elif user_input == 'v':
                return_date()
            elif user_input == 'vi':
                check_fine()
            elif user_input == 'vii':
                print("Your session ended.")
                sys.exit()
            elif user_input == 'viii':
                print("Returning to homepage...")
                main_menu()  # Optionally call main_menu again to restart the menu
            else:
                print("Invalid choice.")

        elif choice == 2:  # For Staff
         while True:
            print("\n\n-----------------------------------------------------\n")
            print("\t\tWelcome " + b)
            print("\n-----------------------------------------------------\n")
            print("[i]   Update book/magazine/novel/dictionary availability")
            print("[ii]  Check return item status")
            print("[iii] Update student fine")
            print("[iv]  Check payment status")
            print("[v]   Close program")
            print("[vi]  Return to homepage")

            user_input = input("\nEnter your choice : ")  # User input for staff
            if user_input == 'i':
                update_item()
            elif user_input == 'ii':
                return_status()
            elif user_input == 'iii':
                update_fine()
            elif user_input == 'iv':
                payment_status()
            elif user_input == 'v':
                print("Your session ended.")
                sys.exit()
            elif user_input == 'vi':
                print("Returning to homepage...")
                main_menu()  # Optionally call main_menu again to restart the menu
            else:
                print("Invalid choice.")
            

        else:
            print("Sorry, but you have entered wrong input. Please enter again!")

    except ValueError:
        print("Oopsie! Invalid input! Please enter a new input.")

if __name__ == "__main__":
    main_menu()
