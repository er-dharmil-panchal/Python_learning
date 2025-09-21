"""
📌 Pandas – Step 8 (Time Series & Data-Handling)
    - Time series = observations recorded over time (sales logs, stock prices, IoT sensor readings, website traffic, etc.)
    - Dates are not simple strings — Pandas can sort, filter, aggregate by them
    - Provides tools like datetime objects, .dt accessor, resample, rolling, shift/lag, and timezone handling

This file covers:
    - Converting columns to datetime
    - Extracting date/time components
    - Setting datetime as index
    - Filtering by date
    - Resampling (daily, weekly, monthly)
    - Shifting & Lagging
    - Rolling windows (moving averages)
    - Time zone handling

📝 Summary:
    - pd.to_datetime() → convert string/date columns to datetime
    - DatetimeIndex → set dates as index for time-based selection
    - .dt accessor → extract year, month, day, hour, minute, second, weekday
    - Filtering → use boolean masks with datetime components
    - resample() → aggregate over time periods (D, W, M, Q, A)
    - shift() → lag/lead values for comparisons
    - rolling() → calculate moving averages or rolling statistics
    - tz_localize() / tz_convert() → handle timezone-aware datetime
"""

import pandas as pd

# =====================================================
# ========== Understanding Time-Series Data ===========
# =====================================================

# -> Time-series data = observations recorded over time, e.g., daily stock prices, sensor readings, sales logs.
print("\n 👉🏻 Example Data-set")
data = {
    "date": [
        "2025-09-01", "2025-09-02", "2025-09-03",
        "2025-09-04", "2025-09-05"
    ],
    "sales": [100, 120, 90, 150, 200]
}

df = pd.DataFrame(data)
print(df)

# =====================================================
# ================ Convert to Datetime ================
# =====================================================

"""
Not all datasets are "YYYY-MM-DD". Sometimes you get:
    - "09/01/2025" → MM/DD/YYYY
    - "01-09-2025" → DD-MM-YYYY
    - "2025/09/01 14:30" → with time
pd.to_datetime() can handle most formats automatically.
"""

# we store the data of date in just string , so now before performing any operation we have to convert date in datetime object
df["date"] = pd.to_datetime(df["date"])
print("\n 👉🏻 data types of the data is :\n", df.dtypes)
# Now Pandas recognizes the column as date.

"""
Basic notation:
    %Y → 4-digit year
    %y → 2-digit year
    %m → month
    %d → day
    %H:%M:%S → hour, minute, second
    %I -> Hour (12h)
    %H -> Hour (24h)
    %p -> AM/PM
"""
# 👉🏻 Explicit Format for Speed & Accuracy
# If the dataset is large, specifying the format is faster and safer:
# in our dataset -> 2025-09-05
print("\n 👉🏻 Explicit Format for Speed & Accuracy (\'%Y-%m-%d\')")
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
print(df)

# Exception :-
df3 = pd.DataFrame({"date": ["2025-09-01", "invalid", "2025-09-03"]})
pd.to_datetime(df3['date'], errors='coerce')

# NOTE :-   errors='coerce' → invalid strings become NaT (Not a Time)
#           errors='ignore' → keeps invalid values as-is


# 👉🏻 Including Time
print("\n👉🏻 Including Time")
df_time = pd.DataFrame({"datetime": ["2025-09-01 14:30:00", "2025-09-02 09:45:00"]})
df_time['datetime'] = pd.to_datetime(df_time['datetime'], format='%Y-%m-%d %H:%M:%S')
print(df_time)

# 👉🏻 Extracting the data
print("\n👉🏻 Extracting the data")
df_time['day'] = df_time['datetime'].dt.day
df_time['month'] = df_time['datetime'].dt.month
df_time['year'] = df_time['datetime'].dt.year
df_time['hour'] = df_time['datetime'].dt.hour
df_time['minute'] = df_time['datetime'].dt.minute
df_time['second'] = df_time['datetime'].dt.second
print(df_time)

# =====================================================
# ============== Set Datetime as Index ================
# =====================================================

