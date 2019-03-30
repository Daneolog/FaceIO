class Customer:
    def __init__(self, face):
        self.face = face;
        self.interests = []

    def add_interest(self, new_interest):
        self.interests.append(new_interest)
