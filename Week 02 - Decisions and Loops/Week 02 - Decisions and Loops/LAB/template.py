"""
RECORD CHECK  -  my version
===========================

Name  : Ritesh Shrivastava
Lane  :  IT
Date  : 22/10/26

Run it:   python template.py
"""

over_limit_count = 0

while True:
    label = input("Enter label (or quit): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))

    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"{'Label':<12}: {label}")
    print(f"{'Value':<12}: {value:>8.2f}")
    print(f"{'Limit':<12}: {limit:>8.2f}")
    print(f"{'Difference':<12}: {difference:>8.2f}")
    print(f"{'Percentage':<12}: {percent:>7.2f}%")
    print(f"{'Status':<12}: {status}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"{over_limit_count} records were over limit.")