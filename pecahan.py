import math
import os
def pecornot(x):
 y = int(x)
 if (y < x or x > y):
  return True
 return False

#pangkat terbanyak dalam list dalam list (list dalam list, two dimensional)
def terbanyak(daftar):
 anggota = []
 gabung = []
 maxi = 0
 maxi1 = 0
 for a in daftar:
  for b in a:
   if (not b in anggota):
    anggota.append(b)
 for i in anggota:
  for a in daftar:
    b = a.count(i)
    if b > maxi:
     maxi = b
     maxi1 = i
 return [maxi, maxi1]
def kpk(*nilai):
 pang_ting = []
 result = []
 jadi = 1
 a = 0
 temp = 0
 for i in range(len(nilai)):
  pang_ting.append([])
 for i in nilai:
  while True:
   if (not pecornot(i/2)):
    i/=2
    pang_ting[a].append(2)
   elif (not pecornot(i/3)):
    i/=3
    pang_ting[a].append(3)
   elif (not pecornot(i/5)):
    i/=5
    pang_ting[a].append(5)
   elif (not pecornot(i/7)):
    i/=7
    pang_ting[a].append(7)
   else:
    a+=1
    break
 maxi = 0
 lanjut = 0
 while True:
  #check if pang_ting still have number. remember its two dimensional
  for i in pang_ting:
   if len(i) > 0:
    lanjut = 1
  if lanjut == 0:
   break
  ###
  a = terbanyak(pang_ting)
  """
  print("A:")
  print(a)
  print(pang_ting)"""
  result.append(a[1]**a[0])
  for i in pang_ting:
   try:
    while a[1] in i:
     i.remove(a[1])
   except:
    pass
  lanjut = 0

 #return result
 for i in result:
  jadi *= i
 return jadi
"""
 for a in pang_ting:
  for b in a:
""" 
    
class pecahan:
 def __init__(self, x, y):
  self.x, self.y = x, y
 def __add__(self, other):
  bawah = kpk(self.y, other.y)
  return pecahan((bawah/self.y*self.x) + (bawah/other.y*other.x), bawah)
 def __sub__(self, other):
  bawah = kpk(self.y, other.y)
  return pecahan((bawah/self.y*self.x) - (bawah/other.y*other.x), bawah)
 def nilai(self):
  return(self.x/self.y)
 def __repr__(self):
  return "pecahan(%s, %s)" %(self.x, self.y)
 
 def __mul__(self, other):
  return pecahan(self.x * other.x, self.y*other.y)

 def __truediv__(self, other):
  return pecahan(self.x * other.y, other.x*self.y)
 def __pow__(self, other):
  return pecahan(self.x**other, self.y**other)
 def perkecil(self):
  kemungkinan = [2, 3, 5, 7]
  for i in kemungkinan:
   if ((not pecornot(self.x/i)) and (not pecornot(self.y/i))):
    self.x, self.y = self.x/i, self.y/i
  return pecahan(self.x, self.y)
 
#print(pecahan(10, 5).nilai())
a = pecahan(1, 2)
print(a**8)

#print(kpk(2, 8, 16))
#print(terbanyak([[1, 2, 3], [1, 2, 3, 2, 2, 2], [2, 2, 2]]))

