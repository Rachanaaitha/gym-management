import frappe
from frappe.model.document import Document
from frappe.utils import today


class GymMembership(Document):
    pass


def expire_memberships():
    memberships = frappe.get_all(
        "Gym Membership",
        filters={
            "end_date": ("<=", today()),
            "status": "Active"
        },
        fields=["name", "member"]
    )

    for m in memberships:
        try:
            # Update status
            frappe.db.set_value(
                "Gym Membership",
                m.name,
                "status",
                "Expired"
            )

            # Get email
            member_email = frappe.db.get_value(
                "Gym Member",
                m.member,
                "email"
            )

            # Send email
            if member_email:
                frappe.sendmail(
                    recipients=[member_email],
                    subject="Gym Membership Expired",
                    message=f"""
                    <p>Your membership <b>{m.name}</b> has expired.</p>
                    <p>Please renew to continue.</p>
                    """,
                    now=True
                )

            # Log
            frappe.logger().info(f"Expired: {m.name}")

        except Exception as e:
            frappe.logger().error(f"Error: {str(e)}")

    frappe.db.commit()
