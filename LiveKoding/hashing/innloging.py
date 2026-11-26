import hashlib, secrets

brukernavn = "admin"
passord = "Mars2027"

salt = secrets.token_bytes(16)
print(salt)

hashVerdi = hashlib.sha256(salt + passord.encode()).hexdigest()

print(hashVerdi)

brukernavninput = input("skriv in brukernavnet: ")
passordinput = hashlib.sha256(salt + input("skriv in passord: ").encode()).hexdigest()

if brukernavn == brukernavninput and passordinput == hashVerdi:
    print("veluket")
else:
    print("feil")