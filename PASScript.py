import random 
import string #Gives us our aplha-numerical-special characters
import pyautogui # keybord/mouse
import time # for pauses

#Use to get mouse location to click where you need to go
#print(pyautogui.position())


#change email as necessary
email="j.andresgonzalez1010@gmail.com"
passwordLength=12

passwordLetters=string.ascii_letters
passwordDigits=string.digits
passwordPunctuation=string.punctuation
#Change inclusion of Puncuation as necessary
password=''.join(random.choices(passwordLetters+passwordDigits+passwordPunctuation,k=passwordLength))


#Start delay
time.sleep(1) 

webBrowser=pyautogui.click(1886,381)
webBrowser

emailLocation=pyautogui.click(813,592)
emailLocation
pyautogui.typewrite(email)
#time.sleep(1)


passwordLocation=pyautogui.click(687,699)
passwordLocation
pyautogui.typewrite(password)
#time.sleep(1)


confirmPasswordLocation=pyautogui.click(688,812)
confirmPasswordLocation
pyautogui.typewrite(password)
time.sleep(1)
createAccount=pyautogui.click(696,891)

