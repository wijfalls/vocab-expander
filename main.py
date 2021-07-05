import csv
from csv import writer
import requests
from bs4 import BeautifulSoup as Soup
import random
import pyautogui

def compact(strarr):
    x = ''
    for element in strarr:
        if element != strarr[0]:
            x = x + element + " "
    return x


name = 'William'
print("Hello " + name + ',')
choice = input("Would you like to add a word to learn, "
               "study current list of words, "
               "or look at archive of learned words?(+/c/o)")
if choice == "+":
    arr = input("Enter words with spaces between to add them to your vocab expansion helper: ")
    words = arr.split()
    with open("vocab.csv", 'a') as f:
        for w in words:

            url = "https://www.vocabulary.com/dictionary/" + w + ""
            response = requests.get(url)
            soup = Soup(response.content, 'html.parser')
            soup1 = soup.find("div", {"class": "definition"})

            writer_obj = writer(f)
            Ar = []
            try:
                soup1 = soup1.get_text()
                definition = str(soup1).replace("\n", "")

                temp = definition.split()
                ndef = compact(temp)

                Ar = [w, temp[0], ndef]
            except AttributeError:
                Ar = [w]
                print("'" + w + "' doesn't seem to exist. Its defintion will be omitted from the vocab list and it will be omitted when studying.")

            writer_obj.writerow(Ar)
        f.close()
elif choice == 'c':
    words = []
    definitions = []
    with open('vocab.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in reader:

            if i >= 1 and len(row) >= 1:
                words.append(row[0])
                definitions.append(row[2])
            i = i + 1

        csvfile.close()
    rndwrd = random.randint(0, len(words))
    w = words[rndwrd]
    pyautogui.hotkey('command', 'shift', 's')
    indef = input("What is the definition of " + w + '?')
    if indef == definitions[rndwrd]:
        pyautogui.hotkey('command', 'shift', 's')
        print("Good muthaFucking job!! You are weeeeellll on your way to learning another word!")
    else:
        pyautogui.hotkey('command', 'shift', 's')
        print("You didnt quite get it. :(")
        print('This is your input: ' + indef)
        print('This is the correct definition: ' + definitions[rndwrd])

    # for w in words:
    #     print(w)
    # for d in definitions:
    #     print(d)


