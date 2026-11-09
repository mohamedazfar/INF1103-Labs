# Represents information about supplier
class Supplier():
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self._supplier_id: str = supplier_id
        self._name: str = name
        self._contact_email: str = contact_email

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