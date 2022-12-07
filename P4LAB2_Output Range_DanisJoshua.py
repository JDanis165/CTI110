first = int(input())
second = int(input())
if first > second:   
    print("Second integer can't be less than the first.")
else:
    while first <= second:
        print(first, end=" ")
        first += 5
    print()