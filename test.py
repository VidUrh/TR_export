from bs4 import BeautifulSoup

separator = ";"
input_file = "input.txt"
output_file = "output.csv"
end_of_line = "\n"

# Read the HTML string from input.txt
with open('input.txt', 'r', encoding="utf-8") as file:
    html_string = file.read()
    
with open('output.csv', 'w', encoding="utf-8") as file:
    file.write(separator.join(["Date", "Order Type", "Price", "Title", "Type of Transfer"]) + end_of_line)

# Parse the HTML string
soup = BeautifulSoup(html_string, 'html.parser')

# Find all elements with class "timeline_entry"
timeline_entries = soup.find_all(class_="timeline__entry")

# Store the timeline entries in a list
timeline_entries_list = list(timeline_entries)

# for each timeline entry in the list

for entry in timeline_entries_list:
    
    # Find the date
    if entry.find(class_="timelineMonthDivider") is not None:
        continue
    
    date = entry.find(class_="timelineEvent__subtitle").get_text().strip()
    try:
        date, orderType = date.split(" - ")
    except:
        date = date
        orderType = "Money added to account"
        
    price = entry.find(class_="timelineEvent__price").get_text().strip()
    title = entry.find(class_="timelineEvent__title").get_text().strip()
    
    if title != "Interest":
        continue
    
    
    if price.startswith("+"):
        price = price[1:]
        typeOfTransfer = "In"
    else:
        typeOfTransfer = "Out"
    with open('output.csv', 'a', encoding="utf-8") as file:
        file.write(separator.join([date, orderType, price, title, typeOfTransfer]) + end_of_line)