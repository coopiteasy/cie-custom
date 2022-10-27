
* add order volume to delivery slip
* add price information on delivery slip
* link picking to sale order
* link moves and move lines to sale order line
* hide product terms from website sale product page
* website: shop & product page accessible only for logged in users

Add a small text in customer credit notes document. This was done directly in the Odoo interface:
Created a view `report_invoice_document_custom_refund` inheriting from `report_invoice_document` as an extension view, and witht the following architecture.

    <?xml version="1.0"?>
    <data inherit_id="account.report_invoice_document">
    <xpath expr="//div[@id='total']/.." position="after">
    <p t-if="o.type == 'out_refund'">Please deduct this credit note from a future invoice or ask a refund.</p>
    </xpath>
    </data>

It has to be done again in case of migration
