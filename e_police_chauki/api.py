import frappe

@frappe.whitelist(allow_guest=True)
def verify_case(case):

    doc = frappe.get_doc("Case File", case)

    return {
        "case_id": doc.name,
        "status": doc.current_status,
        "created_on": doc.creation
    }
