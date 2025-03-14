
from datetime import datetime, timedelta

today = datetime.today()
due_in_7_days = (today + timedelta(days=7)).strftime('%Y-%m-%d')
due_in_3_days = (today + timedelta(days=3)).strftime('%Y-%m-%d')
# Library items data
library_items = {
    "Novel": [
        ['Novel', 'The Notebook', 'Nicholas Sparks', '1996', 'return', None, 'fines'],
        ['Novel', 'It Ends With Us', 'Colleen Hoover', '2016', 'not return', 'due_in_7_days', '-'],
        ['Novel', 'Book Lovers', 'Emily Henry', '2022', 'return', None, '-'],
        ['Novel', 'Twilight Saga Series', 'Stephanie Meyer', '2005 - 2006', 'return', None, '-'],
        ['Novel', 'Harry Potter Series', 'J.K. Rowling', '1997', 'return', None, '-'],
        ['Novel', 'Me before You', 'Jojo Moyes', '2012', 'return', None, '-'],
        ['Novel', 'Outlander', 'Diana Gabaldon', '1991', 'return', None, '-'],
        ['Novel', 'The Fault in Our Stars', 'John Green', '2012', 'not return', 'due_in_3_days', '-'],
        ['Novel', 'Happy Place', 'Emily Henry', '2023', 'return', None, '-'],
        ['Novel', 'Pride and Prejudice', 'Jane Austen', '1813', 'not return', 'due_in_7_days', '-']
    ],
    "Magazine": [
        ['Magazine', 'Fast Company', '-', '1995', 'not return', 'due_in_7_days', '-'],
        ['Magazine', 'Forbes India', '-', '2008', 'not return', 'due_in_7_days', '-'],
        ['Magazine', 'Business Today', '-', '2001', 'return', None, 'fines'],
        ['Magazine', 'Vogue Magazine', '-', '1856 - 1906', 'return', None, '-'],
        ['Magazine', 'Harvard Business Review', '-', '1922', 'not return', 'due_in_7_days', '-']
    ],
    "Dictionary": [
        ['Dictionary', 'Collins English Dictionary', 'Collins Dictionaries', '2009', 'return', None, '-'],
        ['Dictionary', 'Arabic - English Bilingual Visual Dictionary', 'Dorling Kindersley', '2009', 'return', None, '-'],
        ['Dictionary', 'Mandarin Chinese-English Bilingual Visual Dictionary', 'DK Pub', '2015', 'return', None, '-'],
        ['Dictionary', 'Oxford Advanced Learner Dictionary 9th Edition', 'A.S. Hornby', '2015', 'not return', 'due_in_7_days', '-'],
        ['Dictionary', 'Malay Dictionary: English-Malay, Malay-English', 'Othman Sulaiman', '1989', 'not return', 'due_in_3_days', '-']
    ],
    "Book": [
        ['Book', 'Atomic Habits', 'James Clear', '2018', 'return', None, 'fines'],
        ['Book', 'Thinking, Fast and Slow', 'Daniel Kahneman', '2011', 'not return', 'due_in_7_days', '-'],
        ['Book', 'Think and Grow Rich', 'Napoleon Hill', '1937', 'not return', 'due_in_7_days', '-'],
        ['Book', 'The Power of Habit', 'Charles Duhigg', '2012', 'not return', 'due_in_7_days', '-'],
        ['Book', 'Good Economics for Hard Times', 'Esther Duflo', '2019', 'return', None, '-'],
        ['Book', 'The Wealth of Nations', 'Adam Smith', '1776', 'not return', 'due_in_7_days', '-'],
        ['Book', 'Hidden Order', 'David Friedman', '1996', 'return', None, '-'],
        ['Book', 'The Lean Startup', 'Eric Ries', '2011', 'return', None, '-'],
        ['Book', 'Start with Why', 'Simon Sinek', '2009', 'return', None, '-'],
        ['Book', 'The Hard Thing About Hard Things', 'Ben Horowitz', '2014', 'return', None, '-']
    ]
}


#add function
def add_item(library_items):
    item_type = input("Enter the type of item to add (Book, Magazine, Novel, Dictionary): ").capitalize()
    
    if item_type not in library_items:
        print("Invalid item type. Please enter Book, Magazine, Novel, or Dictionary.")
        return
    
    title = input("Enter the title: ")
    author_or_publisher = input("Enter the author/publisher: ")
    date_published = input("Enter the date published (e.g., 2022): ")
    
    # Ask for borrowing duration
    try:
        duration_days = int(input("Enter the number of days you want to borrow the item: "))
        
        if duration_days > 14:
            print("Sorry, the duration exceeds our borrowing policy. If you would like to borrow, we will set it to 14 days.")
            user_input = input("Enter 'yes' to proceed with 14 days or 'no' to cancel: ").strip().lower()
            
            if user_input == 'yes':
                duration_days = 14
            elif user_input == 'no':
                print("Thank you for choosing our service. Please come back again <3.")
                return  # Exit the function if the user chooses 'no'
            else:
                print("Invalid input. Setting duration to 14 days by default.")
                duration_days = 14
        
    except ValueError:
        print("Invalid input for borrowing duration. Setting duration to 14 days by default.")
        duration_days = 14
    
    # Generate due date
    today = datetime.today()
    due_date = today + timedelta(days=duration_days)
    
    # Add item to library_items
    library_items[item_type].append([item_type, title, author_or_publisher, date_published])
    
    print(f"Item added successfully! The due date for return is: {due_date.strftime('%Y-%m-%d')}")


