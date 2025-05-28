#Contact Management System in Python

contacts = []

# Add Contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully.\n")

# View All Contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

# Search Contact by Name or Phone
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("No matching contact found.\n")

# Update Contact
def update_contact():
    search_term = input("Enter name of contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == search_term.lower():
            print("Leave blank to keep existing value.")
            contact["name"] = input(f"New name ({contact['name']}): ") or contact["name"]
            contact["phone"] = input(f"New phone ({contact['phone']}): ") or contact["phone"]
            contact["email"] = input(f"New email ({contact['email']}): ") or contact["email"]
            contact["address"] = input(f"New address ({contact['address']}): ") or contact["address"]
            print("Contact updated successfully.\n")
            return
    print("Contact not found.\n")

# Delete Contact
def delete_contact():
    search_term = input("Enter name of contact to delete: ")
    for contact in contacts:
        if contact["name"].lower() == search_term.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.\n")
            return
    print("Contact not found.\n")

# Main Menu
def menu():
    while True:
        print("=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
