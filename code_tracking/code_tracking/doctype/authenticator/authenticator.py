# Copyright (c) 2025, wanguimbutu@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Authenticator(Document):
	pass

@frappe.whitelist()
def validate_authenticator(qrcode):
    return bool(frappe.db.exists("Authenticator", {"qrcode": qrcode}))