"""
RECORD CHECK  -  my version
===========================

Name  :  Veer Nanwani
Lane  :  AI 
Date  :  11/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line):
    """Returns messy raw lines into clean dict"""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
        
    return {"hostname": hostname, "rating": fields["rating"], "age": fields["age"]}

def status_of(rating, age, min_rating=1, max_rating=5, min_age=18, max_age=100):
    """Return OVER LIMIT if rating or age is out of range, otherwise OK."""
    if not (min_rating<=rating<=max_rating):
        return "FLAGGED"
    if not (min_age<=age<=max_age):
        return "FLAGGED"
    return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [] # replace with your code
with open("raw_messy.txt") as f:
    for line in f:
        if line.strip():
            raw_records.append(line)

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

flagged=0
for raw_record in raw_records:
    parsed_records = parse_line(raw_record)
    status_records = status_of(parsed_records["rating"], parsed_records["age"])
    print(parsed_records,status_records)
    if status_records=="FLAGGED":
        flagged=flagged+1
print(f"{len(raw_records)} records, from which {flagged} were flagged.")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
