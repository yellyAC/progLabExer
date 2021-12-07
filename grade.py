print("Exam Grade 1: ")
grade1 = int(input())
print("Exam Grade 2: ")
grade2 = int(input())
print("Exam Grade 3: ")
grade3 = int(input())
print("Exam Grade 4: ")
grade4 = int(input())


sum = grade1+grade2+grade3+grade3+grade4
avg = sum/4

if avg>=60:
    print("PASSED!")
elif avg<60:
    print("FAILED!")
print("Your Average is " + str(avg))