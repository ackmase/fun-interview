"""Given a string return the longest palindrome that can be constructed by removing or shuffling characters. 

Example: 
'aha' -> 'aha' 
'ttaatta' -> ' ttaaatt' 
'abc' -> 'a' or 'b' or 'c' 
'gggaaa' -> 'gaaag' or 'aggga' 

Note if there are multiple correct answers you only need to return 1 palindrome.
"""

def IsEven(number):
  return len(word) % 2 == 0
  
def FindLengthOfString(char_to_count):
  return sum([count for char_to_count.itervalues()])
  
def FindOddCountChar(char_tO_count):
  for char, count in char_tO_count.iteritems():
    if not IsEven(count):
      return char
  return None
  
def CreatePalindrome(word):
  char_to_count = {}
  
  # Tally up the number of each character.
  for char in word:
    if char in char_to_count:
      char_to_count[char] += 1
    else:
      char_to_count[char] = 1
      
  # Remove characters as necessary to form a palindrome.
  found_odd_count = False
  for char, count in char_to_count.iteritems():
    if not IsEven(count) or found_odd_count:
      char_to_count[char] = count - 1
    else:
      found_odd_count = True
      
  # Now form the palindrome with the letters remaining.
  palindrome = []
  odd_count_char = FindOddCountChar(char_to_count)
  if odd_count_char:
    palindrome = [odd_count_char for index in range(char_to_count[char])]
  for char, count in char_to_count.iteritems():
    if char != odd_count_char:
      halved_list = [char for index in range(count / 2)]
      palindrome = halved_list + palindrome + halved_list
  
  return str(palindrome)
      
  
