import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') 
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

questions=[
    ["The International Literacy Day is observed on ?",
           "Sep 8","Nov 28",
           "May 2","Sep 22",1],

    ["The language of Lakshadweep. a Union Territory of India, is?",
           "Tamil","Hindi",
           "Malyalam","Telugu",3],

    ["Which language was used to create Facebook?",
           "python","Javascript",
           "Php","None",3], 

    ["In which group of places the Kumbha Mela is held every twelve yea",
           "Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik",
           "Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,'Haridwar",2],

    ["Who painted the Mona Lisa?",
     "Michelangelo", "Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", 4],

    ["What is the currency of Japan?",
     "Yen", "Euro", "Dollar", "Pound", 1],   

    ["Who was the first woman to win a Nobel Prize?",
     "Rosalind Franklin","Marie Curie", "Mother Teresa", "Ada Lovelace", 2],

    ["Which is the longest river in the world?",
     "Yangtze", "Amazon", "Nile", "Mississippi", 3],

    ["Which country is the largest by land area?",
     "Russia", "Canada", "China", "United States", 1],

    ["What is the tallest mountain in the world?",
     "Lhotse", "K2", "Kangchenjunga", "Mount Everest", 4],

    ["Who wrote 'To Kill a Mockingbird'?",
     "Harper Lee", "Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain", 3],

    ["Which is the largest mammal?",
     "Blue Whale", "Elephant", "Giraffe", "Hippopotamus", 1],

    ["What is the chemical symbol for water?",
     "O2", "CO2", "NaCl", "H2O", 4],

    ["Which planet is known as the Red Planet?",
     "Mars", "Venus", "Jupiter", "Saturn", 2],

    ["What is the capital of France?",
     "Paris", "Berlin", "London", "Rome", 1]
]


levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1280000,2500000,5000000,10000000]
money=0

for i in range(0,len(questions)):
    
    question=questions[i]
    print(f"\n\nQuestion for {levels[i]} Rupees")
    print(question[0])
    print(f"1. {question[1]}           2. {question[2]}")
    print(f"3. {question[3]}           4. {question[4]}")    
    speak(f"\n\nQuestion for {levels[i]} Rupees")
    speak(question[0])
    speak(f"1. {question[1]}")
    speak(f"2. {question[2]}")
    speak(f"3. {question[3]}")
    speak(f"4. {question[4]}")
    reply= int(input("Enter your Answer Between 1 to 4 or press 0 to quit\n"))
    if reply == 0:
        print(f"Congratulations!!!\nYou won {money} Rupees")
        speak(f"Congratulations!!!\nYou won {money} Rupees")
        break
    
    elif reply == question[-1]:
        print(f"Correct! You have won {levels[i]} Rupees")
        speak(f"Correct! You have won {levels[i]} Rupees")
        money = levels[i]
    
    else:
        if money < 10000:
            print("Wrong Answer!")
            print(f"Correct answer is: {question[-1]}!")
            speak("Wrong Answer!")
            speak(f"Correct answer is: {question[-1]}!")
            break
        elif money >= 10000 and money < 320000:
            print("Wrong Answer! You are out!")
            speak("Wrong Answer! You are out!")
            money = 10000
            print(f"Congratulations!!!\nYou won {money} Rupees")
            speak(f"Congratulations!!!\nYou won {money} Rupees")
            break
        elif money >= 320000 and money < 10000000:
            print("Wrong Answer! You are out!")
            speak("Wrong Answer! You are out!")
            money = 320000
            print(f"Congratulations!!!\nYou won {money} Rupees")
            speak(f"Congratulations!!!\nYou won {money} Rupees")
            break
print(f"Congratulations!!!\nYou won {money} Rupees")    
speak(f"Congratulations!!!\nYou won {money} Rupees")

