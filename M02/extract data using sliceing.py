word = input()
first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
record = (first, second, third)

middle_word = word[1:-1]
first_two = numbers[:2]
reversed_tuple = record[::-1]

print("Middle:", middle_word)
print("First Two:", first_two)
print("Reversed Tuple:", reversed_tuple)