print("\n 👉🏻Set date as index")
df.set_index('date', inplace=True)
print(df)
print(type(df.index))

print("\n 👉🏻Advantages of Having DatetimeIndex")
print("\nSelect single date - (2025-09-03)\n", df.loc['2025-09-03'])
print("\nRange selection - (2025-09-02':'2025-09-04)\n", df.loc['2025-09-02':'2025-09-04'])

# 👉🏻 Partial String Indexing
print("\n 👉🏻 Partial String Indexing")
print("\n All rows in 2025 \n", df.loc['2025'])
print("\n All rows in September 2025 \n", df.loc['2025-09'])
print("\n Single day \n", df.loc['2025-09-03'])

# =====================================================
# ============== Access Date Components ===============
# =====================================================

df_time.set_index('datetime', inplace=True)
print("\n👉🏻 Access Date Components")
print("Year - ", df_time.index.year)
print("Month - ", df_time.index.month)
print("Day - ", df_time.index.day)
print("Week-day - ", df_time.index.day_name())
print("Hour - ", df_time.index.hour)
print("Minute - ", df_time.index.minute)
print("Second - ", df_time.index.second)

# =====================================================
# ================ Filtering by Date ==================
# =====================================================
print("👉🏻 Filtering by date ")
# already saw, single date and range , now we will see conditions

# Never wrap a boolean mask inside a list/array when filtering rows.
print("\n 👉🏻Data After 3-sept-2025")
mask = ((df.index.day > 3) & (df.index.month == 9) & (df.index.year == 2025))
# print(mask)     # [False False False  True  True]

filtered = df.loc[mask]  # ✅ Always use .loc[] for row filtering
print(filtered)

# =====================================================
# =================== Resampling ======================
# =====================================================

"""
| Code      | Meaning     |
| --------- | ----------- |
| 'D'       | Day         |
| 'W'       | Week        |
| 'ME/MS'   | Month end   |
| 'Q'       | Quarter end |
| 'A'       | Year end    |
| 'H'       | Hour        |
| 'T'       | Minute      |

"""
print("\n 👉🏻 Resampling")

# Create a range of dates: Aug 25 → Sep 10 (17 days)
dates = pd.date_range(start="2025-08-25", end="2025-09-10", freq="d")
# Assign sales = 10, 20, 30... so sums are easy
sales = [(i + 1) * 10 for i in range(len(dates))]
df = pd.DataFrame({"date": dates, "sales": sales})
df.set_index("date", inplace=True)
print("\nSample data \n", df)

weekly = df.resample("W").sum()
monthly = df.resample("ME").sum()
print("\n👉🏻 Weekly sum of sales\n", weekly)
print("\n👉🏻 Can also customise the week end")
mon = df.resample('W-MON').sum()  # Weeks end on Monday
print("\nWeek end on Monday\n", mon)
print("\n👉🏻 Monthly sum of sales\n", monthly)

# 👉🏻 Sorting by Time
print("\n👉🏻 Sorting by Time")
df.sort_index(inplace=True)
print(df)

# 👉🏻 Resetting Index (if needed)
df.reset_index(inplace=True)

# =====================================================
# ================ Shifting & Lagging =================
# =====================================================

# Shifting means moving data forward or backward in time while keeping the same index.
"""
Visual Example:

| Date   | Sales | Sales (Shifted by 1)     |
| ------ | ----- | ------------------------ |
| Sep 01 | 100   | NaN                      |
| Sep 02 | 120   | 100  ← yesterday’s sales |
| Sep 03 | 90    | 120  ← yesterday’s sales |

So lagging = shift data down (so you can compare past vs present).
If you shift negative, it moves data up (future values).
"""

# Sample data
dates = pd.date_range("2025-09-01", periods=6, freq="D")
sales = [100, 120, 90, 150, 130, 160]
df = pd.DataFrame({"sales": sales}, index=dates)

print("\n 👉🏻 Original Data")
print(df)

# Shift by 1 day (lag)
df["sales_shifted_1"] = df["sales"].shift(1)

