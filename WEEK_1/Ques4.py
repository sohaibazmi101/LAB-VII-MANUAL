numbers = [1,2,3,4,5,6,7,8,9,10]
squared_numbers = list(map(lambda x: x**2, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Squared Numbers: ", squared_numbers)
print("Odd Numbers: ", odd_numbers)