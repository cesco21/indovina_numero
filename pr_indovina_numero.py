import random 
risultato = random.randint(1,100)
i = 1
numero = int(input("inserisci un numero: "))
while(i<10 and numero!=risultato):
	if(numero>risultato):
		print("il numero è troppo grande!")
	elif(numero<risultato):
		print("il numero è troppo piccolo!")
	i = i+1
	numero = int(input("inserisci un numero: "))
if(numero!=risultato):
	print("mi dispiace non hai indovinato, riprova!")
else:
	print("congratulazioni hai indovinato!")