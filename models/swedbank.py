from openerp import models, fields


class SwedbankPaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    swedbank_PRIVATE_KEY = fields.Char('Private Key', size=256, help='Path to Private Key')
    swedbank_BANK_CERT = fields.Char('Bank Certificate', size=256, help='Path to Bank Certificate')

    def _get_providers(self, cr, uid, context=None):
        providers = super(SwedbankPaymentAcquirer, self)._get_providers(cr, uid, context=context)
        providers.append(['swedbank', 'Swedbank'])
        return providers

    def swedbank_form_generate_values(self, cr, uid, id, partner_values, tx_values, context=None):
        return self.banklink_form_generate_values(cr, uid, id, partner_values, tx_values, context=context)

    def swedbank_get_private_key(self):
        return self.swedbank_PRIVATE_KEY

    def swedbank_get_bank_cert(self):
        return self.swedbank_BANK_CERT

    def swedbank_get_form_action_url(self, cr, uid, id, context=None):
        env = self.read(cr, uid, id, ['environment'], context=context)['environment']
        return env == 'prod' and 'https://www.swedbank.ee/banklink' or 'http://localhost:3480/banklink/swedbank-common'
