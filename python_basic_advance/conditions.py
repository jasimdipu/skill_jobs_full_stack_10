# if | elif | else

if 100 < 10:
    print("True")
else:
    print("False")

# elif
# if else ladder
if 100 < 10:
    print("First Condition is True")
elif 100 < 20:
    print("Second Condition is True")
elif 100 > 40:
    print("Third Condition is True")
else:
    print("No one is True")

# nested condition
if 100 > 10:
    print("Outter condition is True")
    if 100 < 110:
        print("Inner Condition is True")
    else:
        print("Inner condition is False")
else:
    print("Outter condition is False")
