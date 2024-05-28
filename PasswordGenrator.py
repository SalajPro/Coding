#Password Genrator
import random
from time import sleep

lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spectal_char = ['!','@','#','$','%','&']
number = ['1','2','3','4','5','6','7','8','9']


lower_case_choise = random.choice(lower_case)
upper_case_choise = random.choice(upper_case)
spectal_char_choise = random.choice(spectal_char)
numberchoise = random.choice(number)

lower_case_choise2 = random.choice(lower_case)
upper_case_choise2 = random.choice(upper_case)
spectal_char_choise2 = random.choice(spectal_char)
numberchoise2 = random.choice(number)

print("Your Genrated Password Is: "+lower_case_choise+upper_case_choise+spectal_char_choise+numberchoise+
                                lower_case_choise2+upper_case_choise2+spectal_char_choise2+numberchoise2+spectal_char_choise2+lower_case_choise)
sleep(8)


