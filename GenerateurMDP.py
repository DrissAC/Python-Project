import random, string

def generate_password(length):
    if length < 4:
        raise ValueError("Le mot de passe doit avoir au moins 4 caractères.")
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    specials_chars = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(specials_chars)
    ]

    all_chars = uppercase + lowercase + digits + specials_chars
    password +=random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("Entrez la longueur du mot de passe (minimum 4): "))
    password = generate_password(length)
    print("Le mot de passe est:", password)
except ValueError as e:
    print("Erreur:", e)