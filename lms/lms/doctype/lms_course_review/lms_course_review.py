# Copyright (c) 2021, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import cint

class LMSCourseReview(Document):
	pass

@frappe.whitelist()
def submit_review(rating, review, course):
    out_of_ratings = frappe.db.get_all("DocField",
            {
                "parent": "LMS Course Review",
                "fieldtype": "Rating"
            },
            ["options"])
    out_of_ratings = (len(out_of_ratings) and out_of_ratings[0].options) or 5
    rating = cint(rating)/out_of_ratings
    frappe.get_doc({
        "doctype": "LMS Course Review",
        "rating": rating,
        "review": review,
        "course": course
    }).save(ignore_permissions=True)
    return "OK"
