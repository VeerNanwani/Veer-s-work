"""
RECORD CHECK  -  my version
===========================

Name  : Veer Sanjay Nanwani
Lane  :  AI 
Date  : 21/10/2026
"""

class Record:
    over_limit_count=0
    def __init__(self,label,value,limit):
        """Initialize a record with its label, value, and limit."""
        self.label=label
        self.value=value
        self.limit=limit
        if value >= limit:
            Record.over_limit_count += 1

    def percent(self):
        """Return the value as a percentage of its limit."""
        percent = (self.value / self.limit) * 100
        return percent

    def status(self):
        """Return the status based on the percentage of the limit."""
        percent=self.percent()
        if percent >= 100:
            return"OVER LIMIT"
        elif percent>=90:
            return"WARNING"
        else:
            return"OK"

    def is_over(self):
        """Return whether the record meets or exceeds its limit."""
        return self.percent() >= 100

rec = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
] 

for records in rec:
        print("=" * 34)
        print(f"  RECORD CHECK  -  {records.label}")
        print(f" Value:  {records.value}")
        print(f" Limit:  {records.limit}")
        print(f" Status: {records.status()}")
        print("=" * 34)

with open("Data.txt","w") as f:
    f.write("SRV-001,12.0,100.0\n")
    f.write("SRV-02,90.0,100.0\n")
    f.write("SRV-03,190.0,100.0\n")
path="Data.txt"
def load_records(path):
    """Load records from comma-separated label, value, and limit lines."""
    records=[]
    with open(path,"r") as file:
        for line in file:
            label,value,limit=line.strip().split(",")
            records.append(Record(label,float(value),float(limit)))
    return records

loaded_record=load_records("Data.txt")

for record in loaded_record:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print(f" Value:  {record.value}")
    print(f" Limit:  {record.limit}")
    print(f" Status: {record.status()}")
    print("=" * 34)
over_limit_count = sum(record.is_over() for record in loaded_record)
print(f"{over_limit_count} out of {len(loaded_record)} were over limit")
print("=" * 34)