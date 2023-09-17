import random

def generate_prime_numbers(bits):
  """Generates two prime numbers of the specified bit length."""
  while True:
    p = random.randint(2*(bits - 1), 2*bits - 1)
    q = random.randint(2*(bits - 1), 2*bits - 1)
    if is_prime(p) and is_prime(q):
      return p, q

def is_prime(n):
  """Checks if the number is prime."""
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def gcd(a, b):
  """Returns the greatest common divisor of a and b."""
  while b != 0:
    a, b = b, a % b
  return a

def generate_keys(p, q):
  """Generates the public and private keys."""
  n = p * q
  phi = (p - 1) * (q - 1)
  e = random.randint(2, phi - 1)
  d = gcd(e, phi)
  return n, e, d

def encrypt(message, public_key):
  """Encrypts the message using the public key."""
  n, e = public_key
  ciphertext = pow(message, e, n)
  return ciphertext

def decrypt(ciphertext, private_key):
  """Decrypts the ciphertext using the private key."""
  n, d = private_key
  plaintext = pow(ciphertext, d, n)
  return plaintext

def main():
  # Generate the public and private keys.
  p, q = generate_prime_numbers(1024)
  public_key = (n, e)
  private_key = (n, d)

  # Get the name, registered number, DOB, phone number, and blood group from the user.
  name = input("Enter your name: ")
  registered_number = input("Enter your registered number: ")
  dob = input("Enter your date of birth (YYYY-MM-DD): ")
  phone_number = input("Enter your phone number: ")
  blood_group = input("Enter your blood group: ")

  # Encrypt the data using the public key.
  ciphertext = encrypt(name + registered_number + dob + phone_number + blood_group, public_key)

  # Print the encrypted data.
  print("The encrypted data is: ", ciphertext)

if __name__ == "_main_":
  main()