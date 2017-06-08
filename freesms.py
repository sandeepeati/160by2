from selenium import webdriver

class freesms:

    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = pwd

    def sendsms(self, pno, msg):

        # initiating selenium webdriver

        driver = webdriver.Chrome()

        # opening url
        driver.get('http://www.160by2.com/Index')

        # logging in
        try:
            driver.find_element_by_name('username').send_keys(self.uname)
            driver.find_element_by_name('password').send_keys(self.pwd)

            driver.find_element_by_class_name('ind-reg-but').click()
        except:
            print('Wrong uname or password')

        handle = driver.window_handles

        driver.switch_to_window(handle[0])

        driver.switch_to_frame('by2Frame')

        driver.implicitly_wait(40)

        # navigating to sms frame
        driver.find_element_by_name('frmDashboard').find_element_by_class_name('da-sms-btn').click()

        driver.switch_to_default_content()
        driver.switch_to_frame('by2Frame')

        try:
            # this is where recipient phone number goes
            driver.find_element_by_xpath("//input[@placeholder='Enter Mobile Number or Name']").send_keys(pno)

            # this is where sms msg goes
            driver.find_element_by_xpath("//textarea[@placeholder='Enter your message']").send_keys(msg)

            driver.find_element_by_id('btnsendsms').click()

            confirm = driver.find_element_by_id('showLate').text

            driver.close()
        except:
            print('Message could not be send...Try again...')


