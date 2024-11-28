class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. {contact}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            print("Search Results:")
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index].name = name
            if phone:
                self.contacts[index].phone = phone
            if email:
                self.contacts[index].email = email
            if address:
                self.contacts[index].address = address
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == '4':
            contact_book.view_contacts()
            try:
                index = int(input("Enter the contact number to update: ")) - 1
                name = input("Enter new name (leave blank to keep current): ")
                phone = input("Enter new phone number (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                address = input("Enter new address (leave blank to keep current): ")
                contact_book.update_contact(index, name if name else None, phone if phone else None, email if email else None, address if address else None)
            except ValueError:
                print("Invalid input. Please enter a valid contact number.")

        elif choice == '5':
            contact_book.view_contacts()
            try:
                index = int(input("Enter the contact number to delete: ")) - 1
                contact_book.delete_contact(index)
            except ValueError:
                print("Invalid input. Please enter a valid contact number.")

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
