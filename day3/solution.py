#Reading the file
with open("text.txt","r") as file:
    data=file.readlines()
    cleaned_data=[elem.replace("\n","") for elem in data] #cleaning data from the last "\n" because it can count as symbol

part_num_list=[] #part number list
for item in cleaned_data:
    new_data=item.split(".")
    #spliting items with respect to "." which will give us symbols and numbers and also "." which we can use to determine which item is suitable
    for elem in new_data:
        # I use if-elif-else on purpose because I don't want to append an element twice because it has = or % sign in it and also when removed is digit
        if "=" in elem and elem!="=": #to clean the numbers having = and append them directly to the list
            elem=elem.replace("=","")
            part_num_list.append(int(elem))

        elif "%" in elem and elem!="%": # to clean the numbers having % and append them directly to the list
            elem=elem.replace("%","")
            part_num_list.append(int(elem))
        else:
            if elem.isdigit():
                if elem!=new_data[-1]: # we can search the right element if it is not in the end of the line
                    if new_data[new_data.index(elem)-1]!='' or new_data[new_data.index(elem)+1]!='' : #checking if the left or right elements are symbol or not
                        part_num_list.append(int(elem))
                else: # if it is at the end of the line
                    if new_data[new_data.index(elem) - 1] != '': #only check the right
                        part_num_list.append(int(elem))
        #To check for diagonal
        if item!=cleaned_data[0]:
            UPPER_LINE=cleaned_data[cleaned_data.index(item) - 1]
            LOWER_LINE=cleaned_data[cleaned_data.index(item)+1]
            for diag in UPPER_LINE: # to check the above line diagonal
                if diag.isdigit() and elem.isdigit():
                    if diag == UPPER_LINE[-1]:
                        if UPPER_LINE[UPPER_LINE.index(diag) - 1] != '':  # only check the right
                            part_num_list.append(int(elem))
                        # we can search the right element if it is not in the end of the line
                    elif diag == UPPER_LINE[0]:
                        if UPPER_LINE[UPPER_LINE.index(diag) + 1] != '':  # only check the right
                            part_num_list.append(int(elem))
                    else:
                        if UPPER_LINE[UPPER_LINE.index(elem) - 1] != '' or UPPER_LINE[
                            UPPER_LINE.index(elem) + 1] != '':  # checking if the left or right elements are symbol or not
                            part_num_list.append(int(elem))
                # if it is at the end of the line



print(part_num_list)

