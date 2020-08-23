class Tutor():
    name = ""
    age = 0
    grade = 0
    degrees = []
    isStudent = None
    rating = 0
    ratingCount = 0
    comments  = []
    city = ""
    location = []
    subjects = []
    maxGradeToTeach = 0
    minGradeToTeach = 0
    def __init__(self, name):
        self.name = name

    def addRating(self, rating):
        self.ratingCount += 1
        self.rating = (rating + self.rating * (ratingCount - 1)) / ratingCount