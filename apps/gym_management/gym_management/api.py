import frappe
from frappe.utils import today, date_diff

@frappe.whitelist()
def get_membership_info(member):
    membership = frappe.get_all(
        "Gym Membership",
        filters={"member": member, "status": "Active"},
        fields=["end_date"],
        order_by="end_date desc",
        limit=1
    )

    if not membership:
        return {"status": "No Active Membership", "days_left": 0}

    end_date = membership[0].end_date
    days_left = date_diff(end_date, today())

    return {
        "status": "Active",
        "days_left": days_left
    }


import frappe
from frappe.utils import today

@frappe.whitelist()
def get_dashboard_data():
    return {
        "members": frappe.db.count("Gym Member"),
        "active": frappe.db.count("Gym Membership", {"status": "Active"}),
        "today": frappe.db.count("Gym Class Booking", {"class_date": today()})
    }

@frappe.whitelist()
def get_member_summary(member):
    # Fetch active membership plan for the member
    membership = frappe.db.get_value(
        "Gym Membership",
        {"member": member, "status": "Active"},
        "plan_name"
    )

    # Fetch the latest class booking for the member
    booking = frappe.db.get_value(
        "Gym Class Booking",
        {"member": member},
        "class_date",
        order_by="creation desc"
    )

    # Return the data
    return {
        "membership": membership or "No Active Membership",
        "last_booking": booking or "No Booking"
    }
import frappe
import requests

@frappe.whitelist()
def get_ai_fitness_advice(member):

    logs = frappe.get_all(
        "Gym Fitness Log",
        filters={"member": member},
        fields=["weight", "calories", "workout_type"],
        order_by="creation desc",
        limit=3
    )

    if not logs:
        return "No fitness data available"

    # 🔥 CLEAN PROMPT (IMPORTANT)
    prompt = f"""
    You are a professional gym coach.

    Based on this member data:
    {logs}

    Give response in this format:

    Workout Suggestion:
    - (clear simple sentence)

    Diet Recommendation:
    - (clear simple sentence)

    Improvement Tip:
    - (clear simple sentence)

    Keep it simple, clean, and easy to understand.
    Do NOT combine into one line.
    """ 

    url = "https://api.anthropic.com/v1/messages"

    headers = {
        import os

	"x-api-key": os.getenv("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }

    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 100,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        result = response.json()

        if "content" in result:
            return result["content"][0]["text"]
        else:
            return "❌ AI Error. Check API key or request."

    except Exception:
        return "❌ Something went wrong with AI response."
