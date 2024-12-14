# Write a Python program to store marks scored in subject “Fundamental of Data 
# Structure” by
# N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

def avg(marks):
    total = 0
    student_count = 0
    
    for mark in marks:
        if mark != 'AB':
            total = total + int(mark)
            student_count += 1
            
    avg = total / student_count       
    print(avg)



def high_low(marks):
    valid_marks = []
    for mark in marks:
        if mark != 'AB':
            valid_marks.append(int(mark))
    
    high = max(valid_marks)
    low = min(valid_marks)
    print(f"\nHighest Score is {high} and Lowest Score is {low}")
    
    
    
def abs_count(marks):
    count = 0
    for mark in marks:
        if mark == 'AB':
            count += 1 
    
    print("\nTotal Absent Students Are : ", count)


def freq(marks):
    valid_marks = []
    for mark in marks:
        if mark != 'AB':
            valid_marks.append(int(mark))
            
    freq_dic = {mark: valid_marks.count(mark)for mark in valid_marks}
    print("Highest Frequency : ",max(freq_dic, key=freq_dic.get))
        

marks = []
n = int(input("Enter Number of Students in Class: "))
    
for i in range(n):
    mark = input(f"\nEnter mark of student {i+1}: Enter AB if absent: ").upper()
    marks.append(mark)
        

while True:
    print("\nChoose an option")
    print("\n1 - Average score of class")
    print("\n2 - Highest and lowest score")
    print("\n3 - Absent Count")
    print("\n4 - Highest frequency")
    
    
    choice = int(input("\nEnter Your choice: "))
    
    if choice == 1:
        avg(marks)
        
    elif choice == 2:
        high_low(marks)
        
    elif choice == 3:
        abs_count(marks)
        
    elif choice == 4:
        freq(marks)
        
    else:
        print("\nInvalid Choice")
    
   
        
    
    
    


