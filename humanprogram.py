import os
import pyttsx3

pyttsx3.speak("welcome to my program")
print("Welcome to my program")

print()

print("""press 1 for 'Numerical Menu' 
Press 2 for 'Word Menu' 
Press 3 for 'Exit' """)

print("\nEnter Your Choice: ", end= " ")

c= input()
print()

while True:
    if int (c)==1:
        print("""         Press 1 to open the  'Internet Explorer' 
        Press2 to open the 'Chrome Browser' 
        Press 3 to open the 'Notepad' 
        Press 4 to open the 'Gmail' 
        Press 5 to open the 'FireFox'
        Press 6 to open the 'Windows Explorer'
        Press 7 to open the 'Windows Media Player'
        Press 8 to open the 'Facebook'
        Press 9 to open the 'WhatsApp'
        Press 10 to open the 'Instagram'
        press 11 to open the 'GitHub'
        Press 12 to open the 'LinkedIn'
        Press 13 to open the 'Telegram Messenger'
        Press 14 to open the 'Flipkart'
        Press 15 to open the 'Amazon'
        Press 16 to 'Exit'   """)
       
        
        print("\nEnter Your Choice: ", end=" ")
        ch2= input()
        print()
            
        if int (ch2)==1:
            print("Opening Internet Explorer")
            pyttsx3.speak("Opening Internet Explorer.")
            os.system("start iexplore")
            
        elif int (ch2)==2:
            print("Opening Chrome Browser")
            pyttsx3.speak("Opening Chrome Browser")
            os.system("start chrome")
        
        elif int (ch2)==3:
            print("Opening Notepad Text Editor")
            pyttsx3.speak("Opening Notepad Text Editor")
            os.system("start notepad")
        
        elif int (ch2)==4:
            print("Opening Gmail")
            pyttsx3.speak("Opening Gmail")
            os.system("start www.gmail.com")
            
        elif int (ch2)==5:
            print("Opening FireFox")
            pyttsx3.speak("Opening FireFox")
            os.system("start Firefox")
            
        elif int (ch2)==6:
            print("Opening Windows Explorer")
            pyttsx3.speak("Opening windows Explorer")
            os.system("start .")
            
        elif int (ch2)==7:
            print("Opening Windows Media Player")
            pyttsx3.speak("Opening Windows Media Player")
            os.system("start wmplayer")
            
        elif int (ch2)==8:
            print("Opening Facebook")
            pyttsx3.speak("Opening Facebook")
            os.system("start https://www.facebook.com/")
            
        elif int(ch2)==9:
            print("Opening WhatsApp")
            pyttsx3.speak("Opening Whatsapp")
            os.system("start https://www.whatsapp.com/")
            
        elif int(ch2)==10:
            print("Opening Instagram")
            pyttsx3.speak("Opening instagram")
            os.system("start https://www.instagram.com/")
            
        elif int (ch2)==11:
            print("opening GitHub")
            pyttsx3.speak("Opening github")
            os.system("start https://github.com/")
            
        elif int (ch2)==12:
            print("opening LikedIn")
            pyttsx3.speak("Opening linkedin")
            os.system("start https://www.linkedin.com/")
            
        elif int (ch2)==13:
            print("opening Telegram Messenger")
            pyttsx3.speak("Opening Telegram Messenger")
            os.system("start https://telegram.org/")
            
        elif int (ch2)==14:
            print("opening Flipkart")
            pyttsx3.speak("Opening flipkart")
            os.system("start https://www.flipkart.com/")
            
        elif int (ch2)==15:
            print("opening Amazon")
            pyttsx3.speak("Opening amazon")
            os.system("start https://www.amazon.com/")
            
        elif int(ch2)==16:
            print("Goodbye, seen you later.........")
            pyttsx3.speak("Goodbye, seen you later")
            exit()
            
        else:
            print("!!!!Invalid Command Try Again!!!!!")
            pyttsx3.speak("Invalid Command, Please Try again")
            break
    
    elif int (c)==2:
        print("Chat With Me: ", end=" ")
        p= input()
        
        if(("chrome" in p) or ("google" in p)):
            pyttsx3.speak("Opening Chrome Browser")
            os.system("start chrome")
            
        elif(("notepad" in p) or ("text" in p) or ("editor" in p)):
            pyttsx3.speak("Opening Notepad Text Editor.")
            os.system("start notepad")
            
        elif(("internet explorer" in p) or ("explorer" in p)):
            pyttsx3.speak("Opening Internet Explorer.")
            os.system("start iexplore")
            
        elif(("gmail" in p) or ("mail" in p)):
            pyttsx3.speak("Opening Gmail.")
            os.system("start https://mail.google.com/")
            
        elif(("firefox" in p)):
            pyttsx3.speak("Opening FireFox.")
            os.system(" start firefox")
            
        elif(("media" in p) or ("player" in  p)):
            pyttsx3.speak("Opening Windows Media Player")
            os.system('start wmplayer')
            
        elif(("facebook" in p)):
            pyttsx3.speak("Opening Facebook")
            os.system("start https://www.facebook.com/")
            
        elif(("instagram" in p) or ("insta" in p)):
            pyttsx3.speak("Opening Instagram")
            os.system(" start https://www.instagram.com/")
            
        elif(("whatsapp" in p) or ("whats") in p):
            pyttsx3.speak("Opening Whatapp")
            os.system("start https://www.whatsapp.com/")
            
        elif(("Telegram" in p) or ("telegram messenger" in p)):
            pyttsx3.speak("Opening Telegram Messenger")
            os.system("start https://telegram.org/")
            
        elif(("github" in p) or ("git" in p)):
            pyttsx3.speak("Opening github")
            os.system("start https://github.com/")
            
        elif(("linkedin" in p) or ("linked" in p)):
            pyttsx3.speak("Opening linkedin")
            os.system("start https://www.linkedin.com/")
            
        elif(("flipkart" in p) or ("shoping" in p)):
            pyttsx3.speak("Opening Flipkart online shoping site")
            os.system("start https://www.flipkart.com/")
            
        elif(("amazon" in p)):
            pyttsx3.speak("Opening Amazon online shoping site")
            pyttsx3.speak("start https://www.amazon.com/")
            
        elif(("exit" in p) or ("back" in p) or ("quit" in p) or ("stop" in p)):
            pyttsx3.speak("Goodbye, See you Later")
            
        else:
            pyttsx3.speak("Invalid Choice, Please enter correct command or try again later")
            break
            
    elif int (c)==3:
        print("Goodbye, See you later............")
        pyttsx3.speak("Goodbye, See you later")
        break
        exit()
        
    else:
        print("!!!!Invalid Choice, Please Try Again!!!!")
        pyttsx3.speak("Invalid Choice, Please Try Again")
        break
        exit()