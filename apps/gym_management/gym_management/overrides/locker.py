import frappe

def validate_locker_booking(doc, method):
    if not doc.locker_number or not doc.from_date or not doc.to_date:
        return

    overlapping = frappe.db.sql("""
        SELECT name FROM `tabGym Locker Booking`
        WHERE locker_number = %s
        AND name != %s
        AND (
            (%s BETWEEN from_date AND to_date) OR
            (%s BETWEEN from_date AND to_date) OR
            (from_date BETWEEN %s AND %s)
        )
    """, (
        doc.locker_number,
        doc.name,
        doc.from_date,
        doc.to_date,
        doc.from_date,
        doc.to_date
    ))

    if overlapping:
        frappe.throw("Locker already booked for overlapping dates!")