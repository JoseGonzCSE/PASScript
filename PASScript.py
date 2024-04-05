import random 
import string #Gives us our aplha-numerical-special characters
import pyautogui # keybord/mouse
import time # for pauses

#Create Account Information
email="j.andresgonzalez1010@gmail.com"
passwordLength=17
passwordLetters=string.ascii_letters
passwordDigits=string.digits
passwordPunctuation=string.punctuation
password=''.join(random.choices(passwordLetters+passwordDigits+passwordPunctuation,k=passwordLength))

#Script

#Start delay
time.sleep(1) 
#Use to get mouse location to click where you need to go
#print(pyautogui.position())
webBrowser=pyautogui.click(1886,381) #My task bar is on the right of the screen, vertical
emailLocation=pyautogui.click(813,592)
pyautogui.typewrite(email)
#time.sleep(1)
passwordLocation=pyautogui.click(687,699)
pyautogui.typewrite(password)
#time.sleep(1)
confirmPasswordLocation=pyautogui.click(688,812)
pyautogui.typewrite(password)
time.sleep(1)
createAccount=pyautogui.click(696,891)

