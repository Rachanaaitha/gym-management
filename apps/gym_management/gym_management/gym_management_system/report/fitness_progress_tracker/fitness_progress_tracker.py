import frappe

def execute(filters=None):

    columns = [
        {"label": "Member ID", "fieldname": "member", "fieldtype": "Link", "options": "Gym Member"},
        {"label": "Member Name", "fieldname": "full_name", "fieldtype": "Data"},
        {"label": "Date", "fieldname": "date", "fieldtype": "Date"},
        {"label": "Weight", "fieldname": "weight", "fieldtype": "Float"},
        {"label": "Calories", "fieldname": "calories", "fieldtype": "Float"},
        {"label": "Workout", "fieldname": "workout_type", "fieldtype": "Data"},
        {"label": "Progress", "fieldname": "progress", "fieldtype": "Data"},
    ]

    conditions = ""
    if filters and filters.get("member"):
        conditions += f" AND gfl.member = '{filters.get('member')}'"

    logs = frappe.db.sql(f"""
        SELECT 
            gfl.member,
            gm.full_name,
            gfl.date,
            gfl.weight,
            gfl.calories,
            gfl.workout_type
        FROM `tabGym Fitness Log` gfl
        LEFT JOIN `tabGym Member` gm ON gfl.member = gm.name
        WHERE 1=1 {conditions}
        ORDER BY gfl.member, gfl.date ASC
    """, as_dict=True)

    data = []
    prev_weight = {}

    for row in logs:
        member = row["member"]
        progress = "N/A"

        if member in prev_weight:
            prev = prev_weight[member]

            if row["weight"] > prev:
                progress = "⬆️ Gained"
            elif row["weight"] < prev:
                progress = "⬇️ Lost"
            else:
                progress = "➖ Same"

        prev_weight[member] = row["weight"]
        row["progress"] = progress

        data.append(row)

    return columns, data