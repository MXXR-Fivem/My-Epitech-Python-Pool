inputName = str(input("What is your name ? "))
temp = inputName[0].upper()
inputName = temp + inputName[1:]
print(f"Hello {inputName}!")