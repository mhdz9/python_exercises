import sqlite3

class School:

    def contact_db(self, query, query_input):
        conn = sqlite3.connect('C:\Users\mtrevino\Desktop\db_Exercise\school.db')
        conn.text_factory = str
        with conn:
            c = conn.cursor()
            c.execute(query, query_input)
            return c.fetchall()

    def get_all_students(self):
        "Returns list of all students with their courses Description"
        query = 'SELECT students.first_name, students.last_name, courses.description' \
                'FROM students, courses, student_courses' \
                'WHERE students.id = student_courses.student_id' \
                'AND courses.id = student_courses.course_id'
        query_input = ()
        return self.contact_db(query, query_input)

    def add_new_student(self):
        id = raw_input("Enter student id\n")
        first_name = raw_input("Enter first name\n")
        last_name = raw_input("Enter last name\n")
        dob = raw_input("Enter date of birth\n")
        teacher_id = raw_input("Enter teacher id\n")
        query = 'INSERT INTO students VALUES (?,?,?,?,?)'
        query_input = (id,first_name,last_name,dob,teacher_id)
        return self.contact_db(query, query_input)

student1 = School()
student1.add_new_student()
student1.get_all_students()