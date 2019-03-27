import socket
debug_level = 0
timeout = 1
socket.setdefaulttimeout(timeout)  
   
def login(smtphost,smtpport,username,password):
    import smtplib
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtphost,smtpport)
        smtp.set_debuglevel(debug_level)
        smtp.login(username, password)
        #print '[+]%s:%s,' %(username, password)
        smtp.quit()
    except Exception,e:
        return False,str(e)
    return True,None
    
if __name__ == '__main__':
    print login('mail.xxx.xx.cn','25','xxxx@xxx.xx.cn','xxxxxxxx')