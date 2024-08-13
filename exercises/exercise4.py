import string

string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random


def random_char(y):
  return ''.join(random.choice(string.ascii_letters) for x in range(y))


random.choice(string.ascii_letters)
chat = int(
  input("Want to send code or Decode press 1 for coding and 2 for decoding :"))
if (chat == 1):
  a = input("Enter what you want to tell your friend: ")
  words = a.split(" ")
  nwords = []
  for word in words:
    if (len(word) == 2):
      sent = word[::-1]
      nwords.append(sent)
    elif (len(word) == 1):
      sent = word
      nwords.append(sent)
    else:
      sent = random_char(3) + word[1:] + word[0] + random_char(3)
      nwords.append(sent)

  print(" ".join(nwords))
else:
  a = input("Enter what your friend has told you: ")
  words = a.split(" ")
  nwords = []
  for word in words:
    if (len(word) == 2):
      reci = word[::-1]
      nwords.append(reci)
    elif (len(word) == 1):
      reci = word
      nwords.append(reci)
    else:
      # st=-random_char(3)+word[1:]+word[0]-random_char(3)
      reci = word[-4] + word[3:-4]
      nwords.append(reci)

  print(" ".join(nwords))
