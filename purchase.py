#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['PurchaseLine']
__metaclass__ = PoolMeta


class PurchaseLine:
    __name__ = 'purchase.line'

    purchase_date = fields.Function(fields.Date('Purchase Date'),
        'get_purchase_field', searcher='search_purchase_field')
    purchase_state = fields.Function(fields.Selection([
                ('draft', 'Draft'),
                ('quotation', 'Quotation'),
                ('confirmed', 'Confirmed'),
                ('processing', 'Processing'),
                ('done', 'Done'),
                ('cancel', 'Canceled'),
                ], 'State'),
        'get_purchase_field', searcher='search_purchase_field')

    def get_purchase_field(self, name):
        if name == 'purchase_state':
            name = 'state'
        return getattr(self.purchase, name)

    @classmethod
    def search_purchase_field(cls, name, clause):
        if name == 'purchase_state':
            name = 'state'
        return [('purchase.' + name,) + tuple(clause[1:])]
