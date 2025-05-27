import math
import calendar
from datetime import datetime, date, time, timedelta

def math_examples():
    print("=== Math Module Examples ===")
    print("Value of pi:", math.pi)
    print("Value of e:", math.e)
    print("Square root of 16:", math.sqrt(16))
    print("Factorial of 5:", math.factorial(5))
    print("2 raised to the power 3:", math.pow(2, 3))
    print("Natural logarithm of 10:", math.log(10))
    print("Logarithm of 1000 with base 10:", math.log(1000, 10))

    angle_deg = 45
    angle_rad = math.radians(angle_deg)
    print(f"Sine of {angle_deg} degrees:", math.sin(angle_rad))
    print(f"Cosine of {angle_deg} degrees:", math.cos(angle_rad))
    print(f"Tangent of {angle_deg} degrees:", math.tan(angle_rad))
    print()

def datetime_examples():
    print("=== DateTime Module Examples ===")
    now = datetime.now()
    print("Current date and time:", now)

    specific_date = date(2025, 3, 28)
    print("Specific date:", specific_date)

    specific_time = time(5, 39, 45)
    print("Specific time:", specific_time)

    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted current date and time:", formatted_date)

    # Parsing a date string
    date_string = "2025-27-03 05:56:30"
    parsed_date = datetime.strptime(date_string, "%Y-%d-%m %H:%M:%S")
    print("Parsed date and time:", parsed_date)

    # Date arithmetic
    future_date = now + timedelta(days=7)
    print("Date after 7 days:", future_date)

    past_time = now - timedelta(minutes=30)
    print("Time 30 minutes ago:", past_time)
    print()

def calendar_examples():
    print("=== Calendar Module Examples ===")
    year = 2025
    month = 3
    cal = calendar.TextCalendar()
    print(f"Calendar for {month}/{year}:")
    print(cal.formatmonth(year, month))

    leap_year = 2024
    is_leap = calendar.isleap(leap_year)
    print(f"Is {leap_year} a leap year? {is_leap}")
    print()

if __name__ == "__main__":
    math_examples()
    datetime_examples()
    calendar_examples()
