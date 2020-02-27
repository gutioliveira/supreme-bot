from selenium import webdriver
from selenium.webdriver.common.by import By
from config import keys
import time

def get_attrs(object):
	return filter(lambda m: callable(getattr(object, m)), dir(object))

def login():
	driver.find_element_by_xpath('//*[@id="client-email"]').send_keys(keys['email'])
	driver.find_element_by_xpath('//*[@id="cryptosenha"]').send_keys(keys['password'])
	driver.find_element_by_xpath('//*[@id="login"]').click()
	time.sleep(5)

def find_products():
	driver.get('https://www.maze.com.br/pesquisa/?p=' + keys['search_key'])
	element = driver.find_element_by_xpath('//*[@id="center-middle"]/article')
	for e in element.find_elements(By.TAG_NAME, "li"):
		for c in keys['target']:
			if (c.lower() in e.text.lower()):
				return e.click()
	find_products()

def select_size(url=None):
	if url:
		driver.get(url)
	element = driver.find_element_by_xpath('//*[@id="variations"]/fieldset/div[2]')
	elements = element.find_elements(By.TAG_NAME, 'span')
	print(len(elements))
	for e in elements:
		if e.get_attribute("innerText") in keys['sizes']:
			E = e.find_elements(By.TAG_NAME, 'input')[0]
			click_element(E);
			return click_element(driver.find_element_by_xpath('//*[@id="btn-buy"]'));
	elements.reverse()
	for e in elements:
		if e.get_attribute("innerText").isdigit():
			E = e.find_elements(By.TAG_NAME, 'input')[0]
			click_element(E);
			return click_element(driver.find_element_by_xpath('//*[@id="btn-buy"]'));

def checkout():
	print('checkout')
	click_element(find_element_by_xpath('//*[@id="middle"]/div/div/form/div/fieldset/input[1]'))
	if keys['payment_method'] == 'credit_card':
		credit_card()
	else:
		slip()

def credit_card():
	driver.get('https://www.maze.com.br/seguro/checkout/easy#payment/creditcard') #
	# time.sleep(1)
	card_number = find_element_by_xpath('//*[@id="form-checkout"]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div[1]/div[1]/input')
	send_keys(card_number, keys['credit_card_number'])

	name = find_element_by_xpath('//*[@id="form-checkout"]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div/div/input')
	send_keys(name, keys['credit_card_name'])

	month = find_element_by_xpath('//*[@id="form-checkout"]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[1]/div/div/select[1]')
	send_keys(month, keys['credit_card_month'])

	year = find_element_by_xpath('//*[@id="form-checkout"]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[1]/div/div/select[2]')
	send_keys(year, keys['credit_card_year'])

	cvv = find_element_by_xpath('//*[@id="form-checkout"]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/input')
	send_keys(cvv, keys['credit_card_cvv'])

	parcelamento = find_element_by_xpath('//*[@id="form-checkout"]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[4]/div/div/div/select')
	send_keys(parcelamento, keys['parcelamento'])

	if not keys['test']:
		click_element(driver.find_element_by_xpath('//*[@id="form-checkout-submit"]'))

def slip():
	driver.get('https://www.maze.com.br/seguro/checkout/easy#payment/paymentslip')
	if not keys['test']:
		click_element(find_element_by_xpath('//*[@id="form-checkout-submit"]'))


## aux methods
def click_element(e):
	print('click()' + e.get_attribute("innerText"))
	try:
		e.click()
	except:
		time.sleep(.100)
		click_element(e)

def find_element_by_xpath(string):
	print('find_element ' + string)
	try:
		return driver.find_element_by_xpath(string)
	except:
		time.sleep(.100)
		return find_element_by_xpath(string)

def send_keys(obj, string):
	try:
		obj.send_keys(string)
	except:
		time.sleep(.100)
		send_keys(obj, string)


if __name__ == '__main__':
        # load chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path='./chromedriver', options=options)

    # get product url
    driver.get(
    	'https://www.maze.com.br/painel-de-controle'
    	# 'https://www.maze.com.br/tenis-nike-sb-dunk-high-pro-truck-it-preto-p9028/'
    	)

    login()
    find_products()
    select_size(
    	# 'https://www.maze.com.br/tenis-nike-sb-dunk-high-pro-truck-it-preto-p9028/'
    	)

    checkout()


    # https://www.maze.com.br/seguro/checkout/easy#payment/paymentslip
