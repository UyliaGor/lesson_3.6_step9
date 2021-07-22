import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button(browser):
    browser.get(link)
    time.sleep(30)
    element = browser.find_element_by_class_name('btn-add-to-basket')
    assert element, 'Кнопка не найдена'


if __name__ == "__main__":
    test_find_button()





#Решение без assert
#from selenium.common.exceptions import NoSuchElementException
#try:
    #elem = browser.find_element_by_class_name('btn-add-to-basket')
    #return True
#except NoSuchElementException:
     #print('Zero element')
     #return False
