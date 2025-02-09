from Crypto.Hash import SHA3_256, SHA3_224, SHA3_384, SHA3_512, BLAKE2s, BLAKE2b, SHAKE128, SHAKE256
import string

# Demander à l'utilisateur d'entrer le hash à cracker
hash_to_crack = input("Entrez le hash à cracker : ")

# Tous les caractères possibles : lettres minuscules, majuscules, chiffres et symboles
possible_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Fonction pour tester différentes méthodes de hachage
def brute_force_hash(hash_type):
    for char in possible_characters:
        if hash_type == "SHA3_256":
            hasher = SHA3_256.new(data=char.encode())
        elif hash_type == "SHA3_224":
            hasher = SHA3_224.new(data=char.encode())
        elif hash_type == "SHA3_384":
            hasher = SHA3_384.new(data=char.encode())
        elif hash_type == "SHA3_512":
            hasher = SHA3_512.new(data=char.encode())
        elif hash_type == "BLAKE2s":
            hasher = BLAKE2s.new(data=char.encode(), digest_bits=256)
        elif hash_type == "BLAKE2b":
            hasher = BLAKE2b.new(data=char.encode(), digest_bits=512)
        elif hash_type == "SHAKE128":
            hasher = SHAKE128.new()
            hasher.update(char.encode())
        elif hash_type == "SHAKE256":
            hasher = SHAKE256.new()
            hasher.update(char.encode())
        
        # Calculer le hash du caractère
        if hash_type in ["SHAKE128", "SHAKE256"]:
            char_hash = hasher.read(32).hex()  # 32 bytes for SHAKE output
        else:
            char_hash = hasher.hexdigest()

        # Vérifier si le hash correspond
        if char_hash == hash_to_crack:
            print(f"Correspondance trouvée pour {hash_type} : {char}")
            return char

    print(f"Aucune correspondance trouvée pour {hash_type}.")

# Liste des hachages à tester
hash_algorithms = ["SHA3_256", "SHA3_224", "SHA3_384", "SHA3_512", "BLAKE2s", "BLAKE2b", "SHAKE128", "SHAKE256"]

# Tester tous les algorithmes de hachage sur les caractères possibles
for algo in hash_algorithms:
    brute_force_hash(algo)
