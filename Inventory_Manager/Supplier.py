# Represents information about supplier
class Supplier():
    def __init__(self, supplier_id, name, contact_email):
        self._supplier_id = supplier_id
        self._name = name
        self._contact_email = contact_email

    def get_id(self):
        return self._supplier_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._contact_email

    def display_information(self):
        print("ID:", self._supplier_id)
        print("Name:", self._name)
        print("Email:", self._contact_email)