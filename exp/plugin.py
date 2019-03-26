from enum import Enum,unique
@unique
class UsernameType(Enum):
    Phone = 0
    Email = 1
    Nickname = 2
        
class plugin:
    timeout = 2
    def __init__(self,custom_log_dir,args): 
        self.log_dir=custom_log_dir
        self.username = args[0]
        try:
            self.password = args[1]
        except:
            self.password = None
            
    def _write_log(self,filename,msg):
        try:
           with open(filename,'a') as f:
               f.write(msg)
        except:
            pass
            
    def _write_data(self,filename,data):
       try:
          with open(filename,'wb') as f:
              f.write(data)
       except:
           pass
        
    #just use self.log(__name__,"anything") to log anything you want        
    def log(self,filename,msg):
        import time
        now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        param = "%s,%s" % (self.username,self.password)
        self._write_log(self.log_dir+'/'+filename+".log",",".join([now,param,msg])+'\n')
        
    #just use self.save_data(__name__,"1.txt","anything") to write data you want
    def save_data(self,sub_dir,filename,data):
        import os
        if not os.path.exists(self.log_dir+"/"+sub_dir):
            os.makedirs(self.log_dir+"/"+sub_dir)
        self._write_data(self.log_dir+'/'+sub_dir+"/"+filename,data)
        
    def type_of_username(self):
        import re
        if re.match(r"^1[35678]\d{9}$", self.username):
            return UsernameType.Phone
        if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',self.username): 
            return UsernameType.Email
        return UsernameType.Nickname
        
    #return (True/False,self.host,self.port,self.args,"Any string you want to record")
    def probe(self):
        if self.type_of_username() == UsernameType.Phone:
            ret,msg = self.probe_phone()
        if self.type_of_username() == UsernameType.Email:
            ret,msg = self.probe_email()
        if self.type_of_username() == UsernameType.Nickname:
            ret,msg = self.probe_nickname()
        if ret : msg = "registered"
        return ret,self.username,msg

    def probe_phone(self):
        return False,"Phone Detection Not Implement Yet."
        
    def probe_email(self):
        return False,"Email Detection Not Implement Yet."
        
    def probe_nickname(self):
        return False,"Nickname Detection Not Implement Yet."

    #return (True/False,self.host,self.port,self.args,"Any string you want to record")
    def crack(self):
        return False,self.username,self.password,'Password Bruteforce not Implement Yet.'