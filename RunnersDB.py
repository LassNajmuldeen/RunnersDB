import json

# Load JSON data from files
def load_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return {}

# Lookup registration by race number
def lookup_registration():
    try:
        race_number = input("Enter race number: ").strip()
        participant = registrations.get(race_number)
        if participant:
            print(f"Name: {participant['name']}, City: {participant['city']}")
        else:
            print("No participant found with this race number.")
    except Exception as e:
        print(f"Error during lookup: {e}")

# List results faster than a given time
def list_results():
    try:
        time_limit = float(input("Enter time limit (hours): ").strip())
        print("Participants with faster times:")
        print("Number | Time | Name | City")
        print("-" * 40)
        for race_number, result in results.items():
            time = float(result['time'])
            if time < time_limit:
                participant = registrations.get(race_number)
                if participant:
                    print(f"{race_number} | {time:.2f} | {participant['name']} | {participant['city']}")
    except ValueError:
        print("Invalid time input. Please enter a numeric value.")
    except Exception as e:
        print(f"Error during results listing: {e}")

registrations = load_json("registrations.json")
results = load_json("results.json")

# Main menu
def main():
    while True:
        print("\n.: Midnight Marathon :.")
        print("1. Lookup Registration")
        print("2. List Results")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

main()