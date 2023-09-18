months = {
    0: "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec" : "December"
}

print(months.get("0", "There is nothing in here, Dude! Search in a proper place."))


a=10
def add():
    global a
    a=12

print(a)