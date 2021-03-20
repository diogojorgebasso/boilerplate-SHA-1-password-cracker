import hashlib

def crack_sha1_hash(hash, use_salts=False):
  with open('top-10000-passwords.txt') as fp:
    passwords = fp.read()
    if use_salts:
      with open("known-salts.txt", 'r') as f:
        salts = f.read()
        for salt in salts:
          for password in passwords:
            salted = salt+password
            if str(hashlib.sha1(salted.encode()).hexdigest()) == hash:
              return password
    else:
      for senha in passwords:
        if str(hashlib.sha1(senha.encode()).hexdigest()) == hash:
          return senha
      
        