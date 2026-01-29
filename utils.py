import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash

def add(self, username, password_hash):
    # TODO: prevent weak usernames
    self.users[username] = {
        "username": username,
        "password": password_hash
    }
