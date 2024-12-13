def validMarks(marks):
    valid_marks = []
    for mark in (marks):
         if mark != 'AB':
             valid_marks.append(mark)
    return valid_marks;

def enterval(n):
    marks = []
    for _ in range(n):
      
            m = input("Enter marks of student, enter 'AB' if absent: ").strip().upper()
            marks.append(m)
            
    print(marks)
    return marks
  
  
    
def avg(marks):
    total_marks = 0
    count = 0
    
    for index, mark in enumerate(marks):
        if mark != 'AB':
            total_marks += int(mark)
            count += 1   
    avg = total_marks / count
    print("Average marks:", avg)
    
    

def score(marks):
    valid_marks = validMarks(marks)
             
    high = max(valid_marks)
    low = min(valid_marks)
    print("Highest Score:", high)
    print("Lowest Score:", low)
    

def abst(marks):
    abst_count = 0
    for mark in (marks):
         if mark == 'AB':
             abst_count += 1
    print("Total Absent Students Are:", abst_count)



def highfreq(marks):
     freq = {}
    for mark in marks:
        if isinstance(mark, int):
            freq[mark] = freq.get(mark, 0) + 1

    if freq:
        most_frequent_mark = max(freq, key=freq.get)
        print(f"Mark with highest frequency is {most_frequent_mark}.")
    else:
        print("No valid scores to determine frequency.")
    print())    
    
        
    

def main():
    n = int(input("Enter number of students: "))
    marks = enterval(n)
    
    while True:
        print("\nChoose an option:")
        print("1. Average score of class")
        print("2. Highest and lowest score of class")
        print("3. Number of absent students")
        print("4. Mark with highest frequency")
        
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                avg(marks)
            elif choice == 2:
                score(marks)
            elif choice == 3:
                abst(marks)
            elif choice == 4:
                highfreq(marks)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
