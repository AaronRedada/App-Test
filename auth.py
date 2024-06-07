import pickle
from pathlib import Path
import hashlib

names = ["Aaron Redada", "Bruce Banner"]
usernames = ["ajredada", "bbanner"]
passwords = ["abc123", "def456"]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

hashed_passwords = [hash_password(pw) for pw in passwords]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)