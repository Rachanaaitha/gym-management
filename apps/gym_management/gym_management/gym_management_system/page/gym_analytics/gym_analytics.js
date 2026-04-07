frappe.pages['gym-analytics'].on_page_load = function(wrapper) {

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: '🏋️ Gym Analytics Dashboard',
        single_column: true
    });

    // Create container
    let content = $(`
        <div style="padding: 20px;">
            <h2>📊 Gym Insights</h2>

            <div id="stats" style="display:flex; gap:20px; margin-top:20px;">
                <div class="card">Members: <b id="members">0</b></div>
                <div class="card">Active: <b id="active">0</b></div>
                <div class="card">Today: <b id="today">0</b></div>
            </div>

            <button class="btn btn-primary" id="refresh" style="margin-top:20px;">
                🔄 Refresh Data
            </button>
        </div>
    `);

    $(wrapper).find('.layout-main-section').append(content);

    // Load data
    function load_data() {
        frappe.call({
            method: "gym_management.api.get_dashboard_data",
            callback: function(r) {
                if (r.message) {
                    $('#members').text(r.message.members);
                    $('#active').text(r.message.active);
                    $('#today').text(r.message.today);
                }
            }
        });
    }

    // Button click
    $('#refresh').click(function() {
        load_data();
        frappe.msgprint("Data refreshed!");
    });

    // Initial load
    load_data();
};