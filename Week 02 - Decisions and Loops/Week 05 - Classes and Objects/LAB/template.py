
"""
MINI-PROJECT - IT LANE

Name : Ritesh Shrivastava
Lane : IT
Date : 24/10/26
"""


# 1. CLASS

class Record:
    def __init__(self, label, value, limit):
        """Store the record details."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status of the record."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# 2. CREATE RECORDS

records = [
    Record("srv-01", 87, 120),
    Record("srv-02", 95, 100),
    Record("srv-03", 120, 100)
]


# 3. PRINT REPORTS

over_limit_count = 0

for record in records:
    status = record.status()

    print()
    print("=" * 35)
    print("HOSTNAME:", record.label)
    print("GB USED:", record.value)
    print("GB TOTAL:", record.limit)
    print("STATUS:", status)
    print("=" * 35)

    if status == "OVER LIMIT":
        over_limit_count += 1


# 4. FINAL SUMMARY

print()
print(over_limit_count, "of", len(records), "records were OVER LIMIT")


# 5. CHECK THAT OBJECTS ARE INDEPENDENT

if len(records) >= 2:
    print()
    print("BEFORE CHANGE:")
    print(records[0].label, records[0].value)
    print(records[1].label, records[1].value)

    original_value = records[0].value
    records[0].value = 50

    print()
    print("AFTER CHANGE:")
    print(records[0].label, records[0].value)
    print(records[1].label, records[1].value)

    records[0].value = original_value
