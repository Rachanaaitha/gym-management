import frappe
from frappe.model.document import Document

class GymTrainerSubscription(Document):

    def on_submit(self):
        # Debug (optional)
        frappe.msgprint("🔥 on_submit triggered")

        # Get trainer user (email)
        trainer_user = frappe.db.get_value(
            "Gym Trainer",
            self.trainer,
            "user"
        )

        frappe.msgprint(f"Trainer User: {trainer_user}")

        if not trainer_user:
            frappe.throw("Trainer user not set")

        # Get member details
        member_doc = frappe.get_doc("Gym Member", self.member)

        # Send realtime event with the correct fields
        frappe.publish_realtime(
            event="new_trainer_subscription",  # Match the event name in JS
            message={
                "member": member_doc.full_name,   # Make sure it matches the JS key 'member'
                "plan": self.plan_name,           # Ensure the plan name matches the JS key 'plan'
                "start_date": str(self.start_date),
                "status": self.status,

            },
            user=trainer_user  # Send event to the specific trainer
        )













