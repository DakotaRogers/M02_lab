# M02_lab
# this app finds students names and will determine wether they are eligible for the honor roll or for the dean's list


last_name = input("Enter the student's last name OR enter 'ZZZ' to end task: ")

if last_name == 'ZZZ':
    print("The application will close now.")
    quit()
else:
    first_name = input("Enter the student's first name: ")

GPA = float(input("Enter the student's GPA: "))

if GPA >= 3.5:
    print("Congratulations! " + first_name,
          last_name + " has made the Dean's List!")

else:
    if GPA >= 3.25:
        print("Congratulations! " + first_name,
              last_name + " has made the Honor Roll!")
