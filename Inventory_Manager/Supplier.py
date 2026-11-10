# Represents information about supplier
class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.supplier_id: str = supplier_id
        self.name: str = name
        self.contact_email: str = contact_email

    def display_information(self):
        print("ID:", self.supplier_id)
        print("Name:", self.name)
        print("Email:", self.contact_email)