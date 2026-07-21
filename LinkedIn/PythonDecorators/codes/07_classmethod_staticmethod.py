"""@classmethod receives the class (cls); @staticmethod receives nothing.

Use classmethod for alternate constructors, staticmethod for helpers that
logically belong to the class but don't touch it.
Run:  python 07_classmethod_staticmethod.py
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_json(cls, data):           # alternate constructor -> returns cls(...)
        return cls(data["name"], data["email"])

    @staticmethod
    def valid(email):                   # no self, no cls — just namespacing
        return "@" in email

    def __repr__(self):
        return f"User({self.name!r}, {self.email!r})"


if __name__ == "__main__":
    u = User.from_json({"name": "Ada", "email": "ada@mail.com"})
    print(u)
    print("valid:", User.valid("nope"))     # False
    print("valid:", User.valid(u.email))    # True
