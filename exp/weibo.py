from plugin import plugin
import requests
import sys
import socket

class exploit(plugin): 
    def __init__(self,custom_log_dir,args):
        plugin.__init__(self,custom_log_dir,args)
    
    def req(self,url):
        headers = {}
        headers["Referer"] = """https://weibo.com/signup/signup.php"""
        r = requests.get(url, headers=headers,timeout=self.timeout)
        text=r.content.encode("utf-8")
        print(text)
        res=eval(text.replace("true","True").replace("false","False"))
        self.log("weibo.response",str(res))
        return res
        
    def probe_phone(self):
        msg = None
        url="""https://www.weibo.com/signup/v5/formcheck?type=mobilesea&zone=0086&value={0}&from=&__rnd=1553587599510""".format(self.username)
        res = self.req(url)
        if "btn_login" in res["data"]["msg"]:
           ret = True
        elif res["code"] == "600001" and res["data"]["type"]=="err":
           ret = False
           msg = res["data"]["msg"]
        else:
           ret = False
           msg = "not registered"
        return ret,msg
        
    def probe_email(self):
        msg = None
        url="""https://www.weibo.com/signup/v5/formcheck?type=email&value={0}&__rnd=1553592099837""".format(self.username)
        res = self.req(url)
        if "btn_login" in res["data"]["msg"]:
           ret = True
        elif res["code"] == "600001" and res["data"]["type"]=="err":
           ret = False
           msg = res["data"]["msg"]
        else:
           ret = False
           msg = "not registered"
        return ret,msg
        
def main():
    print exploit('./',('15222070607',)).probe()
    print exploit('./',('rrrr',)).probe()
    
if __name__ == '__main__':
    main()