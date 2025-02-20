from collections import defaultdict
from statistics import mean

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []  # List of Enrollment objects
        self._grades = {}  # Dictionary of {Enrollment: grade}

    def course_count(self):
        """Returns the number of courses the student is enrolled in."""
        return len(self._enrollments)

    def aggregate_average_grade(self):
        """Calculates the student's average grade across all courses."""
        return mean(self._grades.values()) if self._grades else 0


class Enrollment:
    all = []  # Class attribute to store all enrollments

    def __init__(self, student, course, date):
        self.student = student
        self.course = course
        self.date = date  # Assume date is a datetime object
        Enrollment.all.append(self)

    def get_enrollment_date(self):
        """Returns the date the student was enrolled."""
        return self.date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        """Counts the number of enrollments per day."""
        enrollment_count = defaultdict(int)
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] += 1
        return dict(enrollment_count)
