import frappe


@frappe.whitelist(allow_guest=True)
def verify_case(case):

    # Validate case
    if not frappe.db.exists("Case File", case):
        return frappe.respond_as_web_page(
            title="Invalid Case",
            html="""
            <div style="font-family:Arial;text-align:center;margin-top:50px">
                <h2 style="color:red;">❌ Invalid Case Number</h2>
                <p>Please check the QR code.</p>
            </div>
            """
        )

    doc = frappe.get_doc("Case File", case)

    # Safe values
    def val(v):
        return v if v else "-"

    html = f"""
    <div style="
        font-family:Arial;
        max-width:650px;
        margin:40px auto;
        padding:25px;
        border-radius:10px;
        box-shadow:0 0 10px rgba(0,0,0,0.1);
        background:#fff;
    ">

        <h2 style="text-align:center;color:#2c3e50;">
            ✅ Case Verification
        </h2>

        <hr>

        <table width="100%" cellpadding="6">

            <tr>
                <td><b>Case ID</b></td>
                <td>{val(doc.name)}</td>
            </tr>

            <tr>
                <td><b>FIR</b></td>
                <td>{val(doc.fir)}</td>
            </tr>

            <tr>
                <td><b>Case Type</b></td>
                <td>{val(doc.case_type)}</td>
            </tr>

            <tr>
                <td><b>Criminal Name</b></td>
                <td>{val(doc.criminial_name)}</td>
            </tr>

            <tr>
                <td><b>Court Name</b></td>
                <td>{val(doc.court_name)}</td>
            </tr>

            <tr>
                <td><b>Start Date</b></td>
                <td>{val(doc.start_date)}</td>
            </tr>

            <tr>
                <td><b>Current Status</b></td>
                <td>{val(doc.current_status)}</td>
            </tr>

            <tr>
                <td><b>Next Hearing</b></td>
                <td>{val(doc.next_hearing_date)}</td>
            </tr>

            <tr>
                <td><b>Final Verdict</b></td>
                <td>{val(doc.final_verdict)}</td>
            </tr>

            <tr>
                <td><b>Remarks</b></td>
                <td>{val(doc.remarks)}</td>
            </tr>

            <tr>
                <td><b>Created On</b></td>
                <td>{doc.creation.strftime('%d-%m-%Y %H:%M')}</td>
            </tr>

        </table>

        <hr>

        <p style="text-align:center;color:green;font-size:14px;">
            ✔ Verified from E-Police Chauki System
        </p>

    </div>
    """

    return frappe.respond_as_web_page(
        title="Case Verification",
        html=html
    )
