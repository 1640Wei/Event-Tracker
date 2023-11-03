import tkinter as tk
import requests
import urllib.request
import io
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from PIL import Image, ImageTk
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
           result_text.insert(END, "No data.\n")
           return

       for event in events:
           result_text.insert(END, f"Event name: {event.get('title')}\n")
           coordinates = event.get("geometry", [{}])[0].get("coordinates")
           date = event.get("geometries", [{}])[0].get("date")
           result_text.insert(END, f"Coordinates: {coordinates if coordinates else 'Unknown'}\n")
           result_text.insert(END, f"Date: {date if date else 'Unknown'}\n")
           result_text.insert(END, f"Category: {event.get('categories', [{}])[0].get('title')}\n")
           result_text.insert(END, "----------------------------------\n")
   else:
       result_text.insert(END, f"Unable to retrieve data, error code: {response.status_code}\n")

def on_submit():
   start_date = start_date_entry.get()
   end_date = end_date_entry.get()
   get_nasa_events(start_date, end_date)

def resize_image(image, new_width, new_height):
   return image.resize((new_width, new_height), Image.LANCZOS)

# Initialize the main window of the GUI application.
root = tk.Tk()
root.title("NASA Events Tracker")
root.geometry("450x500")

# background image
image_url = "https://i.postimg.cc/Z5Pcyq4H/bg.png"
# Download the image and save it to a file
urllib.request.urlretrieve(image_url, "background_image.png")

# Open the image using PIL
background_image = Image.open("background_image.png")

# Resize the image to fill the entire window background.
window_width = 450
window_height = 500
resized_image = resize_image(background_image, window_width, window_height)

# Convert an Image object to a PhotoImage object.
icon_image = ImageTk.PhotoImage(resized_image)

# Create a Label element and set its background to an image.
background_label = ttk.Label(root, image=icon_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# font
title_style = ('Times', 20, 'bold')
font_style = ('.AppleSystemUIFont', 13)

label_title = tk.Label(root, text="NASA Events Tracker", font=title_style, foreground="#134b5f")
label_title.pack(pady=20)

# Create date entry box
Label(root, text="Start Date (YYYY-MM-DD):", font=font_style).pack(pady=13)
start_date_entry = Entry(root, width=20, font=('Arial', 12))
start_date_entry.pack()

Label(root, text="End Date (YYYY-MM-DD):", font=font_style).pack(pady=13)
end_date_entry = Entry(root, width=20, font=('Arial', 12))
end_date_entry.pack()

# Create a submit button
submit_button = Button(root, text="Submit", font=font_style, command=on_submit)
submit_button.pack(pady=13)

# Create a scrolled text box for displaying results
result_text = scrolledtext.ScrolledText(root, width=40, height=20, wrap=WORD)
result_text.pack(pady=20)

root.mainloop()
