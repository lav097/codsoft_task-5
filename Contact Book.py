class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        for contact in self.contacts:
            if contact.name == search_term or contact.phone == search_term:
                return contact
        return None

    def update_contact(self, search_term, new_contact):
        for idx, contact in enumerate(self.contacts):
            if contact.name == search_term or contact.phone == search_term:
                self.contacts[idx] = new_contact
                return True
        return False

    def delete_contact(self, search_term):
        for idx, contact in enumerate(self.contacts):
            if contact.name == search_term or contact.phone == search_term:
                del self.contacts[idx]
                return True
        return False
def add_contact_ui(contact_manager):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(name, phone, email, address)
    contact_manager.add_contact(contact)
    print("Contact added successfully.")

def view_contacts_ui(contact_manager):
    contact_manager.view_contacts()

def search_contact_ui(contact_manager):
    search_term = input("Enter name or phone number to search: ")
    contact = contact_manager.search_contact(search_term)
    if contact:
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
    else:
        print("Contact not found.")

def update_contact_ui(contact_manager):
    search_term = input("Enter name or phone number to update: ")
    name = input("Enter new name: ")
    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")
    address = input("Enter new address: ")
    new_contact = Contact(name, phone, email, address)
    if contact_manager.update_contact(search_term, new_contact):
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact_ui(contact_manager):
    search_term = input("Enter name or phone number to delete: ")
    if contact_manager.delete_contact(search_term):
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contact_manager = ContactManager()
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact_ui(contact_manager)
        elif choice == '2':
            view_contacts_ui(contact_manager)
        elif choice == '3':
            search_contact_ui(contact_manager)
        elif choice == '4':
            update_contact_ui(contact_manager)
        elif choice == '5':
            delete_contact_ui(contact_manager)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
