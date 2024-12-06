import os
import datetime

def save_to_file(rooms, filename="LHMS_850001107.txt"):
    try:
        with open(filename, 'w') as file:
            for room, details in rooms.items():
                file.write(f"{room},{details['type']},{details['price']},{details['status']}\n")
        print(f"Room allocation details saved to {filename}.")
    except IOError as ioe:
        print(f"IOError: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def load_from_file(rooms, filename="LHMS_850001107.txt"):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} does not exist.")
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 4:
                    raise ValueError("Malformed line in file.")
                room_number, room_type, price, status = parts
                rooms[room_number] = {'type': room_type, 'price': float(price), 'status': status}
        print(f"Room data loaded from {filename}.")
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IOError as ioe:
        print(f"IOError: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def backup_file(filename="LHMS_850001107.txt"):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} does not exist.")
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{filename.split('.')[0]}_Backup_{now}.txt"
        with open(filename, 'r') as original, open(backup_filename, 'w') as backup:
            backup.write(original.read())
        print(f"Backup created: {backup_filename}")
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
    except IOError as ioe:
        print(f"IOError: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
