import psutil
import pygetwindow as gw
import time
import os
import platform

def close_tab(title_keywords):
    windows = gw.getAllTitles()
    for window in windows:
        if any(keyword.lower() in window.lower() for keyword in title_keywords):
            window_obj = gw.getWindowsWithTitle(window)[0]
            print(f"close: {window}")
            window_obj.close()

def main():
    title_keywords = ["instagram", "youtube shorts"]
    try:
        while True:
            close_tab(title_keywords)
            time.sleep(5)  # check every 5 sec
    except KeyboardInterrupt:
        print("\nclosed by user")

if __name__ == "__main__":
    main()
