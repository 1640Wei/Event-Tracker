import requests
import socket


def set_dns(server_ip):
    # Set DNS server
    socket.create_connection((server_ip, 53), timeout=10)
    socket.setdefaulttimeout(10)


def get_nasa_events():
    # Using Google's public DNS server
    dns_server = "8.8.8.8"
    set_dns(dns_server)


    # Set up the URL for accessing the EONET API.
    api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    try:
        response = requests.get(api_url)


        if response.status_code == 200:
            data = response.json()
            events = data.get("events", [])


            for event in events:
                print("Event name:", event.get("title"))


                # Category
                categories = event.get("categories", [])
                if categories:
                    category_title = categories[0].get("title")
                    print("Category:", category_title if category_title else "Unknow")


                # Source
                sources = event.get("sources", [])
                if sources:
                    source_id = sources[0].get("id")
                    source_url = sources[0].get("url")
                    print(f"Source: {source_id} ({source_url})" if source_id and source_url else "Source: Unknown")


               # Coordinates and Date
                geometry = event.get("geometry", [])
                if geometry:
                    coordinates = geometry[0].get("coordinates", [])
                    date = geometry[0].get("date")
                    print(f"Coordinates: {coordinates}" if coordinates else "Coordinates: Unknown")
                    print(f"Date: {date}" if date else "Date: Unknown")


                print("----------------------------------")
        else:
            print("Unable to retrieve data, error code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    get_nasa_events()
