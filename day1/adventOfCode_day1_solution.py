with open("text.txt","r") as file:
    data=file.read().split()
    list_of_digits=[]
    for i in range(len(data)):
        digit=[item for item in data[i] if item.isdigit()]
        first_and_last_number=digit[0]+digit[-1]
        list_of_digits.append(int(first_and_last_number))
    total=0
    for i in list_of_digits:
        total+=i

    print(total)
