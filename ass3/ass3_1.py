#6809658138
def get_funny_average(numbers):
    numbers = [i for i in numbers if i > 0]
    numbers = [ n for n in numbers if n != min(numbers) and n != max(numbers) and n > 0 ]
    
    if not numbers:
        return 0
    else :
        avg = sum(numbers) / len(numbers)
        return round(avg, 1)

print("1. Funny average: ", get_funny_average([ 3, 2, 0, 25, 1]))
print("2. Funny average: ", get_funny_average([-6, -32, 2, 0, -51, 1, 0, 0]))
print("3. Funny average: ", get_funny_average([56, 32, 2, 22, 22]))
print("4. Funny average: ", get_funny_average([-56, -3, 0, -21, 0, 0, 5]))
print("5. Funny average: ", get_funny_average([56, 3, 2, 0, 251, 1, 41, 22]))
print("6. Funny average: ", get_funny_average([-56, -3, 2, 0, -251, 1, -41, 0]))
print("7. Funny average: ", get_funny_average([]))








