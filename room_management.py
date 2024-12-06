def add_room(rooms, valid_room_numbers, total_rooms):
    try:
        if len(rooms) >= total_rooms:
            raise OverflowError(f"Cannot add more rooms. The hotel already has the maximum of {total_rooms} rooms.")
        
        print(f"Available room numbers: {', '.join(valid_room_numbers)}")
        room_number = input("Enter room number to add (from available numbers): ")

        if room_number not in valid_room_numbers:
            raise ValueError(f"Room number {room_number} is not valid.")
        
        if room_number in rooms:
            raise ValueError(f"Room {room_number} already exists.")

        room_type = input("Enter room type (Standard/Deluxe/Suite): ")
        price = float(input("Enter room price per night: $"))
        if price <= 0:
            raise ValueError("Price must be a positive number.")

        rooms[room_number] = {'type': room_type, 'price': price, 'status': 'Available'}
        valid_room_numbers.remove(room_number)
        print(f"Room {room_number} added successfully.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except OverflowError as oe:
        print(f"OverflowError: {oe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def delete_room(rooms, valid_room_numbers):
    try:
        room_number = input("Enter room number to delete: ")

        if room_number not in rooms:
            raise ValueError(f"Room {room_number} does not exist.")

        del rooms[room_number]
        valid_room_numbers.append(room_number)
        valid_room_numbers.sort()
        print(f"Room {room_number} deleted successfully.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def display_rooms(rooms):
    try:
        if not rooms:
            raise ValueError("No rooms available to display.")
        for room, details in rooms.items():
            print(f"Room {room}: Type: {details['type']}, Price: ${details['price']}, Status: {details['status']}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
