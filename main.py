from v2_student_grader_pkg.database import init_db,insert_grades,insert_student,fetch_student_grades,get_student_name,update_student_name,delete_student,update_grades

import os 
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
def main():
	init_db()
	while True:
		print("\n=================================" \
		"========================================")
		print("========== STUDENT GARDER V2: \
		DASHBOARD ==========")
		print("1. Add New Student and Marks ")
		print("2. Generate Student Report Card (Search by ID or Student id)")
		print("3. Update Student Name")
		print("4. Delete Student Name")
		print("5. Update Grades Using Student ID")
		print("6. EXIT")
		print("=============================================" \
		"===================================")
		Choice = input("Enter Your Choice (1-6): ").strip()
		if Choice == "1":
			try:
				name = input("Enter your Name: ")
				insert_student(name)
				student_id = int(input("Enter Student ID: "))
			except ValueError:
				print("Invalid input. Please enter a valid student ID.")
				continue
			
			while True:
				try:
					print("\n--- Enter Marks (0-100) ---")
					Physics = int(input("Physics: "))
					chemistry = int(input("Chemistry: "))
					Maths = int(input("Maths : "))
					if not(0<= Physics <= 100 and 0<= chemistry <= 100 and 0<= Maths <=100):
						print("Please Enter Marks in the range of Marks")
						continue
					insert_grades(student_id,"Physics","Marks",Physics)
					insert_grades(student_id,"Chemistry","Marks",chemistry)
					insert_grades(student_id,"Maths","Marks",Maths)
					print(f"\nAll grades locked successfully for Student id {student_id}!")
					break
				except ValueError:
					print("Invalid input. Please enter numeric marks between 0 and 100.")
		
		elif Choice == "2":
			try:
				search_id = int(input("\nEnter Student ID to View Report Card: "))
				records = fetch_student_grades(search_id)
				if not records:
					print(f"Searched ID: {search_id} isn't Availabe Please check the student id and 'try again' ")
					continue
				get_name = get_student_name(search_id)
				print(f"\n=============== GENERATING REPORTS CARD FOR ID: {search_id} ===================")
				print(f"Student ID: {search_id}")
				print(f"Student Name: {get_name}")
				total_marks = 0
				subject_count = len(records)
				for row in records:
					subject_name = row[0]
					marks = row[1]
					print(f"{subject_name}:{marks}/100")
					total_marks += marks
				print("=========================================" \
				"===========================================")
				average_marks = total_marks / subject_count if subject_count > 0 else 0
				if average_marks>= 90:
					final_grade = "A"
				elif average_marks>= 75:
					final_grade = "B"
				elif average_marks>= 50:
					final_grade = "C"
				else:
					final_grade = "F"
				print(f"Total Marks Obtained: {total_marks}/{subject_count*100}")
				print(f"Average Marks: {average_marks:.2f}")
				print(f"Final Status Grade: [GRADE: {final_grade}]")
				if final_grade == "F":
					print("YOU FAILED IN EXAMS, TRY AGAIN")
				else:
					print("CONGRATS BUDDY!")
				print("===================================================")
			except ValueError:
				print("Invalid input. Please enter a numeric student ID.")
		
		elif Choice == "3":
			try:
				stu_id = int(input("Enter student ID: "))
				new_name = input("Enter the new name: ")
				updated = update_student_name(stu_id,new_name)
				if updated:
					print(f"Student '{stu_id}' name UPDATED to '{new_name}' ")
				else:
					print(f"Student ID: {stu_id} not Found!!, Try again")

			except ValueError:
				print("Invalid Input! Student ID must be a Number")
		
		elif Choice == "4":
			try:
				student_id = int(input("Enter student ID: "))
				result = delete_student(student_id)
				if result:
					print(f"Student Deleted Successfully")
				else:
					print(f"Student ID: {student_id} not Found!")
			except ValueError:
				print("Invalid Input! Student ID must be a Number")
		elif Choice == "5":
			try:
				student_id = int(input("Enter student ID: "))
				subject = input("Enter Subject: ")
				marks = int(input("Enter Marks(0-100): "))
				result = update_grades(student_id, subject, marks)
				if result:
					print(f"Graded Updated!")
				else:
					print(f"Failed to Update Grades!")
			except ValueError:
				print("Invalid Input! Student ID must be a Number")
		elif Choice == "6":
			print("Goodbye!, Thankyou for using Our Tool")
			break
		else:
			print("Invalid Choice")
if __name__ == "__main__":
	main()
	
		
		
			