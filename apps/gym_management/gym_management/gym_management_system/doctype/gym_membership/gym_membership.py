import frappe
from frappe.model.document import Document
from frappe.utils import today


class GymMembership(Document):
    pass


def expire_memberships():
    # Get all active memberships that are expired
    memberships = frappe.get_all(
        "Gym Membership",
        filters={
            "end_date": ("<=", today()),
            "status": "Active"
        },
        fields=["name", "member"]
    )

    print("Total memberships found:", len(memberships))

    for m in memberships:
        try:
            print("\nProcessing:", m.name)

            # Update status to Expired
            frappe.db.set_value(
                "Gym Membership",
                m.name,
                "status",
                "Expired"
            )

            # Check if member exists
            if not m.member:
                print(f"No member linked for {m.name}")
                continue

            print("Linked Member:", m.member)

            # Get member email
            member_email = frappe.db.get_value(
                "Gym Member",
                m.member,
                "email"
            )

            print("Fetched Email:", member_email)

            # Send email if email exists
            if member_email:
                frappe.sendmail(
                    recipients=[member_email],
                    subject="Gym Membership Expired",
                    message=f"""
                    <div style="font-family: Arial; font-size:14px;">
                        <p>Dear Member,</p>

                        <p>Your gym membership <b>{m.name}</b> has expired.</p>

                        <p>Please renew your membership to continue access.</p>

                        <p>Regards,<br><b>Gym Team</b></p>
                    </div>
                    """,
                    now=True
                )

                print(f"✅ Email sent to {member_email}")

            else:
                print(f"❌ No email for member {m.member}")

            # Log
            frappe.logger().info(f"Membership expired: {m.name}")

        except Exception as e:
            frappe.logger().error(f"Error processing {m.name}: {str(e)}")

    frappe.db.commit()