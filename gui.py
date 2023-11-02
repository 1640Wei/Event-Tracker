import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

def get_nasa_events(start_date, end_date):
    api_url = f"https://eonet.sci.gsfc.nasa.gov/api/v3/events?start_date={start_date}&end_date={end_date}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        events = data.get("events", [])

        for event in events:
            print("事件名稱:", event.get("title"))
            print("位置:", event.get("geometry", {}).get("coordinates"))
            print("發生時間:", event.get("geometries", [{}])[0].get("date"))
            print("類型:", event.get("categories", [])[0].get("title"))
            print("----------------------------------")

            # 在這裡你可以處理圖片的顯示，例如：
            image_url = event.get("links", {}).get("image", "")
            display_image(image_url)

    else:
        print("無法取得數據，錯誤碼:", response.status_code)

def display_image(image_url):
    if image_url:
        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))

        # 使用 tkinter 來顯示圖片
        img = img.resize((300, 300))  # 調整圖片大小
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
        image_label.pack()

# 提交按鈕的事件處理函數
def on_submit():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    # 在這裡你可以使用日期區間去呼叫 get_nasa_events 函數
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

# 創建顯示圖片的標籤
image_label = Label(root)
image_label.pack()

# 啟動主循環
root.mainloop()

