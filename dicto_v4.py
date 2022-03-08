from time import sleep
import os
# 1-addition a new word pairs
def add(key,newv):
  with open("words.txt","r",encoding = "utf-8") as file:
    dicto = dict()
    for i in file:
        pkey = str(i.strip("\n").split(" ")[0]).capitalize()
        pvalue = str(i.strip("\n").split(" ")[1]).title()
        if pkey not in dicto.keys() and pvalue not in dicto.values():
            dicto[pkey] = pvalue
    if key  in dicto.keys() and newv in dicto.values():
        return f"{key} ==> \N{sauropod} ==> {newv} is already in the dictionary."
    elif key in dicto.keys() and newv != dicto[key]:
        values = dicto.get(key),newv
        dicto[key] = list(values)
    else:
        dicto[key] = newv
  with open("words.txt","w",encoding = "utf-8") as file:
        for k,v in dicto.items():
          if type(v) == type([]):
              value =""
              for i in v:
                  value += i+","
              value = value.strip(",")
              word =(k+" "+value+"\n")
              file.write(word)
          else:
              word =(k+" "+ str(v)+"\n")
              file.write(word)
        print("Please wait while word-pair is added in the dictionary. ")
        sleep(3)
        return f"{key} ==> \N{sauropod} ==> {newv} word-pair has been succesfully added in the dictionary."    
# 2-deleting word
def delete(key):
  with open("words.txt","r",encoding = "utf-8") as file:
    dicto = dict()
    for i in file:
      pkey = str(i.strip("\n").split(" ")[0]).capitalize()
      pvalue = str(i.strip("\n").split(" ")[1]).title()
      dicto[pkey] = pvalue
  if key in dicto.keys():
      with open("words.txt","w",encoding = "utf-8") as file:
          for k,v in dicto.items():
            if key == k:
              if "," in dicto[key]:         
                  while True:
                      responce = input(f"Which antonym of the word would you like to delete? {dicto[key]}:").capitalize()
                      if responce in dicto[key]:
                          break 
                      else:
                        print("Entered value is not in given values.Please try again")
                        sleep(1)
                        continue
                  liste = dicto[key].split(",")
                  liste.remove(responce)
                  value =""
                  for i in liste:
                      value += i+","
                  value = value.strip(",")
                  word =(key+" "+value+"\n")
                  file.write(word)
                  print("Please wait while word-pair is deleted from the dictionary. ")
                  sleep(2)
                  print(f"{key} ==> \N{sauropod} ==> {responce} word-pair has been succesfully deleted from the dictionary.")
              else:
                print("Please wait while word-pair is deleted from the dictionary. ")
                sleep(2)
                print(f"{key} ==> \N{sauropod} ==> {dicto[key]} word-pair has been succesfully deleted from the dictionary.")
            else:
              word = (k+" "+v+"\n")
              file.write(word)
  else:
    return f"\N{sauropod} ==> {key} coundn't be found in the dictionary"
# 3-updating word 
def update(key):
  with open("words.txt","r",encoding = "utf-8") as file:
    dicto = dict()
    for i in file:
      pkey = str(i.strip("\n").split(" ")[0]).capitalize()  
      pvalue = str(i.strip("\n").split(" ")[1]).title() 
      dicto[pkey] = pvalue
  if key in dicto.keys(): 
      responce = dicto.get(key,"UPS :(( word coundn't be found.")
      if responce == "UPS :(( word coundn't be found.":
        print(responce)
        sleep(2) #new word adding
        while True:
          ant = input("Would you like save these word to the dictionary? \N{sauropod} ==> y/n:").capitalize()
          if ant == "Y" :
              newv= input("Please write antonym of the word: ").capitalize()
              print("Please wait while word-pair is updating... ")
              dicto[key] = newv
              sleep(1)
              print(f"{key} ==> \N{sauropod} ==> {newv} word-pair has been succesfully added to the dictionary.")
              break
          elif ant == "N":
              print("Please wait while quit \N{sauropod}")
              sleep(1)
              return "Thank you for your time \N{sauropod}" 
          else:
              print("Please enter y/n \N{sauropod}" )
              continue      
      else:
          print(f"Currently antonym of tne word {key} ==> \N{sauropod} ==> {responce} ")
          if "," in responce: 
              word = input(f"Which antonym of the word would you like to update? {responce}:").capitalize()
              newv = input("Please write new antonym of the word:").capitalize()
              if word not in responce:
                  print("\N{sauropod} word doesn't exist\N{sauropod}")
                  return "Thank you for your time \N{sauropod}" 
              else:  
                  responce = responce.split(",")
                  position = responce.index(word)
                  responce.insert(position,newv)
                  responce.pop(position+1)
                  value = ""
                  for i in responce:
                      value =value+i+","
                  value = value.strip(",")
                  dicto[key] = value
          else:
              newv= input("Please write new antonym of the word: ")
              newv = newv.capitalize()
              dicto[key] = newv
      with open("words.txt","w",encoding = "utf-8") as file:
          for k,v in dicto.items():
              word =(k+" "+ str(v)+"\n")
              file.write(word)
          print("Please wait while word-pair is updated to the dictionary. ")
          sleep(3)
          return f"{key} ==> \N{sauropod} ==> {newv} word-pair has been succesfully updated to the dictionary."   
  else:
    return f"\N{sauropod} ==> {key} coundn't be found in the dictionary" 
