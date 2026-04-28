import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Generate ID
def generate_id(contacts):
    return max([c["id"] for c in contacts], default=0) + 1

# Add contact
def add_contact(contacts):
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        city = input("Enter City: ")
        company = input("Enter Company: ")

        if not name or not phone or not email:
            print("❌ Fields cannot be empty")
            return

        contact = {
            "id": generate_id(contacts),
            "name": name,
            "phone": phone,
            "email": email,
            "city": city,
            "company": company
        }

        contacts.append(contact)
        save_contacts(contacts)
        print("✅ Contact added!")

    except Exception as e:
        print("Error:", e)

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found")
        return

    print("\nID | Name | Phone | Email | City | Company")
    print("-" * 60)
    for c in contacts:
        print(f'{c["id"]} | {c["name"]} | {c["phone"]} | {c["email"]} | {c["city"]} | {c["company"]}')

# Search contact
def search_contacts(contacts):
    keyword = input("Enter search keyword: ").lower()

    results = [c for c in contacts if keyword in c["name"].lower()
               or keyword in c["phone"]
               or keyword in c["email"].lower()]

    view_contacts(results)

# Filter contacts
def filter_contacts(contacts):
    choice = input("Filter by (1) City (2) Company: ")

    if choice == "1":
        city = input("Enter city: ").lower()
        results = [c for c in contacts if c["city"].lower() == city]
    else:
        company = input("Enter company: ").lower()
        results = [c for c in contacts if c["company"].lower() == company]

    view_contacts(results)

# Update contact
def update_contact(contacts):
    try:
        cid = int(input("Enter contact ID: "))
        for c in contacts:
            if c["id"] == cid:
                c["name"] = input("New Name: ") or c["name"]
                c["phone"] = input("New Phone: ") or c["phone"]
                c["email"] = input("New Email: ") or c["email"]
                c["city"] = input("New City: ") or c["city"]
                c["company"] = input("New Company: ") or c["company"]

                save_contacts(contacts)
                print("✅ Updated!")
                return

        print("❌ Contact not found")

    except:
        print("Invalid input")

# Delete contact
def delete_contact(contacts):
    try:
        cid = int(input("Enter contact ID: "))
        contacts[:] = [c for c in contacts if c["id"] != cid]
        save_contacts(contacts)
        print("🗑 Deleted!")

    except:
        print("Invalid input")

# Menu
def menu():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search")
        print("4. Filter")
        print("5. Update")
        print("6. Delete")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            filter_contacts(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            delete_contact(contacts)
        elif choice == "7":
            break
        else:
            print("Invalid choice")

menu()