n = input()
s = int(input())
def spyDecoder(n,s):
   a = []
   for i in range (0,len(n)):
      if n[i] == ' ':
         a.append(n[i])
      elif (ord(n[i])-s)<= 65 or ord(n[i]) <= 65:
         code = n.replace(n[i],chr(ord(n[i])-s+26))
         a.append(code[i]) 
      
      else:
         code = n.replace(n[i],chr(ord(n[i])-s))
         a.append(code[i])  
   return print(''.join(a))
