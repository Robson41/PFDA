# assignment02-bankholidays.py
"""
Program: Northern Ireland Bank Holidays
Description:
    This program prints out all Northern Ireland bank holidays for 2026.
    It also highlights holidays that are unique to Northern Ireland and
    not observed elsewhere in the UK.
"""

# -----------------------------
# Step 1: Define UK-wide bank holidays
# -----------------------------
# Each holiday is stored as a key-value pair:
#   key = holiday name
#   value = date in YYYY-MM-DD format
uk_holidays = {
    "New Year's Day": "2026-01-01",
    "Good Friday": "2026-03-29",
    "Easter Monday": "2026-04-01",
    "Early May Bank Holiday": "2026-05-04",
    "Spring Bank Holiday": "2026-05-25",
    "Summer Bank Holiday (England, Wales, NI)": "2026-08-31",
    "Christmas Day": "2026-12-25",
    "Boxing Day": "2026-12-26",
}

# -----------------------------
# Step 2: Define Northern Ireland unique holidays
# -----------------------------
# These holidays are observed in Northern Ireland but not elsewhere in the UK
ni_unique_holidays = {
    "St. Patrick's Day": "2026-03-17",
    "Battle of the Boyne (Orangemen's Day)": "2026-07-12"
}

# -----------------------------
# Step 3: Combine UK holidays and NI unique holidays
# -----------------------------
# Copy UK holidays to a new dictionary for Northern Ireland
ni_holidays = uk_holidays.copy()
# Add the unique Northern Ireland holidays
ni_holidays.update(ni_unique_holidays)

# -----------------------------
# Step 4: Print Northern Ireland bank holidays
# -----------------------------
print("=== Northern Ireland Bank Holidays 2026 ===")
# Loop through each holiday in the combined dictionary
for name, date in ni_holidays.items():
    # Check if the holiday is unique to Northern Ireland
    if name in ni_unique_holidays:
        # Print the date, name, and mark as unique
        print(f"{date}: {name} (Unique to NI)")
    else:
        # Print standard UK holiday
        print(f"{date}: {name}")
