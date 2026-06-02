alerts = []

def report_emergency():
    emergency_type = input("Enter emergency type: ")
    location = input("Enter location: ")
    description = input("Enter short description: ")

    alert = {
        "type": emergency_type,
        "location": location,
        "description": description
    }

    alerts.append(alert)
    print("\nEmergency alert reported successfully!\n")


def view_alerts():
    if not alerts:
        print("\nNo alerts reported yet.\n")
        return

    print("\n--- All Emergency Alerts ---")
    for i, alert in enumerate(alerts, start=1):
        print(f"\nAlert {i}")
        print(f"Type: {alert['type']}")
        print(f"Location: {alert['location']}")
        print(f"Description: {alert['description']}")


def search_alert():
    search_location = input("Enter location to search: ").lower()
    found = False

    for alert in alerts:
        if search_location in alert["location"].lower():
            print("\nAlert Found:")
            print(f"Type: {alert['type']}")
            print(f"Location: {alert['location']}")
            print(f"Description: {alert['description']}")
            found = True

    if not found:
        print("\nNo alert found for this location.\n")


def safety_tips():
    print("\n--- Safety Tips ---")
    print("Accident: Call ambulance and avoid crowding the road.")
    print("Landslide: Avoid travelling through risky hill roads during heavy rain.")
    print("Flood: Move to higher ground immediately.")
    print("Fire: Stay low, avoid smoke, and call fire brigade.")
    print("Earthquake: Drop, Cover, and Hold.")


while True:
    print("\n===== Suraksha Alert Nepal =====")
    print("1. Report Emergency")
    print("2. View All Alerts")
    print("3. Search Alert by Location")
    print("4. Show Safety Tips")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        report_emergency()
    elif choice == "2":
        view_alerts()
    elif choice == "3":
        search_alert()
    elif choice == "4":
        safety_tips()
    elif choice == "5":
        print("Thank you for using Suraksha Alert Nepal.")
        break
    else:
        print("Invalid choice. Please try again.")