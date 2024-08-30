class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for idx, contact in enumerate(self.contacts):
                print(f"{idx + 1}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        return results

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            self.contacts[index].update(name, phone, email, address)
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

    def display_contact(self, contact):
        print(contact)


def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
            print("Contact added successfully.")
        
        elif choice == '2':
            manager.view_contacts()
        
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = manager.search_contact(search_term)
            if results:
                for idx, contact in enumerate(results):
                    print(f"{idx + 1}. {contact}")
            else:
                print("No contacts found.")
        
        elif choice == '4':
            manager.view_contacts()
            index = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new name (or press Enter to keep current): ")
            phone = input("Enter new phone number (or press Enter to keep current): ")
            email = input("Enter new email (or press Enter to keep current): ")
            address = input("Enter new address (or press Enter to keep current): ")
            manager.update_contact(index, name, phone, email, address)
        
        elif choice == '5':
            manager.view_contacts()
            index = int(input("Enter the contact number to delete: ")) - 1
            manager.delete_contact(index)
        
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
