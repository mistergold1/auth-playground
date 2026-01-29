import json
import os


class UserStorage:
    def __init__(self, filename):
        self.filename = filename
        self.users = self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as f:
            return json.load(f)

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.users, f, indent=2)

    def exists(self, username):
        return username in self.users

    def add(self, username, password_hash):
        self.users[username] = {
            "username": username,
            "password": password_hash
        }
        self._save()

    def get(self, username):
        return self.users.get(username)
