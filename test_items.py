def test_store_button(browser):
  link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
  browser.get(link)
  button = browser.find_elements_by_css_selector('button[type="submit"].btn-add-to-basket')
  assert button
