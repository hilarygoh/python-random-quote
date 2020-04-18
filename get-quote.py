import random

def bigthing():
  #print("Keep it logically awesome.")

  f = open("Fairbairnfilmquotes.txt")
  quotes = f.readlines()
  f.close()

  last = 12
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  bigthing()
