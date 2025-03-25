from selenium import webdriver  # (1) 导入 Selenium 的 WebDriver 模块
browser = webdriver.Chrome()    # (2) 启动 Chrome 浏览器
browser.get('http://localhost:8000')  # (3) 访问本地 Django 开发服务器（端口 8000）
assert 'Django' in browser.page_source  # (4) 检查页面是否包含 "Django" 文本