# 4-finding word
def find(word):
  with open("words.txt","r",encoding = "utf-8") as file:
    dicto = dict()
    for i in file:
        pkey = str(i.strip("\n").split(" ")[0]).capitalize()
        pvalue = str(i.strip("\n").split(" ")[1]).title()
        dicto[pkey] = pvalue
    keys = list(dicto.keys())
    vals = list(dicto.values())
    if word in keys:
        print("Please wait...\N{sauropod}")
        sleep(2)
        return f" {word} ==> \N{sauropod}  ==> {dicto[word]} "
    for i in vals:
        if word == i:
            print("Please wait...\N{sauropod}")
            sleep(2)
            return f" {word} ==> \N{sauropod}  ==> {keys[vals.index(word)]} "
        if word in i:
            i= i.split(",")
            value =""
            for k in i:
                value =value+k+","
                if k == word:
                    po2 = i.index(k)
            value = value.strip(",")
            return f" {i[po2]} ==> \N{sauropod}  ==> {keys[vals.index(value)]} "  
        elif word != i:
          continue
    print("Please wait...\N{sauropod}")
    sleep(2)
    return f"\N{sauropod} ==> {word} coundn't be found in the dictionary"
# 5-word listing
def wlist():
  with open("words.txt","r",encoding = "utf-8") as file:
    print("""
        WORD LIST:
*****************************""")
    liste = []
    for i in file.readlines():
      i= list(i.strip("\n").split(" "))
      liste.append(i)
      new_liste = sorted(liste)
    check = 0
    for i in new_liste:
      print(i[0],(17-len(i[0]))*("."),*i[1:])
      check += 1
    print(f"Total items in the dictionary are ==> {check} \N{sauropod} ")
    sleep(1)
while True:
  sleep(3)
  os.system('cls')
  print("""
  ******************************
  *       ANTONYM WORDS        *
  *  \N{ghost}       MENU        \N{ghost}   *
  *----------------------------*
  *       1-Adding             *
  *       2-Deleting           *
  *       3-Updating           *
  *       4-Finding            * 
  *       5-Listing            *
  *       6-Quit               *
  ******************************""")
  n = input("Choose a number from Menu: ")
  if n == "1" :
    key = input("Write new word: ")
    newv = input("Write antonym of the word: ")
    print(add(key.capitalize(),newv.capitalize()))
  elif n == "2" :
    key = input("Write a word to be deleted: ")
    print(delete(key.capitalize()))
  elif n == "3" :
    key = input("Write a word to be updated: ")
    print(update(key.capitalize()))   
  elif n == "4" :
    word = input("Write a word to be found: ")
    print(find(word.capitalize()))    
  elif n == "5" :
      wlist()
  elif n == "6" :
    print("Thank you for your time, please wait while Quit \N{sauropod}")
    sleep(2)
    print("Have a nice day \N{sauropod}" )
    sleep(2)
    os.system('cls')
    break 
  else:
    sleep(2)
    print("Please enter a valid number \N{sauropod}" )