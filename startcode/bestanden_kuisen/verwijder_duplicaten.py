import os
import hashlib
from collections import defaultdict

hash_groepen = defaultdict(list)

def bereken_hash(bestand_pad):
    with open(bestand_pad, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

