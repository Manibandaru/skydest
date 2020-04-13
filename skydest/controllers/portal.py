
import math

from werkzeug import urls

from odoo import fields as odoo_fields, tools, _
from odoo.osv import expression
from odoo.exceptions import ValidationError
from odoo.http import Controller, request, route
from odoo.addons.portal.controllers.portal import CustomerPortal

# --------------------------------------------------
# Misc tools
# --------------------------------------------------

class CustomerPortalInherit(CustomerPortal):

    MANDATORY_BILLING_FIELDS = ["name", "phone", "email", "street", "city", "country_id","experience"]
    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "company_name","education","visa_status","availability","salary_exp","nationality","gender","emirate","dob","university","course","year_of_study","intern_role","other_job_role","description","whatsapp","availability_intern","previous_emp","certification","partner_phone","resume"]

