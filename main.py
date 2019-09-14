import random
import time

text_to_find = input("Enter a word to shuffle : ")
liste = list(text_to_find)
liste_to_find = list(text_to_find)
rounds = 0
random.shuffle(liste)
found = True
print(liste)
print(liste_to_find)

while found:
	
	#time.sleep(0.1)
	rounds+=1
	random.shuffle(liste)
	print(''.join(liste))

	if liste == liste_to_find:

		print("liste finded in",rounds)
		found = False
