import frappe
from frappe.utils import today, add_days

def execute():

    members = frappe.get_all("Gym Member", fields=["name"])

    for m in members:

        # Get last 30 days activity
        last_30_days = add_days(today(), -30)

        visits = frappe.db.count(
            "Gym Fitness Log",
            {
                "member": m.name,
                "date": [">=", last_30_days]
            }
        )

        # Decide category
        if visits >= 10:
            tag = "🔥 Regular"
        elif visits >= 3:
            tag = "🟢 Active"
        elif visits > 0:
            tag = "⚠️ Low Activity"
        else:
            tag = "🔴 Inactive"

        # Store in status field (or create new field if you want)
        frappe.db.set_value("Gym Member", m.name, "member_category", tag)

    frappe.db.commit()