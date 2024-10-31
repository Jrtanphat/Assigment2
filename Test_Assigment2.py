import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_valid(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(10)
    driver.get("https://demo.opencart.com/")
    time.sleep(10)
    # Mở menu dropdown
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    time.sleep(5)  # Đợi cho đến khi dropdown xuất hiện
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click()
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("tanphatrey510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("147258369P")
    time.sleep(3)
    # Gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(3)


def test_login_invalid(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(10)
    driver.get("https://demo.opencart.com/")
    time.sleep(10)
    # Mở menu dropdown
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    time.sleep(5)  # Đợi cho đến khi dropdown xuất hiện
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click()
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("tanphatrey510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    time.sleep(3)
    # Gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(3)

def test_logout(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(5)
    driver.find_element(By.NAME, "email").send_keys("tanphatrey510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("147258369P")
    time.sleep(3)
    # Gửi biểu mẫu đăng nhập
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    time.sleep(5)
    # Quá trình đăng xuất
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/logout']").click()


def test_form_submission(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(5)
    driver.find_element(By.NAME, "email").send_keys("tanphatrey510@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(3)
    # Kiểm tra thông báo sau khi gửi biểu mẫu
    message = driver.find_element(By.ID, "alert").text
    assert "Warning: No match for E-Mail Address and/or Password." in message


def test_navigation(driver):
    driver.get("https://demo.opencart.com/home")
    time.sleep(7)
    driver.find_element(By.LINK_TEXT, "About Us").click()
    time.sleep(7)
    assert "About Us" in driver.title
    time.sleep(7)
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(7)
    assert "Contact Us" in driver.title


def test_data_validation(driver):
    # Tìm sản phẩm MacBook
    driver.get("https://demo.opencart.com/home")
    time.sleep(5)
    macbook_element = driver.find_element(By.XPATH, "//a[text()='MacBook']")
    # Kiểm tra tên sản phẩm
    assert macbook_element.text == "MacBook", "Tên sản phẩm không khớp!"
    # Kiểm tra giá của sản phẩm MacBook
    macbook_price_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/div/span[1]")
    macbook_price = macbook_price_element.text.split("\n")[0]  # Lấy giá đầu tiên (không bao gồm thuế)
    assert macbook_price == "$602.00", "Giá của MacBook không khớp!"
    # Kiểm tra mô tả của sản phẩm MacBook
    macbook_description_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/p")
    macbook_description = macbook_description_element.text

    expected_description = "Intel Core 2 Duo processor"

    assert expected_description in macbook_description, "Mô tả chứa thông tin mong đợi!"

    print("Tất cả dữ liệu sản phẩm MacBook đã được xác thực thành công!")


def test_add_to_cart(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(10)
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]").click()
    time.sleep(10)
    driver.find_element(By.LINK_TEXT, "Shopping Cart").click()
    time.sleep(5)

@pytest.mark.usefixtures("driver")  # Sử dụng fixture driver đã định nghĩa
def login(driver):
    # Mở trang đăng nhập
    driver.get("https://demo.opencart.com/index.php?route=account/login")

    # Khởi tạo WebDriverWait với thời gian chờ tối đa
    wait = WebDriverWait(driver, 10)  # Thay đổi 10 thành thời gian chờ tối đa bạn mong muốn

    # Chờ cho trường email có thể nhìn thấy và nhập email
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    email_field.send_keys("tanphatrey510@gmail.com")

    # Chờ cho trường mật khẩu có thể nhìn thấy và nhập mật khẩu
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    password_field.send_keys("147258369P")

    time.sleep(10)  # Chờ trang tải xong

    # Chờ cho nút đăng nhập có thể nhấp được và nhấn
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()

    # Chờ cho việc đăng nhập hoàn tất (kiểm tra tiêu đề trang hoặc một phần tử nào đó)
    wait.until(EC.title_contains("My Account"))  # Kiểm tra tiêu đề trang nếu đăng nhập thành công


def test_checkout_valid_info(driver):
    # login
    login(driver)
    # Choose product to add
    driver.get("https://demo.opencart.com/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(driver, 10)

    time.sleep(10)  # wait loading page
    # Add to cart
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(10)  # wait loading page

    # Go to cart
    driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

    time.sleep(10)  # wait for update update

    # Chọn nút thanh toán
    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
    checkout_button.click()

    time.sleep(10)

    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-firstname"))).send_keys("John")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-lastname"))).send_keys("Doe")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-address-1"))).send_keys("123 Main St")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-city"))).send_keys("New York")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-postcode"))).send_keys("10001")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-country"))).send_keys("United States")
    wait.until(EC.visibility_of_element_located((By.ID, "input-payment-zone"))).send_keys("New York")

    # Choose payment method
    payment_method_radio = wait.until(EC.element_to_be_clickable((By.NAME, "payment_method")))
    payment_method_radio.click()

    # Confirm order
    confirm_order_button = wait.until(EC.element_to_be_clickable((By.ID, "button-confirm")))
    confirm_order_button.click()

    success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    assert "Your order has been placed!" in success_message.text


def test_search_functionality(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(5)
    driver.find_element(By.NAME, "search").send_keys("Iphone")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    time.sleep(8)
    # Kiểm tra kết quả tìm kiếm
    assert "Search - Iphone" in driver.title


@pytest.mark.parametrize("size", [(800, 600), (1024, 768), (1920, 1080)])
def test_responsive_design(driver, size):
    driver.set_window_size(*size)
    driver.get("https://demo.opencart.com/")
    time.sleep(5)
    # Kiểm tra bố cục hoặc các phần tử cụ thể cho tính năng phản hồi
    element = driver.find_element(By.ID, "logo")
    assert element.is_displayed()
