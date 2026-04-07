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

        frappe.logger().info(f"Membership expired: {doc.name}")