
"""
RECORD CHECK - my version

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 23/10/26
"""

# INPUT
label = input("Enter record name: ")
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))

# PROCESS
difference = value - limit
percent = (value / limit) * 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

# OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)
print(f"  Value       : {value:>10.2f}")
print(f"  Limit       : {limit:>10.2f}")
print(f"  Difference  : {difference:>10.2f}")
print(f"  Percent     : {percent:>9.2f}%")
print(f"  Status      : {status:>10}")
print("=" * 34)
