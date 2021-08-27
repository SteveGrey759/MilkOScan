# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:09:33 2018

@author: Admin
"""


#frequency of letters in english
# =============================================================================
# e	12.702%	
# t	9.056%	
# a	8.167%	
# o	7.507%	
# i	6.966%	
# n	6.749%	
# s	6.327%	
# h	6.094%	
# r	5.987%	
# d	4.253%	
# l	4.025%	
# c	2.782%	
# u	2.758%	
# m	2.406%	
# w	2.360%	
# f	2.228%	
# g	2.015%	
# y	1.974%	
# p	1.929%	
# b	1.492%	
# v	0.978%	
# k	0.772%	
# j	0.153%
# x	0.150%	
# q	0.095%	
# z	0.074%
# =============================================================================




#turn into a dictionary?
freqLetter = {e:12.702	,
 t:	9.056,
 a:	8.167,
 o:	7.507,
 i:	6.966,
 n:	6.749,
 s:	6.327,
 h:	6.094,
 r:	5.987,
 d:	4.253,
 l:	4.025,
 c:	2.782,
 u:	2.758,
 m:	2.406,
 w:	2.360,
 f:	2.228,
 g:	2.015,
 y:	1.974,
 p:	1.929,
 b:	1.492,
 v:	0.978,
 k:	0.772,
 j:	0.153,
 x:	0.150	,
 q:	0.095	,
 z:	0.074}

print (freqLetter)


newAlpha = {1:'i', 2:'t',3:'e',4:'a',5:'s',6:'b',7:'v',8:'b', 9:'n' }


alphabet = "abcdefghijklmnopqrstuvwxyz"

missing = ""

print(newAlpha.values())

 
for char in alphabet:
    if not char in newAlpha.values():
        missing += char
        
#print([1,2,3,4]-[2,3])
     
        
print(alphabet)     
print (missing)


from nltk.corpus import wordnet

#if not wordnet.synsets(word_to_test):
#  print("not a word")
#else:
#  print("a valid word")
  
  
  #example case of functionality
# =============================================================================
#   DNA 7x compression by nucleosome, 100-10,000 compression to fit in cell
#   7100140 (4 0's), special character for this kind of compression? e.g. h, r
#use r (repeat)
#   translates into  71001r40   
  # into v
#  
  
# =============================================================================












