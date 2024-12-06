# File: hotel_management_system
# Author: Anish Khatri
# Date: 20-11-2024
# Description: Hotel Management System

try:
    from file_management import save_to_file, load_from_file, backup_file
    from room_management import add_room, delete_room, display_rooms
    from room_allocation import allocate_room, display_allocations, billing_and_deallocation

except ImportError as ie:
    print(f"Error: A module could not be imported. {ie}")
    exit(1)

def menu():
    """
    Main menu to run the Hotel Management System.
    """
    try:
        rooms = {}  # Stores room details
        total_rooms = int(input("Enter the total number of rooms in the hotel: "))

        valid_room_numbers = [str(i) for i in range(1, total_rooms + 1)]  # Generate valid room numbers

        while True:
            print("\nHotel Management System")
            print("1. Add Room")
            print("2. Delete Room")
            print("3. Display Rooms Details")
            print("4. Allocate Rooms")
            print("5. Display Room Allocation Details")
            print("6. Billing & De-Allocation")
            print("7. Save Room Allocation to File")
            print("8. Load Room Allocation from File")
            print("9. Backup File")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_room(rooms, valid_room_numbers, total_rooms)
            elif choice == '2':
                delete_room(rooms, valid_room_numbers)
            elif choice == '3':
                display_rooms(rooms)
            elif choice == '4':
                allocate_room(rooms)
            elif choice == '5':
                display_allocations(rooms)
            elif choice == '6':
                billing_and_deallocation(rooms)
            elif choice == '7':
                save_to_file(rooms)
            elif choice == '8':
                load_from_file(rooms)
            elif choice == '9':
                backup_file()
            elif choice == '0':
                print("Exiting application. Goodbye!")
                break
            else:
                raise ValueError("Invalid menu option. Please enter a number between 0 and 9.")

    except NameError as ne:
        print(f"Error: A variable or function is not defined. {ne}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except EOFError as eof:
        print(f"Error: Input ended unexpectedly. {eof}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    menu()
