from selenium import webdriver

brower = webdriver.Firefox()


# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
brower.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in brower.title

# She is invited to enter a to-do item straight away
