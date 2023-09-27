import mysql.connector

# Connect to MySQL
connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="312776",
        database="samta"
    )

    cursor = connection.cursor()

    # Create the "students" table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
    """
    cursor.execute(create_table_query)

    #Insert a new student record
    insert_query = """
    INSERT INTO students (first_name, last_name, age, grade)
    VALUES (%s, %s, %s, %s)
    """
    student_data = ("Bhaskar", "Sharma", 20, 91.5)
    cursor.execute(insert_query, student_data)
    connection.commit()
    print("Inserted a new student record.")

    #Update the grade of the student with the first name "Alice"
    update_query = """
    UPDATE students
    SET grade = %s
    WHERE first_name = %s
    """
    updated_grade = 97.0
    cursor.execute(update_query, (updated_grade, "Alice"))
    connection.commit()
    print("Updated the grade for Alice.")

    # Delete the student with the last name "Smith"
    delete_query = """
    DELETE FROM students
    WHERE last_name = %s
    """
    cursor.execute(delete_query, ("Smith",))
    connection.commit()
    print("Deleted student with last name Smith.")

    # Fetch and display all student records
    select_query = "SELECT * FROM students"
    cursor.execute(select_query)
    students = cursor.fetchall()

    print("\nAll Student Records:")
    for student in students:
        print(f"Student ID: {student[0]}")
        print(f"First Name: {student[1]}")
        print(f"Last Name: {student[2]}")
        print(f"Age: {student[3]}")
        print(f"Grade: {student[4]}")
        print()

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    if connection:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
        else:
            print("Connection was not established.")
