#! /usr/bin/python3

def checkVowel(n):
   match n:
      case 'a': return "Vowel alphabet"
      case 'e': return "Vowel alphabet"
      case 'i': return "Vowel alphabet"
      case 'o': return "Vowel alphabet"
      case 'u': return "Vowel alphabet"
      case _: return "Simple alphabet"
ch = ''; 
ch = input('Enter the char :')
print (checkVowel(ch))
ch = input('Enter the char :')
print (checkVowel(ch))
ch = input('Enter the char :')
print (checkVowel(ch))
