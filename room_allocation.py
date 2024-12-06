def allocate_room(rooms):
    """
    Allocates a room to a customer.
    """
    room_number = input("Enter room number to allocate: ")
    if room_number in rooms and rooms[room_number]['status'].lower() == 'available':
        customer_name = input("Enter customer name: ")
        rooms[room_number]['status'] = f"Allocated to {customer_name}"
        print(f"Room {room_number} allocated to {customer_name}.")
    else:
        print("Error: Room is not available or does not exist.")

def display_allocations(rooms):
    """
    Displays room allocation details.
    """
    for room, details in rooms.items():
        print(f"Room {room}: {details['status']}")

def billing_and_deallocation(rooms):
    """
    Handles billing and deallocates a room.
    """
    room_number = input("Enter room number to deallocate: ")
    if room_number in rooms and 'Allocated' in rooms[room_number]['status']:
        customer = rooms[room_number]['status'].split("to")[1].strip()
        print(f"Billing customer {customer} for Room {room_number}.")
        rooms[room_number]['status'] = 'Available'
        print(f"Room {room_number} is now available.")
    else:
        print("Error: Room is not allocated or does not exist.")
