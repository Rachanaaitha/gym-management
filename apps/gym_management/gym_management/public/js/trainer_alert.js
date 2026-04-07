// frappe.provide("gym_management.notifications");
// console.log("🔥 Trainer Alert JS LOADED");
// // Register the real-time listener once per session
// if (!gym_management.notifications.trainer_listener_registered) {

//     frappe.realtime.on("new_trainer_subscription", function (data) {
//         // Show a persistent toast notification to the trainer
//         console.log("🔥 RECEIVED new_trainer_subscription EVENT:", data);
//         frappe.show_alert(
//             {
//                 message: `
//                     <strong>New subscription!</strong><br>
//                     <b>Member:</b> ${data.member}<br>
//                     <b>Plan:</b> ${data.plan}<br>
//                     <b>Date:</b> ${data.start_date}<br>
//                 `,
//                 indicator: "green",
//             },
//             10   // stays visible for 10 seconds
//         );

//         // Also push a system notification (bell icon in top bar)
//         frappe.utils.notify(
//            `New member ${data.member} subscribed to your plan`,
//             "success"
//         );
//     });
    

//     gym_management.notifications.trainer_listener_registered = true;
// }


frappe.provide("gym_management.notifications");
console.log("🔥 Trainer Alert JS LOADED");

// ✅ Wait for frappe to be fully ready before registering
$(document).ready(function () {
    
    // ✅ Debug: check socket connection status
    setTimeout(function () {
        console.log("Socket connected:", frappe.realtime.socket && frappe.realtime.socket.connected);
        console.log("Socket ID:", frappe.realtime.socket && frappe.realtime.socket.id);
    }, 2000);

    if (!gym_management.notifications.trainer_listener_registered) {

        frappe.realtime.on("new_trainer_subscription", function (data) {
            console.log("🔥 RECEIVED new_trainer_subscription EVENT:", data);

            frappe.show_alert(
                {
                    message: `
                        <strong>🏋️ New Subscription!</strong><br>
                        <b>Member:</b> ${data.member}<br>
                        <b>Plan:</b> ${data.plan}<br>
                        <b>Date:</b> ${data.start_date}<br>
                        <b>Status:</b> ${data.status}<br>
                    `,
                    indicator: "green",
                },
                15
            );
        });

        gym_management.notifications.trainer_listener_registered = true;
        console.log("✅ Trainer realtime listener registered");
    }
});
