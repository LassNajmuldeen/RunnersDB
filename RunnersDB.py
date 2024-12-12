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
        registrations = load_json("registrations.json")
        results = load_json("results.json")
        race_number = input("Enter race number: ").strip()
        participant = registrations.get(race_number)
        if participant:
            print(f"Name: {participant['name']}, City: {participant['city']}")
        else:
            print("No participant found with this race number.")
    except Exception as e:
        print(f"Error during lookup: {e}")