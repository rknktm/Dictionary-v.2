
from time import sleep
import os

# finding word
def find(word):
    with open("words.txt","r",encoding = "utf-8") as file:
      dicto = dict()
      for i in file:
        key = str(i.strip("\n").split("\t")[0]).capitalize()
        value = str(i.strip("\n").split("\t")[1]).capitalize()
        dicto[key]=value
      responce = dicto.get(word,"UPS :(( word coundn't be found.")
      print("Please wait...\N{sauropod}")
      sleep(3)
      return f" {word} ==> \N{sauropod}  ==> {responce} "

# addition a new word pairs
def add(key,value):
  # word kontrol
  with open("words.txt","r",encoding = "utf-8") as file:
    dicto = dict()
    for i in file:
      pkey = str(i.strip("\n").split("\t")[0]).capitalize()
      pvalue = str(i.strip("\n").split("\t")[1]).capitalize()
      if pkey not in dicto.keys() and pvalue not in dicto.values():
        dicto[pkey] = pvalue
    if key  in dicto.keys() and value in dicto.values():
      return f"{key} ==> \N{sauropod} ==> {value} is already in the dictionary."
    elif (key+"*") in dicto.keys() and value in dicto.values():
       return f"{key} ==> \N{sauropod} ==> {value} is already in the dictionary."
    elif  key  in dicto.keys() and value != dicto[key]:
      word = key+"*"+"\t"+value+"\n"
      with open("words.txt","a",encoding = "utf-8") as file:
        file.write(word)
        print("Please wait while new word-pair is added to the dictionary. ")
        sleep(2)
        return f"{key} ==> \N{sauropod} ==> {value} word-pair has been succesfully added to the dictionary."

    else: 
        word = key+"\t"+value+"\n"
        with open("words.txt","a",encoding = "utf-8") as file:
          file.write(word)
          print("Please wait while new word-pair is added to the dictionary. ")
          sleep(2)
          return f"{key} ==> \N{sauropod} ==> {value} word-pair has been succesfully added to the dictionary."

# deleting word
def delete(key,value):
  # word kontrol
  with open("words.txt","r",encoding = "utf-8") as file:
    dicto = dict()
    for i in file:
      pkey = str(i.strip("\n").split("\t")[0]).capitalize()
      pvalue = str(i.strip("\n").split("\t")[1]).capitalize()
      if pkey not in dicto.keys() and pvalue not in dicto.values():
        dicto[pkey] = pvalue
  with open("words.txt","w",encoding = "utf-8") as file:
      for k,v in dicto.items():
        if k == key:
          continue
        else:
          word = k+"\t"+v+"\n"
          file.write(word)
      print("Please wait while word-pair is deleted from the dictionary. ")
      sleep(3)
      return f"{key} ==> \N{sauropod} ==> {value} word-pair has been succesfully deleted from the dictionary."

# updating word 
def update(key,oldv,newv):
  # word kontrol
  with open("words.txt","r",encoding = "utf-8") as file:
    dicto = dict()
    for i in file:
      pkey = str(i.strip("\n").split("\t")[0]).capitalize()  #pkey:key of pair
      pvalue = str(i.strip("\n").split("\t")[1]).capitalize() #pvalue:value of pair
      if pkey not in dicto.keys() and pvalue not in dicto.values():
        dicto[pkey] = pvalue
  if key in dicto.keys() and oldv in dicto.values():
    dicto.update({key:newv})
    with open("words.txt","w",encoding = "utf-8") as file:
      for k,v in dicto.items():
        word = k+"\t"+v+"\n"
        file.write(word)
      print("Please wait while word-pair is added to the dictionary. ")
      sleep(3)
      return f"{key} ==> \N{sauropod} ==> {newv} word-pair has been succesfully added to the dictionary."    
  else:   
      return f"{key} ==> \N{sauropod} ==> {oldv} is not in the dictionary."
    

 # word listing
def wlist():
  with open("words.txt","r",encoding = "utf-8") as file:
    print("""
        WORD LIST:
*****************************
          """)
    liste = []
    for i in file.readlines():
      i= list(i.strip("\n").split("\t"))
      liste.append(i)
      new_liste = sorted(liste)
    check = 0
    for i in new_liste:
      print(i[0],(17-len(i[0]))*("."),i[1])
      check += 1
    print(f"Total items in the dictionary are ==> {check} \N{sauropod} ")
    sleep(2)
 
    
while True:
  sleep(2)
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
  ******************************
  """)

  n = input("Choose a number from Menu: ")

  if n == "1" :
    key = input("Write new word: ")
    value = input("Write antonym of the word: ")
    key = key.capitalize()
    value = value.capitalize()
    print(add(key,value))
  elif n == "2" :
    key = input("Write a word to be deleted: ")
    value = input("Write antonym of the word: ")
    key= key.capitalize()
    value = value.capitalize()
    print(delete(key,value))
  elif n == "3" :
    key = input("Write a word to be updated: ")
    oldv = input("Write a old value of the word: ")
    newv = input("Write a new value of the word: ")
    key = key.capitalize()
    oldv = oldv.capitalize()
    newv = newv.capitalize()
    print(update(key,oldv,newv))
      
  elif n == "4" :
    word = input("Write a word to be found: ")
    word= word.capitalize()
    print(find(word))
       
  elif n == "5" :
      wlist()
  elif n == "6" :
    print("Thank you for your time, please wait while Quit \N{sauropod}")
    sleep(3)
    print("Have a nice day \N{sauropod}" )
    break 
  else:
    sleep(3)
    print("Please enter a valid number \N{sauropod}" )

