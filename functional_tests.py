from selenium import webdriver

brower = webdriver.Firefox()
brower.get('http://localhost:8080')

assert 'Django' in brower.title
