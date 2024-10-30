# Hướng Dẫn Thiết Lập Môi Trường và Chạy Kịch Bản Selenium với Edge

## Giới Thiệu

Tệp hướng dẫn này mô tả cách thiết lập môi trường để chạy các kịch bản kiểm thử tự động hóa bằng **Selenium** và **Microsoft Edge**, sử dụng **pytest** làm framework kiểm thử. Bạn sẽ học cách cài đặt các công cụ cần thiết, cấu hình WebDriver cho trình duyệt Edge, và cách chạy các bài kiểm tra.

## Yêu Cầu Hệ Thống

Trước khi bắt đầu, đảm bảo rằng bạn có các công cụ sau:
1. **Python 3.7+**: Bạn có thể tải Python tại [python.org](https://www.python.org/downloads/).
2. **Microsoft Edge**: Phiên bản mới nhất của trình duyệt Edge.
3. **Edge WebDriver**: WebDriver để điều khiển trình duyệt Edge, bạn có thể tải nó từ [trang WebDriver của Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
4. **pip**: Công cụ quản lý gói của Python (thường được cài sẵn với Python).

## Bước 1: Cài đặt Python và pip

Kiểm tra xem Python và pip đã được cài đặt chưa bằng cách chạy các lệnh sau trong terminal:

```bash
python --version
pip --version
```
## Bước 2: Cài Đặt Các Thư Viện Cần Thiết

Sử dụng `pip` để cài đặt các thư viện cần thiết cho dự án của bạn. Các thư viện cơ bản bao gồm:

- **Selenium**: Thư viện chính để tự động hóa các trình duyệt web.
- **pytest**: Thư viện để viết và chạy các bài kiểm tra.

Mở terminal hoặc command prompt và chạy lệnh sau:

```bash
pip install selenium pytest
```
## Bước 3: Tải Về và Cấu Hình Edge WebDriver

### Tải Về Edge WebDriver

1. Truy cập [trang WebDriver của Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
2. Tải về phiên bản Edge WebDriver tương ứng với phiên bản trình duyệt Edge mà bạn đang sử dụng.

### Cấu Hình Edge WebDriver

1. Sau khi tải về, giải nén tệp tải về.
2. Lưu tệp giải nén vào một thư mục mà bạn có thể truy cập dễ dàng.

### Thêm Đường Dẫn vào Biến Môi Trường PATH

Để cấu hình Edge WebDriver, bạn cần thêm đường dẫn đến thư mục chứa WebDriver vào biến môi trường PATH của hệ thống. 

**Ví dụ trên Windows:**

1. Kích chuột phải vào **This PC** và chọn **Properties**.
2. Chọn **Advanced system settings**.
3. Nhấn vào **Environment Variables**.
4. Trong phần **System variables**, tìm và chọn **Path**, sau đó nhấn **Edit**.
5. Nhấn vào **New** và thêm đường dẫn đến thư mục chứa Edge WebDriver của bạn.
6. Nhấn **OK** để lưu thay đổi.

## Bước 3: Chạy Kịch Bản Kiểm Thử

Để chạy các kịch bản kiểm thử sử dụng `pytest`, bạn chỉ cần mở terminal và chạy lệnh sau trong thư mục chứa tệp kiểm thử:

```bash
pytest -v
```
- **-v**: Hiển thị chi tiết từng bài kiểm tra.

Nếu mọi thứ được thiết lập đúng, bạn sẽ thấy kết quả kiểm thử trong terminal, hiển thị thành công hoặc thất bại của từng bài kiểm tra.

### Ví dụ về Kết Quả

Khi bạn chạy lệnh kiểm thử, bạn có thể thấy kết quả như sau:

```bash
============================= test session starts ==============================
collected 1 item                                                               

test_data_validation.py::test_macbook_data_validation PASSED              [100%]

============================== 1 passed in 3.45s ===============================
```
Nếu xảy ra lỗi, pytest sẽ cung cấp thông tin chi tiết về vị trí và nguyên nhân gây lỗi.
## Bước 4: Khắc phục sự cố

- Edge WebDriver không khớp với phiên bản Edge: Kiểm tra phiên bản trình duyệt Edge và đảm bảo rằng bạn đã tải đúng phiên bản Edge WebDriver tương ứng.
- Lỗi không tìm thấy WebDriver: Đảm bảo rằng bạn đã thêm đường dẫn đến WebDriver vào biến môi trường PATH.
  
## Tài liệu tham khảo

- Tài liệu Selenium: https://www.selenium.dev/documentation/
- Tài liệu pytest: https://docs.pytest.org/
