frappe.ui.form.on("CaseFile", {

    refresh(frm) {

        if (frm.doc.qr_code) {

            let img_html = `
                <div style="text-align:center">
                    <img src="${frm.doc.qr_code}"
                         width="200"
                         style="border:1px solid #ccc;padding:8px">
                </div>
            `;

            frm.fields_dict.qr_code_preview.$wrapper.html(img_html);
        }
    }
});
