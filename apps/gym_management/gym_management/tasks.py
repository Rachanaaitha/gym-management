import frappe
from frappe.utils import nowdate, getdate

def update_expired_memberships():
    today = getdate(nowdate())

    memberships = frappe.get_all(
        "Gym Membership",
        filters={
            "status": "Active",
            "end_date": ("<", today)
        },
        fields=["name"]
    )

    for m in memberships:
        doc = frappe.get_doc("Gym Membership", m.name)
        doc.status = "Expired"
        doc.save()

        frappe.logger().info(f"Expired: {doc.name}")
import frappe

def weekly_summary():
    members = frappe.get_all(
        "Gym Member",
        fields=["first_name", "last_name", "email"],
        filters={"email": ["!=", ""]}
    )

    for m in members:
        if m.email:
            full_name = f"{m.first_name or ''} {m.last_name or ''}".strip()

            frappe.sendmail(
                recipients=m.email,
                subject="Weekly Gym Summary",
                message=f"""
                Hello {full_name},

                Here is your weekly gym progress summary 💪

                Stay consistent and keep pushing!
                """
            )