
def clean(item):
    c_1=item.replace(";","")
    c_2=c_1.replace(",","")
    return c_2

def check(color,lim):
    for num in color:
        if int(num)<=lim:
            ANSWER=True
        else:
            ANSWER=False
            break
    return ANSWER


def tot(li):
    tot=0
    for num in li:
        tot+=num
    return tot

satisfied_games=[]
power_list=[]
with open("text.txt","r") as file:
    data=file.readlines()

    for item in data:

        item_list=[clean(item) for item in item.split()]
        #blue
        blue=[ ]
        i=0
        for elem in item_list :
            if elem=="blue":
                blue.append(int(item_list[i-1]))
                i+=1
            else:
                i+=1


        #red
        red = []
        j = 0
        for elem in item_list:
            if elem == "red":
                red.append(int(item_list[j - 1]))
                j += 1
            else:
                j += 1

        #green
        green = []
        k = 0
        for elem in item_list:
            if elem == "green":
                green.append(int(item_list[k - 1]))
                k += 1
            else:
                k += 1

        max_blue = max(blue)
        max_red = max(red)
        max_green = max(green)
        power_list.append(max_red * max_blue * max_green)

        if check(blue,14) and check(green,13) and check(red,12):
            satisfied_games.append(int(item_list[1].replace(":","")))





print(tot(satisfied_games))
print(tot(power_list))

