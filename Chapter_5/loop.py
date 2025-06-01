marks_tuple = ()

print(marks_tuple,  "Before enter <-")

for a in range(5):
    marks = int(input(f"Enter marks for the {a} student : "))
    marks_tuple = marks_tuple + (marks,)
    
print(marks_tuple , " <- After enter ")    
    