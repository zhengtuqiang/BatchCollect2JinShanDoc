# -*- coding: UTF-8 -*-
import tkinter as tk
import time,pyautogui,webbrowser,sys
root = tk.Tk()
root.title("金山文档批量收藏工具")
def saveInternal(links):  
    interval=3   
    waitInterval = 5
    try:            
        for link in links:                
            webbrowser.open_new_tab(link)
            print("打开："+link)           
            time.sleep(waitInterval)
            if sys.platform == 'darwin':
                pyautogui.hotkey('option', 'r')
            elif sys.platform == 'win32':
                pyautogui.hotkey('alt', 'r')
            print("保存")  
            time.sleep(interval)       

    except KeyboardInterrupt:            
        print("Stopping tab switcher...")            
 

# 创建一个Text组件
text_box = tk.Text(root, height=10)
text_box.pack()
def validateData(it):
    return it.startswith("http")
def patchSave():
    links = list(filter(validateData,text_box.get("1.0", "end-1c").split("\n")))
    print("有效链接数量：%d\n" %len(links))
    print(links)
    if len(links) > 0:
        saveInternal(links)


# # 创建按钮并绑定事件处理函数
button = tk.Button(root, text="收藏", command=patchSave)
button.pack()
root.mainloop()
