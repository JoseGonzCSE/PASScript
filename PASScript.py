import random 
import string #Gives us our aplha-numerical-special characters
import pyautogui # keybord/mouse
import time # for pauses

#change email as necessary
email="j.andresgonzalez1010@gmail.com"
passwordLength=12
passwordLetters=string.ascii_letters
passwordDigits=string.digits
passwordPunctuation=string.punctuation

#Change inclusion of Puncuation as necessary
password=''.join(random.choices(passwordLetters+passwordDigits+passwordPunctuation,k=passwordLength))
confirmPassword=password
time.sleep(1)
#print(pyautogui.position())
#print(pyautogui.position()) Use to get mouse location to click where you need to go


webBrowser=pyautogui.click(1886,381)
webBrowser

emailLocation=pyautogui.click(813,592)
emailLocation
pyautogui.typewrite(email)

passwordLocation=pyautogui.click(844,710)
passwordLocation
pyautogui.typewrite(password)
confirmPasswordLocation=pyautogui.click(988,840)
confirmPasswordLocation
pyautogui.typewrite(password)
