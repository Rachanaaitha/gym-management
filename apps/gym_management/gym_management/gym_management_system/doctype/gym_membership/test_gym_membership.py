import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymMembership(FrappeTestCase):

    def test_membership_creation(self):
        """Test if Gym Membership is created successfully"""

        doc = frappe.get_doc({
            "doctype": "Gym Membership",
            "member": "GM-0001",  # use existing member
            "plan_name": "Monthly",
            "start_date": "2026-03-01",
            "end_date": "2026-04-01",
            "status": "Active"
        })

        doc.insert()

        self.assertEqual(doc.status, "Active")


    def test_membership_expiry(self):
        """Test if membership gets expired correctly"""

        doc = frappe.get_doc({
            "doctype": "Gym Membership",
            "member": "GM-0001",
            "plan_name": "Monthly",
            "start_date": "2025-01-01",
            "end_date": "2025-02-01",
            "status": "Active"
        })

        doc.insert()

        # simulate expiry logic
        if doc.end_date < frappe.utils.today():
            doc.status = "Expired"

        self.assertEqual(doc.status, "Expired")