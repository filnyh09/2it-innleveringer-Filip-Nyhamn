import hashlib, secrets, time

passord = "test"
passor = "lest"
salt1 = "salt".encode()
salt2 = "annen salt".encode()

def scryptHash(passord, salt):
    return hashlib.scrypt(
        passord.encode(), 
        salt=salt,
        n=2**14,
        r=8,
        p=1
        )

print(f"Hasher det samme passordet flere ganger uten salt, der algoritmen støtter dette: {scryptHash(passord, salt1) == scryptHash(passord, salt1)}")
print(f"Endrer ett tegn i passordet: {scryptHash(passord, salt1) != scryptHash(passor, salt1)}")
print(f"Hasher samme passord med forskjellige salt: {scryptHash(passord, salt1) != scryptHash(passord, salt2)}")
startTid = time.perf_counter()
scryptHash(passord, salt1)
print(f"Måler hvor lang tid algoritmene bruker på å beregne en hashverdi: {time.perf_counter() - startTid}")