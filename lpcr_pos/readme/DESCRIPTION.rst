Customize the PoS according to LPCR specifications.

This module hides several buttons for regular users (not for managers):

* Top header:

  * Cash In/Out
* Product screen:

  * Customer Note
  * Refund
  * Info
  * Quotation/Order (from ``pos_sale`` module)
* Customer selection screen:

  * Create
  * Details
* Payment screen:

  * Customer

Additionally, this module also hides the same data hidden by the ``pos_hide_partner_info`` module, but does not depend on it because that data should still be visible by managers.
For this module to work properly, ``pos_hide_partner_info`` must not be installed.
