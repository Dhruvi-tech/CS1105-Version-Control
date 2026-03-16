data = input("Enter data packet: ")

if data == data[::-1]:
    print("Data integrity verified")
else:
    print("Data corrupted")