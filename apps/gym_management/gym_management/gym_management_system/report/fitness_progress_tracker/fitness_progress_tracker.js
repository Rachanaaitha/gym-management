frappe.query_reports["Fitness Progress Tracker"] = {
    filters: [
        {
            fieldname: "member",
            label: "Member",
            fieldtype: "Link",
            options: "Gym Member"
        }
    ]
};