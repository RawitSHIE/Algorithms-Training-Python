"""
pair programming
countletter
rawit 60070081
"""
def main():
    """calender"""
    date = int(input())
    month = int(input())
    date_month = [6, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(day[((sum(date_month[:month]) + date)%7)])
main()
