from random import sample
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz1234567890"
def get_random_password(n) -> str:
   return ''.join(sample(symbols, n))

print(get_random_password(8))
