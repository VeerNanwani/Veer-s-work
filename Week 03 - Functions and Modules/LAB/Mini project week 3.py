"""
RECORD CHECK  -  my version
===========================

Name  : Veer Nanwani
Lane  :  AI 
Date  : 07/10/2026

Run it:   python template.py

"""
def status_of(percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculates the difference and percentage based on value and limit."""
    difference = limit - value
    percent = (value / limit) * 100 
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Prints the report based on the provided parameters."""
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Value      :      {value:>10.2f}")
    print(f"Limit      :      {limit:>10.2f}")
    print(f"Difference : {difference:>15.2f}")
    print(f"Percent    :    {percent:>10.2f}%")
    print(f"Status     :     {status:>10}")
    print("=" * 34)


over_limit_count=0
while True:
    label = input("Enter the label (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1
print()
print(f"Number of records OVER LIMIT: {over_limit_count}")

