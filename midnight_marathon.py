import json

# Load JSON data from a file
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return []

# Lookup a registration by race number
def lookup_registration(registrations):
    try:
        race_number = int(input("Enter race number: ").strip())
        participant = next((p for p in registrations if p["number"] == race_number), None)
        if participant:
            print(f"Name: {participant['name']}, City: {participant['city']}")
        else:
            print("No participant found with this race number.")
    except ValueError:
        print("Invalid input. Please enter a numeric race number.")

# List results based on a time filter
def list_results(registrations, results):
    try:
        time_limit = int(input("Enter time limit (seconds): ").strip())
        filtered_results = [r for r in results if r["time"] < time_limit]

        if not filtered_results:
            print("ERROR: please select a value greater than the fastest time (1213 sec)")
            return

        print("\nParticipants with faster times:")
        print("Number | Time (s) | Name                 | City")
        print("-" * 50)
        for result in filtered_results:
            participant = next((p for p in registrations if p["number"] == result["number"]), None)
            if participant:
                print(f"{result['number']:>6} | {result['time']:>8} | {participant['name']:<20} | {participant['city']}")
    except ValueError:
        print("Invalid input. Please enter a numeric time value.")

# Main menu
def main():
    registrations = load_json("registrations.json")
    results = load_json("results.json")

    if not registrations or not results:
        print("Failed to load necessary data. Exiting.")
        return

    while True:
        print("\n RunnersDB ")
        print("1. Lookup Registration")
        print("2. List Results")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            lookup_registration(registrations)
        elif choice == "2":
            list_results(registrations, results)
        else:
            print("Invalid choice. Please try again.")

main()
