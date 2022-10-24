import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')

        os.system('xdg-open https://www.facebook.com/KAyNAT.BabY')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from public import Subscription
 
        Subscription()
 
        
