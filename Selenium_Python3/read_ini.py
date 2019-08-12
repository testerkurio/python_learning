import configparser

cf = configparser.ConfigParser()
cf.read("D:/kurio/Code/workspace/python_learning/Selenium_Python3/config/LocalElement.ini")
print(cf.get("RegsiterElement","user_email"))