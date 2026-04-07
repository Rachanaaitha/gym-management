frappe.ui.form.on('Gym Member', {
    refresh: function(frm) {
        // Only call API if the form has a member name
        if (frm.doc.name) {
            // API call for membership info
            frappe.call({
                method: "gym_management.api.get_membership_info",
                args: {
                    member: frm.doc.name
                },
                callback: function(r) {
                    if (r.message) {
                        let msg = `
                            <b>Status:</b> ${r.message.status}<br>
                            <b>Days Left:</b> ${r.message.days_left}
                        `;

                        // If membership is expiring soon, show a red warning
                        if (r.message.days_left <= 5) {
                            msg += "<br><span style='color:red;'>Expiring Soon!</span>";
                        }

                        frappe.msgprint(msg);  // Display the membership status
                    }
                }
            });

            // Adding custom button "View Summary"
            frm.add_custom_button('View Summary 📊', function() {

                // Fetch the member's summary data
                frappe.call({
                    method: "gym_management.api.get_member_summary",
                    args: {
                        member: frm.doc.name
                    },
                    callback: function(r) {
                        if (!r.message) {
                            frappe.msgprint("No summary data found for this member.");
                            return;
                        }

                        // Create the dialog box to show the summary
                        let d = new frappe.ui.Dialog({
                            title: 'Member Summary',
                            fields: [
                                {
                                    fieldtype: 'HTML',
                                    fieldname: 'summary'
                                }
                            ]
                        });

                        // Inject the HTML into the dialog
                        d.fields_dict.summary.$wrapper.html(`
                            <div style="padding:10px;">
                                <h4>👤 ${frm.doc.full_name || frm.doc.first_name}</h4>
                                <p><b>Membership:</b> ${r.message.membership}</p>
                                <p><b>Last Booking:</b> ${r.message.last_booking}</p>
                            </div>
                        `);

                        // Show the dialog
                        d.show();
                    }
                });

            });
        }
    }
});