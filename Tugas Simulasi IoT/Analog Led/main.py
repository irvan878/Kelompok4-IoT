from gpio import * 
from time import *  
def main():
  pinMode(0, IN)
  pinMode(1, OUT)
  print("light on")
  while True: 
    if digitalRead(0)== HIGH:
      digitalWrite(1, HIGH)
    else : 
      digitalWrite(1, LOW)

if __name__ == "__main__": 
  main()
