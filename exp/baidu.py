#coding=utf-8
from plugin import plugin
import requests
import time

class exploit(plugin): 
    def __init__(self,custom_log_dir,args):
        plugin.__init__(self,custom_log_dir,args)
    
    def req(self,url):
        headers = {}
        headers["User-Agent"] = """Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"""
        r = requests.get(url, headers=headers,timeout=self.timeout)
        text=r.content
        res=eval(text)
        self.log("baidu.response",str(res))
        return res
    
    def probe_phone(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        if  __name__ != "__main__":
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        url = "https://passport.baidu.com/v2/?reg"
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__phone"]')
        elem.send_keys(self.username)
        elem = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__isAgree"]')
        elem.click()
        time.sleep(2)
        result = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__phoneSucc"]')
        style = result.get_attribute('style')
        if __name__ == "__main__":
            driver.save_screenshot('baidu.png')
        driver.close()
        if style == 'display: inline;':
            ret = False
            msg = "not registered"
        elif style == 'display: none;':
            ret = True
            msg = "registered"
        return ret,msg
        
    def probe_nickname(self):
        url="https://passport.baidu.com/v2/?regnamesugg&token=&tpl=mn&apiver=v3&tt=1553597312588&gid=&username={0}&traceid=&callback=".format(self.username)
        res = self.req(url)
        if res["data"]["userExsit"]=="1":
           ret = True
           msg = "registered"
        else:
           ret = False
           msg = "not registered"
        return ret,msg
        
def main():
    print exploit('./',('13603854766',)).probe()
    print exploit('./',('13260277899',)).probe()
    print exploit('./',('rrrr',)).probe()
    print exploit('./',('HeHH',)).probe()
    
if __name__ == '__main__':
    main()