#display function
def display_items(items):
    if items:
        headers = ["TYPE", "TITLE", "AUTHOR/PUBLISHER", "DATE PUBLISHED"]
        # Calculate column widths
        col_widths = [max(len(row[i]) for row in [headers] + items) for i in range(len(headers))]
        
        # Create a horizontal line
        h_line = '+' + '+'.join(['-' * (width + 2) for width in col_widths]) + '+'
        
        # Print header
        print(h_line)
        print('| ' + ' | '.join([headers[i].ljust(col_widths[i]) for i in range(len(headers))]) + ' |')
        print(h_line)
        
        # Print rows
        for item in items:
            print('| ' + ' | '.join([item[i].ljust(col_widths[i]) for i in range(len(item))]) + ' |')
        print(h_line)
    else:
        print("No items available.")

from difflib import get_close_matches

def search_item(items, target):
    target_lower = target.lower()
    
    # Create a list of titles for comparison
    titles = [item[1].lower() for item in items]
    
    # Check for exact match first
    for item in items:
        if item[1].lower() == target_lower:
            return ', '.join(item)
    
    # If no exact match, find closest matches
    closest_matches = get_close_matches(target_lower, titles, n=1, cutoff=0.6)
    
    if closest_matches:
        # Find the item corresponding to the closest match
        closest_title = closest_matches[0]
        for item in items:
            if item[1].lower() == closest_title:
                return f"No exact match found. Did you mean : {', '.join(item)}"
    
    return "Item not found."

# Sample usage
if __name__ == "__main__":
    sample_items = [
        ['Novel', 'The Notebook', 'Nicholas Sparks', '1996'],
        ['Novel', 'It Ends With Us', 'Colleen Hoover', '2016'],
        # Add more sample items if needed
    ]
    search_result = search_item(sample_items, 'the notebook')
    print(search_result)

#function delete item
def delete_item(library_items, combined_items):
    # Ask user for the type of item to delete
    item_type = input("Enter the type of item to delete (Book, Magazine, Novel, Dictionary): ").capitalize()
    
    if item_type not in library_items:
        print("Invalid item type. Please enter Book, Magazine, Novel, or Dictionary.")
        return
    
    title = input("Enter the title of the item to delete: ").strip().lower()
    
    # Search and delete item
    item_found = False
    for item in library_items[item_type]:
        if item[1].lower() == title:
            item_found = True
            # Check if the item is currently borrowed
            borrowed = False
            for borrowed_item in combined_items:  # Iterate directly over combined_items
                if borrowed_item[1].lower() == title.lower():
                    borrowed = True
                    print(f"Item found and currently borrowed: {borrowed_item[1]}")
                    break
            
            if borrowed:
                print("The item is currently borrowed and cannot be deleted.")
                return
            
            # Remove item from the list
            library_items[item_type].remove(item)
            print(f"Item '{title}' has been deleted successfully.")
            return
    
    if not item_found:
        print(f"No item with title '{title}' found in {item_type} category.")

# Function to check return date
def return_date():
    item_type = input("Enter type of item (Book, Magazine, Novel, Dictionary) to find out return date: ").capitalize()
    
    if item_type not in library_items:
        print("Invalid item type. Please enter Book, Magazine, Novel, or Dictionary.")
        return
    
    title = input("Enter the title: ").strip().lower()
    
    # Search for the item in the specified category
    found_item = None
    for item in library_items[item_type]:
        if item[1].lower() == title:
            found_item = item
            break
    
    if found_item:
        # Check if the item has been returned
        if found_item[-2].lower() == 'return':  # Corrected index to access the return status
            print(f"The item '{title}' has been returned and is available.")
        else:
            print(f"The item '{title}' has not been returned. It is due by: {found_item[-1]}")
    else:
        print(f"No item with title '{title}' found in {item_type} category.")

