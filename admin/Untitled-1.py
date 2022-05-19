print("Name: Pushpinder Singh ||Uid:20BCS7300")
def add_string(str1):
 length = len(str1)
 #check if string has atleast size 3 
 if length > 2:
     #check if "ing" is present at end of string
  if str1[-3:] == 'ing':
      #if present then add "ly" at end
   str1 += 'ly'
  else:
      #else add "ing" at end
   str1 += 'ing'
   #returning new string
 return str1

print(add_string('ab'))
print(add_string('spac'))
print(add_string('bing'))
