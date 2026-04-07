import frappe
from frappe.utils import nowdate, add_days

def weekly_class_summary():
    # Get last 7 days
    today = nowdate()
    last_week = add_days(today, -7)

    # Count total bookings
    total = frappe.db.count(
        "Gym Class Booking",
        {
            "class_date": ["between", [last_week, today]]
        }
    )

    frappe.log_error(
        f"Weekly Class Summary: {total} bookings",
        "Weekly Gym Report"
    )