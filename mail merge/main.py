#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def create_list():
    f =  open("mail merge/Input/Names/inivited_names.txt", "r")
    names =f.readlines()
    names2 = []
    for x in names:
        if x:
            names2.append(x.strip())
    
    docx = open('mail merge/Input/Letters/starting_letter.docx', 'r')
    docx2 = docx.read()
    for x in names2:
        file = docx2.replace('name', x)
        file2 = open(f"mail merge/Input/{x}.txt", "w")
        file2.write(file)
create_list()