# PASScript (WorkDay Account Creation Automation)

## Overview

This Python script automates the process of creating an account on the WorkDay website, including generating a random password. The motivation behind this script is to streamline the account creation process, particularly for websites like WorkDay that may not work seamlessly with browser-based password generators.

## Problem Statement

When using Google Chrome, the built-in random password generator does not function properly on the WorkDay website. This issue leads to inefficiencies and time wastage for users who frequently need to create accounts on such platforms. The conventional workaround involves manually opening a new tab, searching for an online random password generator, copying the generated password, and pasting it into the registration form. This script aims to automate the entire process, eliminating the need for manual intervention.

## Solution

The script utilizes Python along with the PyAutoGUI library to automate the account creation process. It generates a random password using a combination of alphabetic characters, digits, and special symbols. The automation includes clicking on specific locations within the browser window to navigate through the registration form and entering the generated email and password.

## Usage

1. Ensure that Python is installed on your system.
2. Install the PyAutoGUI library using `pip install pyautogui`.
3. Modify the `email` variable to specify your desired email address.
4. Adjust the `passwordLength` variable to set the desired length of the generated password.
5. Run the script.
6. If the script doesn't work as expected, you may need to adjust the click locations within the script. Banner size differences among companies' websites can affect the coordinates of elements on the page. You can modify the click values in the script to match the specific layout of the registration form on the WorkDay website or any other website you are automating account creation for.
7. Sit back and let the script handle the account creation process for you.

## Disclaimer

Please note that automation scripts like this should be used responsibly and ethically. Make sure to comply with all relevant terms of service and legal regulations when using automation tools.