# Shift by 2 days (lag)
df["sales_shifted_2"] = df["sales"].shift(2)

# Shift backwards (lead/future values)
df["sales_shifted_-1"] = df["sales"].shift(-1)

print("\n👉🏻 After Shifting:")
print(df)

# 👉🏻Professional Use-Cases
print("\n👉🏻 Professional Use-Cases")
print("--> Day-over-Day Changes")
df["daily_change"] = df["sales"] - df["sales"].shift(1)
print("--> Growth Rate / Percentage Change")
df["pct_change"] = df["sales"].pct_change() * 100
# This is just a shortcut for (df["sales"] / df["sales"].shift(1)) - 1)
print(df)
df.drop('daily_change', axis=1, inplace=True)
df.drop('pct_change', axis=1, inplace=True)
df.drop('sales_shifted_-1', axis=1, inplace=True)
df.drop('sales_shifted_2', axis=1, inplace=True)

# =====================================================
# ========== Rolling Window (Moving Average) ==========
# =====================================================
# Smooth fluctuations over time:

print("\n👉🏻 Rolling Window")
# 👉🏻 shift + rolling
print("\n👉🏻 shift + rolling")

# 1. Calculate 3-day moving average (centered on current day)
print("--> 1.Calculate 3-day moving average (centered on current day)")
df["ma_3"] = df["sales"].rolling(window=3).mean()
# 2. Shift the moving average by 1 to compare "today vs previous avg"
print("--> 2. Shift the moving average by 1 to compare \"today vs previous avg\"")
df["prev_ma_3"] = df["ma_3"].shift(1)
df["prev_ma_3"] = df["sales"].rolling(3).mean().shift()

# 3. Compare today's sales with previous moving average
print("--> 3. Compare today's sales with previous moving average")
df["compare_to_prev_ma"] = df["sales"] - df["prev_ma_3"]

# short-cut
df["prev_ma_3"] = df["sales"].rolling(3).mean().shift()
print(df)

"""
Real World Uses
    - Stock trading: Compare today’s price vs previous 10-day moving average
    - Website analytics: Is today’s traffic above the last week’s average?
    - Sales monitoring: Detect sudden spikes/drops compared to historical trend
"""

# =====================================================
# ================== Sorting by Time ==================
# =====================================================

print("\n👉🏻 Sorting by Time")
# Even if the CSV is unsorted, you can fix it easily:
df.sort_index(inplace=True)
print(df)

# =====================================================
# ==================== Time Zones =====================
# =====================================================

# tz-naive dates
dates = pd.date_range("2025-09-01", periods=5, freq="D")
sales = [100, 120, 90, 150, 130]

df = pd.DataFrame({"sales": sales}, index=dates)
print("Naive datetime index:\n", df, "\n")

df.index = df.index.tz_localize("Asia/Kolkata")
print("After tz_localize (Asia/Kolkata (+5:30):\n", df, "\n")

df_utc = df.tz_convert("UTC")
print("Converted to UTC:\n", df_utc)

# =====================================================
# ================== QUICK RECAP ======================
# =====================================================

"""
📝 Quick Recap – Time Series & Data-Handling

* pd.to_datetime() → convert strings to datetime objects; use 'format' for speed/accuracy, 'errors="coerce"' for invalid dates
* DatetimeIndex → set with .set_index() for easy date-based selection
* Access components using .dt or index (year, month, day, hour, minute, second, weekday)
* Partial string indexing → select by year, month, or day
* Filtering → use boolean masks with datetime attributes (e.g., df.index.day > 3)
* resample(freq) → aggregate over time periods (D=day, W=week, ME=month-end, Q=quarter-end)
* shift(n) → lag/lead values for comparisons; pct_change() for growth rate
* rolling(window) → calculate moving averages or rolling statistics; can combine with shift
* tz_localize("Zone") → assign timezone to naive timestamps
* tz_convert("Zone") → convert tz-aware timestamps to another timezone
* Always sort by datetime before analysis to avoid errors in rolling/resampling
"""
