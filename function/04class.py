class PhoneBook(object):
    def __init__(self,nm,phone):
        self.name = nm
        self.phone = phone

    def get_phone(self):
        return self.phone

if __name__ == "__main__":
    bob = PhoneBook("bob green","13901234567")
    print(bob.get_phone())
