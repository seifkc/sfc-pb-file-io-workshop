import json

"""
Note: This is designed to hold a list of contacts as a list of dictionaries.
An alternative approach is to build a "Contact" class to represent a contact.
If you would like to do that as a Bonus exercise, that would be good way
to practice using OOP and composition!
"""

import json




class ContactManager:
    """Class to do CRUD operations on the list of contacts"""

    def __init__(self, file="data.json"):
        self.file = file
        self.contacts = []
    def load_contacts(self):
        try: #follows this
            with open(self.file, "r") as new:
                self.contacts = json.load(new)
        except: (FileNotFoundError, json.JSONDecodeError): #if it doesn't work and gives errors listed
                self.contacts = [] #set an empty list, just in case its corrupt or pulled and saved from previous "try"
                Print (f"File {self.file} is corrupt or doesn't exist.")
            return self.contacts




        """Loads contacts from a JSON file and converts them to a list of
        dictionaries

        Bonus: What should happen if the file isn't there?
                What should happen if the file has invalid JSON in it?

        """


    def add_contact(self, ):
        self.contacts.append(contact)
        with open(self.file, "w") as new:
            json.dump(self.contacts, new, indent =4) #makes it look neat like pokemon api


    def update_contact(self, contact_to_update):
        for contact in self.contacts:
            if contact["id"] == contact_to_update["id"]:
            self.contacts[i] = contact_to_update
            with open(self.file, "w") as new:
                json.dump(self.contacts, new, indent= 4)
            return

        print (f"No contact found with ID {contact_to_update['id']}.")

    def delete_contact(self, id_to_delete):
        for contact in self.contacts:
            if contact["id"] == id_to_delete:
                self.contacts.remove(contact)
                with open(self.files, "w") as new:
                    json.dump(self.contacts, new, indent=4)
                return
            print(f"No contact with ID {id_to_delete}.")


