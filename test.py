import sys
import os

def Login(theprint = True):
    global fini
    if(theprint):
        spinner.start("Logging into account\n")
    global session    
    session = requests.Session()
    
#Get info from accounts.txt

with open('accounts.txt', 'r') as f:
    account_list = f.readlines()

for account in account_list:
    print(account.strip())
   
    
    checkemail = session.post("https://login.live.com/GetCredentialType.srf",json=checkJson,verify=False,headers=headers)
    
    dataPost = {"i13" : "0", "login" : email, "loginfmt" : email, "type" : "11", "LoginOptions" : "3", "lrt" : "", "lrtPartition" : "", "hisRegion" : "", "hisScaleUnit" : "", "passwd" : password, "ps" : "2", "psRNGCDefaultType" : "", "psRNGCEntropy" : "", "psRNGCSLK" : "", "canary" : "", "ctx" : "", "hpgrequestid" : "", "PPFT" : flowToken, "PPSX" : "Passpor", "NewUser" : "1", "FoundMSAs" : "", "fspost" : "0", "i21" : "0", "CookieDisclosure" : "0", "IsFidoSupported" : "1", "i2" : "1", "i17" : "0", "i18" : "", "i19" : "1668743"}
   
    
    if not keyExist(session.cookies,'PPAuth'):
        sys.exit("Couldn't log in")
