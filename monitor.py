import platform
import os

def check_system():
    print("=== System Monitor Started ===")
    # הדפסת פרטי מערכת ההפעלה
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    
    print("\n--- Disk Space Check ---")
    # הרצת פקודת לינוקס דרך פייתון
    os.system("df -h / | grep /")
    
    print("\n=== Check Complete ===")

if __name__ == "__main__":
    check_system()
