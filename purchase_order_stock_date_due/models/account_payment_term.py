# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from functools import reduce
from dateutil.relativedelta import relativedelta

from odoo import fields, models
from odoo.tools.float_utils import float_is_zero


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    def _compute_for_purchase(self, value, date_ref=False, currency=None):
        # Compute code inspired on account_payment_term_extension
        #  compute() method
        # TODO remove amount references, seems to be unnecessary
        self.ensure_one()
        date_ref = date_ref or fields.Date.today()
        amount = value
        result = []
        if not currency:
            if self.env.context.get("currency_id"):
                currency = self.env["res.currency"].browse(
                    self.env.context["currency_id"]
                )
            else:
                currency = self.env.user.company_id.currency_id
        precision_digits = currency.decimal_places

        next_date = date_ref
        for line in self.line_ids:
            amt = line.compute_line_amount(value, amount, precision_digits)
            if not self.sequential_lines:
                next_date = date_ref
                if float_is_zero(amt, precision_digits=precision_digits):
                    continue
            if line.option == "day_after_invoice_date":
                next_date += relativedelta(
                    days=line.days, weeks=line.weeks, months=line.months
                )
            elif line.option == "day_following_month":
                # Getting last day of next month
                next_date += relativedelta(day=line.days, months=1)
            elif line.option == "day_current_month":
                # Getting last day of next month
                next_date += relativedelta(day=line.days, months=0)
            # From Odoo
            elif line.option == "after_invoice_month":
                # Getting 1st of next month
                next_first_date = next_date + relativedelta(day=1, months=1)
                # Then add days
                next_date = next_first_date + relativedelta(
                    days=line.days - 1, weeks=line.weeks, months=line.months
                )
            next_date = self.apply_payment_days(line, next_date)
            next_date = self.apply_holidays(next_date)
            if not float_is_zero(amt, precision_digits=precision_digits):
                result.append((next_date, amt))
                amount -= amt
        amount = reduce(lambda x, y: x + y[1], result, 0.0)
        dist = round(value - amount, precision_digits)
        if dist:
            last_date = result and result[-1][0] or fields.Date.today()
            result.append((last_date, dist))
        return result and result[-1][0]
