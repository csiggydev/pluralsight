# This while loop says - while the response variable equaling user input method is true - perform the if loop until break

while True:
    response = input()
    if int(response) % 7 == 0:
        break