'''
    Create an application which asks a user for an input for a maths mark, a chemistry mark, and a physics mark.
    Add the marks together, then work out the overall percentage, and print it out to the screen.
    Print the letter grade based on the average mark.
    Percentage below 40%: "You failed"
    40% or higher: "D"
    50% or higher: "C"
    60% or higher: "B"
70% or higher: "A"
'''

marks = {'maths': 0, 'chemistry': 0, 'physics': 0}

print("Welcome to Grade Calculator.")
print("\nPlease enter your maths mark.")
marks['maths'] = int(input())
print("\nPlease enter your chemistry mark.")
marks['chemistry'] = int(input())
print("\nPlease enter your physics mark.")
marks['physics'] = int(input())

marks_sum = sum(marks.values())
marks_average = marks_sum/len(marks)
print(f'Your marks sum is {marks_sum}, for a total of {marks_average}.')

if marks_average >= 70:
    print("You received an A.")
elif marks_average >= 60:
    print("You received a B.")
elif marks_average >= 50:
    print("You received a C.")
elif marks_average >= 40:
    print("You received a D.")
else:
    print("You failed.")