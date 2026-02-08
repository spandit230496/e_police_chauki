import frappe


@frappe.whitelist(allow_guest=True)
def verify_case(case):

    if not frappe.db.exists("Case File", case):
        frappe.throw("Invalid Case Number")

    doc = frappe.get_doc("Case File", case)

    html = f"""
    <h2>Case Verification</h2>
    <p><b>Case ID:</b> {doc.name}</p>
    <p><b>Status:</b> {doc.current_status}</p>
    <p><b>Created On:</b> {doc.creation}</p>
    """

    return frappe.respond_as_web_page(
        title="Case Verification",
        html=html
    )
