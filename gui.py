import requests
from tkinter import *
import socket


def get_nasa_events(start_date, end_date, dns_server="8.8.8.8"):
    # Set DNS server
    socket.create_connection((dns_server, 53), timeout=10)
    socket.setdefaulttimeout(10)


    api_url = f"https://eonet.gsfc.nasa.gov/api/v3/events?start={start_date}&end={end_date}"
    response = requests.get(api_url)


    if response.status_code == 200:
        data = response.json()
        events = data.get("events", [])


        if not events:
            print("No date。")
            return


        for event in events:
            print("Event name:", event.get("title"))
            coordinates = event.get("geometry", [{}])[0].get("coordinates")
            date = event.get("geometries", [{}])[0].get("date")
            print("Coordinates:", coordinates if coordinates else "Unknow")
            print("Date:", date if date else "Unknow")
            print("Category:", event.get("categories", [{}])[0].get("title"))
            print("----------------------------------")
    else:
        print("Unable to retrieve data, error code:", response.status_code)


def on_submit():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    get_nasa_events(start_date, end_date)

# Create the main window
root = Tk()
root.title("NASA Events Tracker")

# Create date entry box
Label(root, text="Start Date (YYYY-MM-DD):").pack()
start_date_entry = Entry(root)
start_date_entry.pack()

Label(root, text="End Date (YYYY-MM-DD):").pack()
end_date_entry = Entry(root)
end_date_entry.pack()

# Create a submit button
submit_button = Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
