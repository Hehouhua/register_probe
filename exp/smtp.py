from plugin import plugin
import socket
import smtplib
debug_level = 0

class exploit(plugin):
    param_count = 2
    timeout = 1
    socket.setdefaulttimeout(timeout)  
    def __init__(self,custom_log_dir,args):
        plugin.__init__(self,custom_log_dir,args)

	#def login(self):
	#	return False,"Not Implement Yet"
	
    def login(self):
        if len(self.args) != self.param_count:
            error_msg = "param_count not matched."
            self.log(__name__,error_msg)
            return False,self.host,self.port,self.args,error_msg
        self.username,self.password = self.args[0],self.args[1]
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.host,self.port)
            smtp.set_debuglevel(debug_level)
            smtp.login(self.username, self.password)
            #print '[+]%s:%s,' %(self.username, self.password)
            smtp.quit()
        except Exception,e:
            self.log(__name__,str(e))
            return False,self.host,self.port,self.args,str(e)
        
if __name__ == '__main__':
    print exploit('./',('mail.xxx.xx.cn','25','xxxx@xxx.xx.cn','xxxxxxxx')).login()