"""
RECORD CHECK  -  my version
===========================

Name  : Veer Sanjay Nanwani
Lane  :  AI 
Date  : 14/10/2026
"""

def status_of(percent):
    """Return the status for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check_record(value, limit):
    """Return the difference, percent and status for one value and limit."""
    difference = limit - value
    percent = value / limit * 100
    return difference, percent, status_of(percent)


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Value      : {value:>21.2f}")
    print(f"Limit      : {limit:>21.2f}")
    print(f"Difference : {difference:>21.2f}")
    print(f"Percent    : {percent:>20.2f}%")
    print(f"Status     : {status:>21}")
    print("=" * 34)



def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            records.append({
                "label": label.strip(),
                "value": float(value),
                "limit": float(limit),
            })
    return records


def save_results(lines, path):
    """Write one label,status line per record to a file."""
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


with open("Records.txt", "w", encoding="utf-8") as f:
    f.write("R-001,87.0,100\n")
    f.write("R-002,120.0,100\n")
    f.write("R-003,45.0,100\n")
    f.write("R-004,95.0,100\n")
try:
    records = load_records("Records.txt")
except FileNotFoundError:
    print("Could not find 'Records.txt'. Check the name and folder.")
    records = []

result_lines = []
over_count = 0

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    result_lines.append(f"{record['label']},{status}")
    if status == "OVER LIMIT":
        over_count += 1

save_results(result_lines, "results.txt")
print(f"{over_count} record(s) OVER LIMIT")