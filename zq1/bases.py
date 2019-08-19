import time
import unittest
import MySQLdb
import ddt
from selenium import webdriver
from selenium.webdriver import ActionChains


@ddt.ddt
class Basic(unittest.TestCase):
    def setUp(self) :
        #初始化
        self.driver = webdriver.Chrome()
        self.driver.get("urlxxx")
        self.driver.maximize_window()
        # 登录
        self.driver.find_element_by_id("loginName").send_keys("xxx")
        self.driver.find_element_by_id("pwd").send_keys("xxx")
        self.driver.find_element_by_id("login-button").click()
        time.sleep(3)
        quit = self.driver.find_elements_by_xpath("//a[contains(@href,'login')]")
        assert quit,"登录失败"
        print("登录成功")
        #连接数据库
        self.db = MySQLdb.connect(
            host='xxx',
            port=3306,
            user='xxx',
            passwd='xxx',
            db='xxx',
        )


    @ddt.file_data("./test.json")
    def test_create(self, number, unpContent):
        #数据驱动的方式进行信息录入
        self.driver.find_elements_by_xpath("//a[text()='不合格品']")[0].click()
        self.driver.find_elements_by_xpath("//cite[text()='信息录入']")[0].click()
        time.sleep(5)
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_id("add").click()
        time.sleep(3)
        a = self.driver.find_elements_by_xpath("//dd[text()='外购件']")[0]
        self.driver.execute_script('$(arguments[0]).click()', a)
        b = self.driver.find_elements_by_xpath("//dd[text()='总装B车间']")[0]
        self.driver.execute_script('$(arguments[0]).click()', b)
        self.driver.find_element_by_id("discoveryDate").click()
        self.driver.find_elements_by_xpath("//span[@lay-type='now']")[0].click()
        c = self.driver.find_elements_by_xpath("//dd[text()='VV7']")[0]
        self.driver.execute_script('$(arguments[0]).click()', c)
        self.driver.find_element_by_id("number").send_keys(number)
        self.driver.find_element_by_id("utilCode").send_keys("M001")
        d = self.driver.find_elements_by_xpath("//dd[@lay-value='物料1']")[0]
        self.driver.execute_script('$(arguments[0]).click()', d)
        self.driver.find_element_by_id("unpContent").send_keys(unpContent)
        self.driver.find_element_by_id("submit_tab1").click()
        time.sleep(3)
        self.driver.switch_to.default_content()
        # qzbcsdb库的up_un_product表
        cursor = self.db.cursor()
        sql = "select * from up_un_product where unp_content = '"+unpContent+"'"
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            print("信息录入成功")
        else:
            print("信息录入失败")





    def tearDown(self):
        #登出
        chain = ActionChains(self.driver)
        implement = self.driver.find_element_by_id("loginname")
        chain.move_to_element(implement).perform()
        quit = self.driver.find_elements_by_xpath("//a[contains(@href,'login')]")[0]
        self.driver.execute_script('$(arguments[0]).click()', quit)
        time.sleep(6)
        quit.click()
        login = self.driver.find_element_by_id("login-button")
        time.sleep(2)
        assert login,"登出失败"
        print("登出成功")
        #关闭
        self.driver.quit()
        self.db.close()

if __name__ == "__main__":
    unittest.main()
