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
            
check_chromedriver()