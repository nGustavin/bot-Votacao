import requests
import time
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


geckodriver_autoinstaller.install()

url = 'https://afazenda.r7.com/a-fazenda-12/votacao'

option = Options()
option.headless = True
driver = webdriver.Firefox(options = option)

driver.get(url)
time.sleep(0.5)

openVoteSection = driver.find_element_by_class_name('voting-button--hidden').click()
selectCandidate = driver.find_element_by_id('633').click()


def handleVote():

  voteButton = driver.find_element_by_class_name('voting-button.voting-button--medium.disabled').click()
  time.sleep(0.8)
  revoteButton = driver.find_element_by_class_name('voting-button.vote-confirmation__button').click()
  time.sleep(0.6)
  selectCandidate = driver.find_element_by_id('633').click()


count = 0

while True:
  handleVote()
  count += 1
  print(count, 'votes')


driver.quit()

