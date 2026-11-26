import hashlib

brukernavn = "admin"
passord = "Mars2027"

hashVerdi = hashlib.sha256(passord.encode()).hexdigest()

print(hashVerdi)

brukernavninput = input("skriv in brukernavnet: ")
passordinput = hashlib.sha256(input("skriv in passord: ").encode()).hexdigest()

if brukernavn == brukernavninput and passordinput == hashVerdi:
    print("veluket")
else:
    print("feil")