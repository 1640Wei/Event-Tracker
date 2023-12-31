Hello, I am Wei. 🌩
======

### Project Name:  Event Tracker

### Date:  Nov 3, 2023

### Description:
This project retrieves event data through the NASA Earth Observatory Natural Event Tracker (EONET) API. Users can input dates through a GUI and display events that fall within the specified date range.

### Technologies Used:
- **Python**: Primary programming language.
  
- **Tkinter**: Python library for building GUI (graphical user interfaces).

- **Requests Library**: Used for making HTTP requests to retrieve data from the EONET API.

- **Socket Library**: Employed to configure DNS servers within the `set_dns` function.

- **JSON Library**: Utilized for parsing JSON-formatted data obtained from the API.


### Project Structure:：
- `gui.py`：Main code for the GUI interface.
- `event_tracker.py`：Main code for handling event tracking functionality


### Example:

- Enter the start date and end date, then click the Submit button. If there are events within the specified range, they will be displayed in the scrolling text box below.

<img width="300" height="400" src="https://github.com/1640Wei/Event-Tracker/blob/8d74c7a9a7d870569bc24d95cd7c55fd87b1ffe4/picture/1.png">   
<img width="300" height="400" src="https://github.com/1640Wei/Event-Tracker/blob/8d74c7a9a7d870569bc24d95cd7c55fd87b1ffe4/picture/2.png">

### Notice:

#### 1. DNS Configuration

DNS (Domain Name System) is a service that translates human-readable domain names into machine-understandable IP addresses. In this project, the accuracy of DNS configuration ensures that the program accurately resolves domain names to their corresponding IP addresses, facilitating successful sending and receiving of network requests. Incorrect DNS configuration could lead to failed domain name resolution, preventing the code from accessing external resources, such as an API. 

To ensure smooth communication, the project utilizes Google's public DNS server (8.8.8.8).

```python
dns_server = "8.8.8.8"
set_dns(dns_server)
```

#### 2. API Usage:
An API (Application Programming Interface) provides an interface that allows different software systems to communicate and exchange information. The purpose of this project is to utilize the NASA EONET API, which offers information about natural events on Earth, such as volcanic eruptions, hurricanes, and more.

**Steps for an API Request**:

1.Select the API URL.

```python
api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
```
2.Choose the HTTP method: Typically, the GET method is used to retrieve data.

3.Send the request: Use the HTTP request function in the code to send a request to the API.

4.Handle the response: Once a response is received from the API, use the code to process it, often by converting it into an easily manageable format like JSON.

5.Verify success: Check the API response's status code; a status code of 200 usually indicates success.

```python
try:
       response = requests.get(api_url)


       if response.status_code == 200:
           data = response.json()
           events = data.get("events", [])
```

### Update Log:
- Version 1.0.0 (Nov 3, 2023)

Initial release, featuring the basic GUI and event tracker functionality.


***
### Thanks:

🌩 I hope you enjoy this project! If you have any questions or suggestions, feel free to reach out at any time. 🌩

✉️ HTY140226@gmail.com
