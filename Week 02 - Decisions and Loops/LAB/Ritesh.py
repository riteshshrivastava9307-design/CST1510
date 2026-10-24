"""
RECORD CHECK - my version
=========================
Name  : Ritesh Shrivastava
Lane  : IT
Date  : 22/10/26
"""

label = input("Enter hostname (or quit to stop): ")

while label != "quit":
    value = float(input("Enter GB used: "))
    limit = float(input("Enter GB total: "))

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
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Used       : {value:>8.2f}")
    print(f"  Total      : {limit:>8.2f}")
    print(f"  Free       : {difference:>8.2f}")
    print(f"  Percent    : {percent:>7.2f} %")
    print(f"  Status     : {status:>8}")
    print("=" * 34)
    print()

    label = input("Enter hostname (or quit to stop): ")

print("Record checks finished.")