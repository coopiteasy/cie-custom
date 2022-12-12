
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/coopiteasy/cie-custom/actions/workflows/pre-commit.yml/badge.svg?branch=12.0)](https://github.com/coopiteasy/cie-custom/actions/workflows/pre-commit.yml?query=branch%3A12.0)
[![Build Status](https://github.com/coopiteasy/cie-custom/actions/workflows/test.yml/badge.svg?branch=12.0)](https://github.com/coopiteasy/cie-custom/actions/workflows/test.yml?query=branch%3A12.0)
[![codecov](https://codecov.io/gh/coopiteasy/cie-custom/branch/12.0/graph/badge.svg)](https://codecov.io/gh/coopiteasy/cie-custom)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

# cie-custom

Custom modules for Coop IT Easy's clients.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_invoice_pos_already_paid](account_invoice_pos_already_paid/) | 12.0.1.0.0 |  | Remove sentence about payment communication from invoice based on the account journal
[bablmarket_custom](bablmarket_custom/) | 12.0.1.0.0 |  | Specifics customizations for Bablmarket
[bees_custom](bees_custom/) | 12.0.1.1.0 |  | Specifics customizations for BEES coop.
[coopiteasy_custom](coopiteasy_custom/) | 12.0.1.2.0 |  | Specific customizations for Coop IT Easy
[foodhub_copy_product_fields](foodhub_copy_product_fields/) | 12.0.1.0.0 | [![carmenbianca](https://github.com/carmenbianca.png?size=30px)](https://github.com/carmenbianca) | When duplicating a product, copy more fields over.
[foodhub_custom](foodhub_custom/) | 12.0.1.1.0 |  | Foodhub customizations
[foodhub_custom_product_kanban_view](foodhub_custom_product_kanban_view/) | 12.0.1.0.0 | [![remytms](https://github.com/remytms.png?size=30px)](https://github.com/remytms) | Adapt the kanban view for product
[foodhub_label_custom](foodhub_label_custom/) | 12.0.1.0.0 |  | Additional fields for product labels
[lesptitspots_worker_status](lesptitspots_worker_status/) | 12.0.1.0.0 |  | Worker status management specific to Les P'tit Pots.
[provelo_analytic_account](provelo_analytic_account/) | 12.0.1.0.0 |  | Match BOB analytical accounts.
[provelo_custom](provelo_custom/) | 12.0.1.6.0 |  | Pro Velo customizations
[provelo_custom_display_phone](provelo_custom_display_phone/) | 12.0.1.5.0 |  | Display phone number in sale order and invoice reports
[provelo_custom_timesheet_ui](provelo_custom_timesheet_ui/) | 12.0.1.0.1 |  | Small modifications to the Timesheets UI
[provelo_resource_activity_reports](provelo_resource_activity_reports/) | 12.0.1.0.1 |  | Reports for resource activities
[rotordc_autofill_product_variant](rotordc_autofill_product_variant/) | 12.0.1.0.1 |  | Autofill some field of the product variant based on the product template.
[rotordc_custom](rotordc_custom/) | 12.0.1.1.0 |  | Customization for RotorDC
[rotordc_invoice_link_down_payment](rotordc_invoice_link_down_payment/) | 12.0.1.0.0 | [![carmenbianca](https://github.com/carmenbianca.png?size=30px)](https://github.com/carmenbianca) | Register payments done through invoices as down payment on sale orders.
[rotordc_mail_activity_display_info](rotordc_mail_activity_display_info/) | 12.0.1.0.0 | [![carmenbianca](https://github.com/carmenbianca.png?size=30px)](https://github.com/carmenbianca) | Display the info of activities by default.
[rotordc_optional_product](rotordc_optional_product/) | 12.0.1.0.0 |  | Custom modifications regarding RotorDC's use of optional products.
[rotordc_payment_link_down_payment](rotordc_payment_link_down_payment/) | 12.0.1.0.1 | [![carmenbianca](https://github.com/carmenbianca.png?size=30px)](https://github.com/carmenbianca) | Register payments done with payment acquirers as down payment on sale orders.
[rotordc_product_storage_location](rotordc_product_storage_location/) | 12.0.1.0.0 | [![carmenbianca](https://github.com/carmenbianca.png?size=30px)](https://github.com/carmenbianca) | Select a storage location on products.
[rotordc_report_picking_huge_sale_order](rotordc_report_picking_huge_sale_order/) | 12.0.1.0.0 |  | At the bottom of the Picking Operations report, display the sale order in huge text.
[rotordc_sale_address](rotordc_sale_address/) | 12.0.1.0.0 | [![carmenbianca](https://github.com/carmenbianca.png?size=30px)](https://github.com/carmenbianca) | Display full address for invoice and delivery in sale order.
[rotordc_sale_invoice_comment](rotordc_sale_invoice_comment/) | 12.0.1.0.0 | [![carmenbianca](https://github.com/carmenbianca.png?size=30px)](https://github.com/carmenbianca) | Make sure that the terms & conditions are always set on all invoices, and don't display the reference on POS invoices.
[rotordc_sale_picking_state](rotordc_sale_picking_state/) | 12.0.1.0.0 | [![carmenbianca](https://github.com/carmenbianca.png?size=30px)](https://github.com/carmenbianca) | Set states for stock pickings on sale orders depending on the stock pickings' types.
[rotordc_website_theme](rotordc_website_theme/) | 12.0.1.0.0 |  | Website theme for RotorDC.
[spp_custom](spp_custom/) | 12.0.1.1.0 |  | Specifics customizations for SPP

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Coop IT Easy SC
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
<!-- /!\ Non OCA Context : Set here the full description of your organization. -->
