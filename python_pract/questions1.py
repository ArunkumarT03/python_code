'''def print3largest(numbers):
    num = len(numbers)
    if num < 3:
        print("Invalid Input")
        return
    third = first = second = float('-inf')
    for i in range(num):
        if numbers[i] > first:
            third = second
            second = first
            first = numbers[i]
        elif numbers[i] > second and numbers[i] != first:
            third = second
            second = numbers[i]
        
        elif numbers[i] > third and numbers[i] != second and numbers[i] != first:
            third = numbers[i]

    print("Three largest elements are", first, second, third)
numbers = [12, 13, 1, 10, 34, 11, 34]
print3largest(numbers)'''

