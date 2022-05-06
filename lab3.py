import ipaddress
import platform
def palindrome(text):

   word_list = []
   temp = ''
   for i, v in enumerate(text): 
   if v.isalpha(): 
   temp += v
   if i == len(text) - 1 and temp.isalpha():
   word_list.append(temp) 
   else: 
      
   word_list.append(temp)
   temp = ''
    pal_words = []
    for i in word_list:
    reversed_word = i[::-1]  
    if len(i) < 3:
    break
    
    if reversed_word == i:  
    pal_words.append(i)
    return pal_words
  
palindrome("abc ada abba a")
def validate_ip(ip_address):
    ip_validate = False
    try:
    ip = ipaddress.ip_address(ip_address)
    ip_validate = True
    except ValueError:
    ip_validate = False

    return ip_validate
validate_ip("192.168.1.31")
validate_ip("192.168.1.25")
def get_os():
    return platform.system()
get_os()
