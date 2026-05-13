import os

# The physical file where our list data will be saved
FILE_NAME = "list_data.txt"

def load_list():
    """Reads the text file and loads the items into a Python list."""
    items = []
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                # Read each line and remove any extra invisible spaces/newlines
                items = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
    return items

def save_list(items):
    """Writes the current Python list back to the text file."""
    try:
        with open(FILE_NAME, 'w') as file:
            for item in items:
                file.write(f"{item}\n")
        print("List saved successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def display_list(items):
    """Prints out the current items in the list."""
    print("\n--- Current List ---")
    if not items:
        print("  (The list is empty)")
    else:
        for i, item in enumerate(items):
            # Display numbers starting at 1 instead of 0
            print(f"  {i + 1}. {item}")
    print("--------------------")

def main():
    # Load any existing data from the file when the program starts
    items = load_list()

    while True:
        display_list(items)
        print("\nMenu Options:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Edit Item")
        print("4. Move Item")
        print("5. Save and Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            new_item = input("Enter new item: ")
            if new_item.strip():
                items.append(new_item.strip())
                print(f"'{new_item}' added.")
            else:
                print("Invalid input. Cannot add a blank item.")

        elif choice == '2':
            try:
                # Subtract 1 because Python lists start at index 0
                index = int(input("Enter the number of the item to remove: ")) - 1
                if 0 <= index < len(items):
                    removed = items.pop(index)
                    print(f"'{removed}' removed.")
                else:
                    print("Invalid number. Out of range.")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '3':
            try:
                index = int(input("Enter the number of the item to edit: ")) - 1
                if 0 <= index < len(items):
                    new_val = input(f"Enter the new text for item {index + 1}: ")
                    if new_val.strip():
                        items[index] = new_val.strip()
                        print("Item updated.")
                    else:
                        print("Invalid input. Cannot be blank.")
                else:
                    print("Invalid number. Out of range.")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '4':
            try:
                old_index = int(input("Enter the number of the item to move: ")) - 1
                if 0 <= old_index < len(items):
                    new_index = int(input("Enter its new position number: ")) - 1
                    if 0 <= new_index <= len(items):
                        item_to_move = items.pop(old_index)
                        items.insert(new_index, item_to_move)
                        print("Item moved.")
                    else:
                        print("Target position out of range.")
                else:
                    print("Item number out of range.")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '5':
            save_list(items)
            print("Goodbye!")
            break

        else:
            print("Unknown command. Please select a number from 1 to 5.")

# Run the main program loop
if __name__ == "__main__":
    main()