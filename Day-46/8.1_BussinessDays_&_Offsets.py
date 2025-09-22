"""
📌 Pandas – Step 8.1 (Business Days & Offsets)
    - Builds on Step 8 by adding Business-Day aware operations
    - Real-world data (finance, sales) often ignores weekends/holidays
    - Pandas provides tools to generate, shift, and offset dates with business-day logic

This file covers:
    - Generating business-day ranges (Mon–Fri only)
    - Shifting values by business days
    - Adding business-day offsets to dates (forecasting)

📝 Summary:
    - pd.bdate_range() → create range of weekdays (skips Sat & Sun)
    - shift(freq="B") → shift index forward/backward by business days
    - pd.offsets.BDay(n) → add business days to a timestamp or index
"""

import pandas as pd

# =====================================================
# ========= Business-Day Range (Skip Weekends) =========
# =====================================================

print("\n 👉🏻 Business-Day Range Example")
dates = pd.bdate_range(start="2025-09-01", periods=10)  # Only Mon–Fri
sales = [10, 15, 8, 20, 18, 22, 30, 25, 27, 35]

df = pd.DataFrame({"sales": sales}, index=dates)
print(df)

# =====================================================
# ===== Shift Sales by Business Day (freq='B') =========
# =====================================================

print("\n 👉🏻 Shifting by Business Day")
# Normally shift() just moves values down — but freq="B" shifts index by 1 business day
df["sales_prev_bday"] = df["sales"].shift(1, freq="B")
print(df)

# =====================================================
# ====== Adding Future Business Day Offsets ============
# =====================================================

print("\n 👉🏻 Adding 5 Business Days to Each Date (Forecast Dates)")
df["future_5b_days"] = df.index + pd.offsets.BDay(5)
print(df)

# =====================================================
# ================== Quick Recap ======================
# =====================================================

"""
📝 Quick Recap – Business-Day Handling

* pd.bdate_range(start, periods) → generate only business days (Mon–Fri)
* shift(freq="B") → shift index by business-day steps (ignores weekends)
* pd.offsets.BDay(n) → add n business days to timestamps (useful for forecasting)

Real World Uses:
    - Finance → Calculate returns on trading days only
    - Sales → Skip weekends when analyzing daily sales patterns
    - Forecasting → Project delivery dates ignoring weekends
"""
