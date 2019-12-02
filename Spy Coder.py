n = input()
s = int(input())
def spyCoder(n,s):
   a = []
   for i in range (0,len(n)):
      if (ord(n[i])+s)>= 90 or ord(n[i]) >= 90:
         code = n.replace(n[i],chr(s+ord(n[i])-90+64))
         a.append(code[i]) 
      elif n[i] == ' ':
         a.append(n[i])
      else:
         code = n.replace(n[i],chr(s+ord(n[i])))
         a.append(code[i])  
   return print(''.join(a))
