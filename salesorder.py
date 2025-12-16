from odoo import models
from odoo.expecttions import ValidationError

class SaleOrder(models.Model):
    _inherit ="sales.order"
    def action_confirm(self):
        for order in self:
            if orcder.amount_total <=500000:
                raise ValidationError("Minimal order adalah 500.000")
            return super().action_confirm()