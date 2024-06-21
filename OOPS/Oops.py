'''
Problem 1: Library Management System
Create a Book class and a Library class to manage a collection of books.

Requirements:
Book class should have attributes: title, author, and ISBN.
Library class should have methods to:
Add a book.
Remove a book by ISBN.
Search for a book by title.
Display all books in the library.
'''
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN '{isbn}' removed from the library.")
                return
        print(f"No book found with ISBN '{isbn}'.")

    def display_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

# Example usage
if __name__ == "__main__":
    library = Library()
    
    book = Book("Half Girlfriend", "Chetan Bhagat", "9876543210")
    book1 = Book("Five Point Someone", "Chetan Bhagat", "321654987")
    book2 = Book("One Night @ the Call Center", "Chetan Bhagat", "789456123")
    
    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)
    
    library.display_books()
    
    print("\nRemoving book with ISBN '321654987':")
    library.remove_book("321654987")
    
    library.display_books()


'''
Problem 2: Student Grades Management
Create a Student class and a Course class to manage students and their grades.

Requirements:
Student class should have attributes: name, student_id, and a dictionary to 
store course names and grades.
Course class should have attributes: course_name and instructor.
Implement methods to:
Add a course to a student's record.
Remove a course from a student's record.
Calculate the student's average grade.
'''
class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor

    def __str__(self):
        return f"Course Name: {self.course_name}, Instructor: {self.instructor}"

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}  # Dictionary to store course names and grades

    def add_course(self, course, grade):
        self.courses[course.course_name] = grade
        print(f"Added course '{course.course_name}' with grade {grade} to student '{self.name}'.")

    def remove_course(self, course_name):
        if course_name in self.courses:
            del self.courses[course_name]
            print(f"Removed course '{course_name}' from student '{self.name}'.")
        else:
            print(f"Course '{course_name}' not found in student '{self.name}' records.")

    def calculate_average_grade(self):
        if not self.courses:
            print(f"No courses for student '{self.name}' to calculate average grade.")
            return 0.0
        total_grades = sum(self.courses.values())
        average_grade = total_grades / len(self.courses)
        return average_grade

    def __str__(self):
        courses_str = ', '.join([f"{course}: {grade}" for course, grade in self.courses.items()])
        return f"Student Name: {self.name}, Student ID: {self.student_id}, Courses: [{courses_str}]"

# Example usage
if __name__ == "__main__":
    # Create courses
    course1 = Course("Mathematics", "Dr. Smith")
    course2 = Course("Physics", "Dr. Johnson")
    course3 = Course("Chemistry", "Dr. Brown")

    # Create a student
    student = Student("John Doe", "S12345")
    
    # Add courses to the student's record
    student.add_course(course1, 85)
    student.add_course(course2, 90)
    student.add_course(course3, 78)
    
    # Print student details
    print(student)

    # Calculate and print the student's average grade
    average_grade = student.calculate_average_grade()
    print(f"Average Grade for {student.name}: {average_grade:.2f}")

    # Remove a course from the student's record
    student.remove_course("Physics")
    
    # Print student details after removal
    print(student)

    # Calculate and print the student's average grade after removal
    average_grade = student.calculate_average_grade()
    print(f"Average Grade for {student.name} after removal: {average_grade:.2f}")

