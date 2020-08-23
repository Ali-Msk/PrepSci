class Student():
    name = ""
    age = 0
    grade = 0
    program = ""
    rating = 0
    ratingCount = 0
    comments = []
    comments = []
    city = ""
def __init__(self, name):
        self.name = name

    def addRating(self, rating):
        self.ratingCount += 1
        self.rating = (rating + self.rating * (ratingCount - 1)) / ratingCount

