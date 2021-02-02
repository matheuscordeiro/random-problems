#!/usr/local/bin/python3

# Book phone numbers
# Difficulty: Medium

if __name__ == "__main__":
    total_phone = int(input())
    book = {}
    
    for _ in range(total_phone):
        name, phone = input().split()
        book[name] = phone
        
    while True:
        try:
            name = input()
            print(name)
            if book.get(name):
                print(f"{name}={book[name]}")
            else:
                print("Not found")
        except EOFError:
            break
