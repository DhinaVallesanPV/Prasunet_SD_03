import json
import os

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")

        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            print(f"Contact for {name} added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("\nContacts List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print("No contacts found.")

    def edit_contact(self):
        name = input("Enter the name of the contact to edit: ")
        if name in self.contacts:
            print(f"Current details: Phone: {self.contacts[name]['phone']}, Email: {self.contacts[name]['email']}")
            new_phone = input("Enter new phone number (or press Enter to keep current): ")
            new_email = input("Enter new email address (or press Enter to keep current): ")
            if new_phone:
                self.contacts[name]['phone'] = new_phone
            if new_email:
                self.contacts[name]['email'] = new_email
            print(f"Contact for {name} updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} deleted successfully.")
        else:
            print("Contact not found.")

    def run(self):
        while True:
            print("\n--- Contact Management ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Edit Contact")
            print("4. Delete Contact")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.edit_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                self.save_contacts()
                print("Contacts saved. Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.run()