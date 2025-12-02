# 在代码中添加调试信息
import os
import stat

def check_chromedriver():
    driver_path = "./chromedriver/chromedriver"
    print(f"ChromeDriver 路径: {driver_path}")
    print(f"文件是否存在: {os.path.exists(driver_path)}")
    
    if os.path.exists(driver_path):
        # 检查权限
        st = os.stat(driver_path)
        print(f"权限: {oct(st.st_mode)}")
        print(f"可执行: {os.access(driver_path, os.X_OK)}")
        
        # 尝试执行
        import subprocess
        try:
            result = subprocess.run([driver_path, "--version"], 
                                  capture_output=True, text=True)
            print(f"ChromeDriver 版本: {result.stdout}")
        except Exception as e:
            print(f"执行失败: {e}")
            
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_chromedriver_basic():
    try:
        # 配置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无头模式，不显示浏览器窗口
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--verbose')
        
        # 创建Service对象（指定chromedriver路径）
        service = Service('./chromedriver/chromedriver')  # 如果chromedriver不在PATH中
        
        # 启动浏览器
        #driver = webdriver.Chrome(options=chrome_options)  # 如果chromedriver在PATH中
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # 测试访问网页
        test_urls = [
            "https://www.baidu.com",
            "https://www.python.org"
        ]
        
        for url in test_urls:
            try:
                print(f"正在访问: {url}")
                driver.get(url)
                time.sleep(2)  # 等待页面加载
                
                # 验证页面是否成功加载
                title = driver.title
                print(f"✓ 成功访问 {url}")
                print(f"  页面标题: {title}")
                print(f"  当前URL: {driver.current_url}")
                print("-" * 50)
                
            except Exception as e:
                print(f"✗ 访问 {url} 失败: {str(e)}")
        
        # 测试基本操作
        print("\n测试基本浏览器操作...")
        driver.get("https://www.example.com")
        
        # 测试页面元素查找
        elements = driver.find_elements("tag name", "h1")
        print(f"找到 {len(elements)} 个h1标签")
        
        # 测试JavaScript执行
        result = driver.execute_script("return document.title;")
        print(f"通过JavaScript获取的标题: {result}")
        
        # 测试截图功能
        driver.save_screenshot("test_screenshot.png")
        print("✓ 截图已保存为 test_screenshot.png")
        
        print("\n✅ ChromeDriver 运行正常！")
        
    except Exception as e:
        print(f"❌ ChromeDriver 测试失败: {str(e)}")
        
    finally:
        # 确保关闭浏览器
        try:
            driver.quit()
            print("浏览器已关闭")
        except:
            pass

if __name__ == "__main__":
    check_chromedriver()
    test_chromedriver_basic()