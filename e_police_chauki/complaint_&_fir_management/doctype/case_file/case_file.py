# Copyright (c) 2026, Sandip Pandit and contributors
# For license information, please see license.txt

import frappe
import qrcode
import os

from frappe.model.document import Document


class CaseFile(Document):

    def after_insert(self):
        self.generate_qr_code()

    def generate_qr_code(self):

        # Data you want inside QR
        # Example: API URL / Case ID
        qr_data = f"{frappe.utils.get_url()}/api/method/e_police_chauki.api.verify_case?case={self.name}"


        # Create QR
        qr = qrcode.make(qr_data)

        # File name
        file_name = f"case_qr_{self.name}.png"

        # Path to save
        file_path = os.path.join(
            frappe.get_site_path("private", "files"),
            file_name
        )

        # Save image
        qr.save(file_path)

        # Save as Frappe File
        file_doc = frappe.get_doc({
            "doctype": "File",
            "file_name": file_name,
            "file_url": "/private/files/" + file_name,
            "attached_to_doctype": self.doctype,
            "attached_to_name": str(self.name),
            "is_private": 1
        })

        file_doc.insert(ignore_permissions=True)

        # Link to field (if you created qr_code field)
        self.db_set("qr_code", file_doc.file_url)

        frappe.db.commit()