#check fine
def check_fine():
    user_input = input("If you want to check additional charges, enter 'yes' or 'no': ").strip().lower()

    if user_input == 'yes':
        total_fines = 0

        # Display fines data
        print("The charges stated as below:\n")
        for category, items in library_items.items():
            for item in items:
                if item[6] == 'fines':
                    # Display the item details
                    print(f"Category: {category}")
                    print(f"Item Type: {item[0]}")
                    print(f"Title: {item[1]}")
                    print(f"Author/Publisher: {item[2]}")
                    print(f"Year: {item[3]}")
                    print(f"Return Status: {item[4]}")
                    print(f"Due Date Status: {item[5]}")
                    print(f"Additional Charge: RM 5")
                    print("-" * 40)
                    # Accumulate total fines
                    total_fines += 5
        
        print(f"Total fines: RM {total_fines}\n\n")
    
    else:
        print("No additional charges to display.")

#for staff function

#update item
def update_item():
    item_type = input("Enter the type of item to update (Book, Magazine, Novel, Dictionary): ").capitalize()
    if item_type not in library_items:
        print("Invalid item type. Please enter Book, Magazine, Novel, or Dictionary.")
        return
    
    title = input("Enter the title of the item to update: ").strip().lower()
    
    # Search for the item in the specified category
    found_item = None
    for item in library_items[item_type]:
        if item[1].lower() == title:
            found_item = item
            break
    
    if found_item:
        new_status = input(f"Current status is '{found_item[4]}'. Do you want to update this status? Enter 'yes' or 'no': ").strip().lower()
        if new_status == 'yes':
            updated_status = input("Enter new status (return/not return): ").strip().lower()
            found_item[4] = updated_status
            print(f"Status for '{title}' updated to '{updated_status}'.")
        else:
            print("No changes made.")
    else:
        print(f"No item with title '{title}' found in {item_type} category.")

#check return item
def return_status():
    item_type = input("Enter the type of item (Book, Magazine, Novel, Dictionary): ").capitalize()
    
    if item_type not in library_items:
        print("Invalid item type. Please enter Book, Magazine, Novel, or Dictionary.")
        return
    
    title = input("Enter the title of the item to check: ").strip().lower()
    
    # Search for the item in the specified category
    found_item = None
    for item in library_items[item_type]:
        if item[1].lower() == title:
            found_item = item
            break
    
    if found_item:
        print(f"The current return status of '{title}' is '{found_item[4]}'.")
        update_status = input("Do you want to update the status? Enter 'yes' or 'no': ").strip().lower()
        if update_status == 'yes':
            new_status = input("Enter new status (return/not return): ").strip().lower()
            found_item[4] = new_status
            print(f"Status for '{title}' updated to '{new_status}'.")
        else:
            print("No changes made.")
    else:
        print(f"No item with title '{title}' found in {item_type} category.")

#check update fine
def update_fine():
    item_type = input("Enter the type of item (Book, Magazine, Novel, Dictionary): ").capitalize()
    
    if item_type not in library_items:
        print("Invalid item type. Please enter Book, Magazine, Novel, or Dictionary.")
        return
    
    title = input("Enter the title of the item to check fines: ").strip().lower()
    
    # Search for the item in the specified category
    found_item = None
    for item in library_items[item_type]:
        if item[1].lower() == title:
            found_item = item
            break
    
    if found_item:
        print(f"The current fine status of '{title}' is '{found_item[6]}'.")
        if found_item[6] == 'fines':
            update_fine_status = input("Has the student paid the fine? Enter 'yes' or 'no': ").strip().lower()
            if update_fine_status == 'yes':
                found_item[6] = '-'
                print(f"Fine status for '{title}' has been updated to 'paid'.")
            else:
                print("No changes made.")
        else:
            print("This item has no outstanding fines.")
    else:
        print(f"No item with title '{title}' found in {item_type} category.")

#payment status
def payment_status():
    item_type = input("Enter the type of item (Book, Magazine, Novel, Dictionary): ").capitalize()
    
    if item_type not in library_items:
        print("Invalid item type. Please enter Book, Magazine, Novel, or Dictionary.")
        return
    
    title = input("Enter the title of the item to check payment status: ").strip().lower()
    
    # Search for the item in the specified category
    found_item = None
    for item in library_items[item_type]:
        if item[1].lower() == title:
            found_item = item
            break
    
    if found_item:
        print(f"The current payment status of '{title}' is '{found_item[6]}'.")
        if found_item[6] == 'fines':
            payment_made = input("Has the fine been paid? Enter 'yes' or 'no': ").strip().lower()
            if payment_made == 'yes':
                found_item[6] = '-'
                print(f"Payment status for '{title}' has been updated to 'paid'.")
                send_notice = input("Do you want to send a notice to the student? Enter 'yes' or 'no': ").strip().lower()
                if send_notice == 'yes':
                    print(f"Notice has been sent to the student regarding the payment for '{title}'.")
                else:
                    print("No notice sent.")
            else:
                print("No changes made.")
        else:
            print("This item has no outstanding fines.")
    else:
        print(f"No item with title '{title}' found in {item_type} category.")
