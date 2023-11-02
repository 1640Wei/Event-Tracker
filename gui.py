import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import socket


def set_dns(server_ip):
   # 使用 socket 设置 DNS 服务器
   socket.create_connection((server_ip, 53), timeout=10)
   socket.setdefaulttimeout(10)




def get_nasa_events(start_date, end_date):
    dns_server = "8.8.8.8"
    set_dns(dns_server)


    api_url = f"https://eonet.gsfc.nasa.gov/api/v3/events?start={start_date}&end={end_date}"
    response = requests.get(api_url)


    if response.status_code == 200:
        data = response.json()
        events = data.get("events", [])


        if not events:
            print("沒有可用數據。")
            return


        for event in events:
            print("事件名稱:", event.get("title"))
            coordinates = event.get("geometry", [{}])[0].get("coordinates")
            date = event.get("geometries", [{}])[0].get("date")
            print("位置:", coordinates if coordinates else "未提供")
            print("發生時間:", date if date else "未提供")
            print("類型:", event.get("categories", [{}])[0].get("title"))
            print("----------------------------------")
    else:
        print("無法取得數據，錯誤碼:", response.status_code)








def display_image(image_url):
   response = requests.get(image_url)
   img_data = response.content
   img = Image.open(BytesIO(img_data))
   img.show()




def on_submit():
   start_date = start_date_entry.get()
   end_date = end_date_entry.get()


   get_nasa_events(start_date, end_date)




# 創建主窗口
root = Tk()
root.title("NASA Events Tracker")


# 創建日期輸入框
Label(root, text="Start Date (YYYY-MM-DD):").pack()
start_date_entry = Entry(root)
start_date_entry.pack()


Label(root, text="End Date (YYYY-MM-DD):").pack()
end_date_entry = Entry(root)
end_date_entry.pack()


# 創建提交按鈕
submit_button = Button(root, text="Submit", command=on_submit)
submit_button.pack()


# 啟動主循環
root.mainloop()

