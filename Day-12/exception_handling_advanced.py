# ========================================
#   Python Exception Handling (Complete)
# ========================================

# ---------------------------
# finally → always runs
# ---------------------------
try:
    l = input("Enter a number: ")
    x = l / 12
except TypeError as e:
    print("TypeError:", e)
finally:
    print("I will always execute")


# ---------------------------
# Difference: finally vs after-except
# ---------------------------
try:
    l = input("Enter a number: ")
    x = l / 12
except TypeError as e:
    print("TypeError:", e)

print("This will execute if no fatal error occurs before")


# ---------------------------
# finally with return
# ---------------------------
def fun():
    try:
        l = int(input("Enter a number: "))
        x = l / 12
        return 1
    except TypeError as e:
        print("TypeError:", e)
        return 0
    finally:
        print("finally → I am executed")  # ✅ always runs
    print("Never reached")


print(fun())

# finally is mainly used for:
#   - closing database connections
#   - cleaning file handles
#   - releasing network resources


# ---------------------------
# try-except-else-finally
# ---------------------------
try:
    5 / 5  # no error
except TypeError as e:
    print("TypeError:", e)
else:
    print("I am in else (only if no error)")
finally:
    print("I am in finally (always)")


# ---------------------------
# try-finally (without except)
# ---------------------------
try:
    # "dharmil" / 7   # error
    pass
finally:
    print("Always runs (even without except)")


# ---------------------------
# Nested try-except-finally (with typed exceptions)
# ---------------------------

print("\n\n")
try:
    print("Outer try block")
    # 1/"Hi"
    try:
        print("Inner try block")
        # 2/"Hi"
    except ZeroDivisionError:
        print("Inner except (ZeroDivisionError)")
        # 3/"Hi"
    finally:
        print("Inner finally")
        # 4/"Hi"
    print("After inner try-except-finally block")
    # 5/"Hi"
except ValueError:
    print("Outer except (ValueError)")
    # 6/"Hi"
finally:
    print("Outer finally")
    # 7/"Hi"

print("After outer try-except-finally block")
# 8/"Hi"


# ========================================
#   CASE ANALYSIS (Most Important for Understanding the Flow of try-except-finally)
# ========================================


"""
Case 0 → No error
    Normal flow → both finally blocks run → no except executed.

Case 1 → Error at (1/"Hi") [outer try before inner]
    Inner skipped.
    If type matches outer except → handled.
    If not → outer finally runs, program stops.

Case 2 → Error at (2/"Hi") [inner try]
    - If matches inner except → handled → inner finally → continue outer.
    - If not → inner except skipped → inner finally runs → goes to outer except.
    - If outer also mismatched → outer finally runs, program stops.

Case 3 → Error at (2/"Hi") AND (3/"Hi") [inner try + inner except]
    Inner try fails → inner except also fails → inner finally runs → error bubbles outward.
    Outer except handles only if type matches.

Case 4 → Error at (4/"Hi") [inside inner finally]
    Inner finally fails → error goes to outer except.
    If type mismatch → outer finally runs, program stops.

Case 5 → Error at (5/"Hi") [after inner block inside outer try]
    Inner completes → error in outer try.
    Outer except handles if type matches, else unhandled.

Case 6 → Error at (6/"Hi") [inside outer except]
    Outer except fails → outer finally still runs → program stops.

Case 7 → Error at (7/"Hi") [inside outer finally]
    Outer finally fails → program stops immediately.

Case 8 → Error at (8/"Hi") [after everything]
    All try/except/finally done → error happens in normal code → uncaught unless wrapped.

Case 9 → Inner except mismatch, outer except handles
    Error in inner try.
    Inner except type not matching → skipped.
    Inner finally runs.
    Outer except type matches → handled.
    Outer finally runs.

Case 10 → Inner except mismatch, outer except mismatch
    Error in inner try.
    Inner except skipped.
    Inner finally runs.
    Outer except skipped.
    Outer finally runs.
    Program stops (uncaught).

Case 11 → Both excepts present with different types
    - Error in inner try matches inner except → handled.
    - If another error later in outer try matches outer except → handled separately.
    - Both finally blocks run.

Case 12 → Nested mix (error chain through all)
    Error in inner try (mismatch) → inner except skipped → inner finally runs.
    Error then bubbles to outer except (mismatch too) → outer skipped.
    Outer finally runs.
    Program stops (uncaught).
"""


# ========================================
# Special Case:
# Inner Try Error + Inner Except Mismatch + Inner Finally Error
# ========================================

"""
Step-by-step flow:
1. Inner try raises an error (TypeError).
2. Inner except does not match (set to ZeroDivisionError) → skipped.
3. Inner finally executes anyway and raises a new error (ValueError).
4. Python discards the original inner try error and propagates only the finally error.
5. Outer except handles the ValueError (if matching).
6. Outer finally always runs.

⚡ Key Insight:
    - If finally raises a new error, the original try error is LOST.
    - Only the latest error from finally survives.
"""

print("\n\n")

try:
    print("Outer try block")
    try:
        print("Inner try block")
        1 / "hi"     # ❌ TypeError (inner try error)
    except ZeroDivisionError:
        # Mismatch → skipped
        print("Inner except (ZeroDivisionError)")
    finally:
        print("Inner finally")
        int("hello")   # ❌ ValueError (inner finally error)
    print("After inner block")   # never reached
except (TypeError, ValueError) as e:
    print("Outer except handled:", e)
finally:
    print("Outer finally")

"""
Expected Output:
----------------
Outer try block
Inner try block
Inner finally
Outer except handled: invalid literal for int() with base 10: 'hello'
Outer finally
"""

print("\n\n")

try:
    print("Outer try block")
    try:
        print("Inner try block")
        1 / "hi"     # ❌ TypeError (inner try error)
    except ZeroDivisionError:
        # Mismatch → skipped
        print("Inner except (ZeroDivisionError)")
    finally:
        print("Inner finally")
        int("hello")   # ❌ ValueError (inner finally error)
    print("After inner block")   # never reached
except ValueError as e:   # <-- only ValueError handled
    print("Outer except handled:", e)
finally:
    print("Outer finally")

# NOTE: If there are 2 errors in one block, the new one is considered.
#       The old one is LOST, as shown in the above 2 cases.
