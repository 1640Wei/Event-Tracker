import requests
import socket


def set_dns(server_ip):
    # 使用 socket 设置 DNS 服务器
    socket.create_connection((server_ip, 53), timeout=10)
    socket.setdefaulttimeout(10)


def get_nasa_events():
    # 设置你想要使用的 DNS 服务器，这里以 Google DNS 为例
    dns_server = "8.8.8.8"
    set_dns(dns_server)

    api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            events = data.get("events", [])

            for event in events:
                print("事件名稱:", event.get("title"))

                # 處理類別
                categories = event.get("categories", [])
                if categories:
                    category_title = categories[0].get("title")
                    print("類別:", category_title if category_title else "未知")

                # 處理來源
                sources = event.get("sources", [])
                if sources:
                    source_id = sources[0].get("id")
                    source_url = sources[0].get("url")
                    print(f"來源: {source_id} ({source_url})" if source_id and source_url else "來源: 未知")

                # 處理座標和日期
                geometry = event.get("geometry", [])
                if geometry:
                    coordinates = geometry[0].get("coordinates", [])
                    date = geometry[0].get("date")
                    print(f"座標: {coordinates}" if coordinates else "座標: 未知")
                    print(f"日期: {date}" if date else "日期: 未知")

                print("----------------------------------")
        else:
            print("無法取得數據，錯誤碼:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("發生錯誤:", e)


if __name__ == "__main__":
    get_nasa_events()
