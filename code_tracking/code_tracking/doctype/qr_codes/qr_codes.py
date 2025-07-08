# Copyright (c) 2025, wanguimbutu@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class QrCodes(Document):
	pass


@frappe.whitelist()
def check_qr_exists(qr_code):
    return bool(frappe.db.exists("Qr Codes", {"qr_code": qr_code}))

@frappe.whitelist()
def validate_authenticator(qrcode):
    return bool(frappe.db.exists("Authenticator", {"qrcode": qrcode}))