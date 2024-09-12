#import pygame 
import requests

response = requests.get("https://pypi.org/simple/pip/", verify=False)

askA="Do you want to be my friend?"
askA="How is your day?"
#      ow is your day?
# owHis your day?

ask = list(askA)
#ask="o you want to be my friend?"
print(askA)

for a in range(len(ask)):
   print("a: ", a)
   for b in range(a + 1, len(ask)):
       print(" b: ", b, end=''),
       if ord(ask[a]) > ord(ask[b]):
           #print("i am in", type(ask[a]))
           #because I will earse ask[a]
           c = ask[a] #store index a from ask string's value
           #print("i am in", type(ask[a]), type(c))
           ask[a] = ask[b] #store index b from ask string's value to 
           ask[b] = c # put ask[a] back
           d=""
           print("\n["+d.join(ask)+']\n')
   d=""
   print("\n["+d.join(ask)+']\n')
d=""
print(d.join(ask))
