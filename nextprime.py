def prime(w):
  if w == 2:
    return True
  if w % 2 == 0 or w <2:
    return False
  for i in range(3, int(w**0.5)+1, 2):
    if w%i == 0:
      return False
  return True
def find_next_prime(n):
  while not prime(n):
    n += 1
  print n

find_next_prime(22)