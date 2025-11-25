
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/coopiteasy/cie-custom/actions/workflows/pre-commit.yml/badge.svg?branch=16.0)](https://github.com/coopiteasy/cie-custom/actions/workflows/pre-commit.yml?query=branch%3A16.0)
[![Build Status](https://github.com/coopiteasy/cie-custom/actions/workflows/test.yml/badge.svg?branch=16.0)](https://github.com/coopiteasy/cie-custom/actions/workflows/test.yml?query=branch%3A16.0)
[![codecov](https://codecov.io/gh/coopiteasy/cie-custom/branch/16.0/graph/badge.svg)](https://codecov.io/gh/coopiteasy/cie-custom)
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
[bao_supplier_certificate](bao_supplier_certificate/) | 16.0.1.0.0 | <a href='https://github.com/remytms'><img src='https://github.com/remytms.png' width='32' height='32' style='border-radius:50%;' alt='remytms'/></a> | Custom certificates for supplier of Boucher À Oreilles
[cookingo_custom](cookingo_custom/) | 16.0.1.0.0 |  | Custom modifications for Cookingo.
[foodhub_custom](foodhub_custom/) | 16.0.1.0.0 |  | Foodhub customizations
[foodhub_custom_product_kanban_view](foodhub_custom_product_kanban_view/) | 16.0.1.0.0 | <a href='https://github.com/remytms'><img src='https://github.com/remytms.png' width='32' height='32' style='border-radius:50%;' alt='remytms'/></a> | Adapt the kanban view for product
[foodhub_picking](foodhub_picking/) | 16.0.1.1.0 |  | Foodhub customizations : sort picking operations by category and reference
[foodhub_product_fields](foodhub_product_fields/) | 16.0.1.0.0 | <a href='https://github.com/victor-champonnois'><img src='https://github.com/victor-champonnois.png' width='32' height='32' style='border-radius:50%;' alt='victor-champonnois'/></a> | Set Mandatory and Copy Options to Fields in Product
[lpcr_donation_tax_report](lpcr_donation_tax_report/) | 16.0.2.0.0 | <a href='https://github.com/remytms'><img src='https://github.com/remytms.png' width='32' height='32' style='border-radius:50%;' alt='remytms'/></a> | Custom tax report for donation
[lpcr_pos](lpcr_pos/) | 16.0.1.0.0 |  | Customize the PoS according to LPCR specifications
[lpcr_pos_membership](lpcr_pos_membership/) | 16.0.1.0.0 | <a href='https://github.com/flaenen'><img src='https://github.com/flaenen.png' width='32' height='32' style='border-radius:50%;' alt='flaenen'/></a> | POS Membership customizations for LPCR
[lpcr_website_partner_form](lpcr_website_partner_form/) | 16.0.1.0.2 | <a href='https://github.com/remytms'><img src='https://github.com/remytms.png' width='32' height='32' style='border-radius:50%;' alt='remytms'/></a> | Add a form to add partners from website.
[medor_custom_stats](medor_custom_stats/) | 16.0.1.0.0 |  | Compute stats on number of subscribers and number of cooperators
[rotordc_autofill_product_variant](rotordc_autofill_product_variant/) | 16.0.1.0.0 |  | Autofill some field of the product variant based on the product template.
[rotordc_custom](rotordc_custom/) | 16.0.1.0.0 |  | Customization for RotorDC
[rotordc_optional_product](rotordc_optional_product/) | 16.0.1.0.0 |  | Custom modifications regarding RotorDC's use of optional products.
[rotordc_report_picking_huge_sale_order](rotordc_report_picking_huge_sale_order/) | 16.0.1.0.0 |  | At the bottom of the Picking Operations report, display the sale order in huge text
[rotordc_sale_related_so](rotordc_sale_related_so/) | 16.0.1.0.0 | <a href='https://github.com/robinkeunen'><img src='https://github.com/robinkeunen.png' width='32' height='32' style='border-radius:50%;' alt='robinkeunen'/></a> | Add M2M links between SOs
[sawb_custom_contact_interface](sawb_custom_contact_interface/) | 16.0.1.0.0 | <a href='https://github.com/victor-champonnois'><img src='https://github.com/victor-champonnois.png' width='32' height='32' style='border-radius:50%;' alt='victor-champonnois'/></a> | SAWB Custom : Contact Interface.
[sawb_custom_hide_vat_for_individual](sawb_custom_hide_vat_for_individual/) | 16.0.1.0.0 | <a href='https://github.com/victor-champonnois'><img src='https://github.com/victor-champonnois.png' width='32' height='32' style='border-radius:50%;' alt='victor-champonnois'/></a> | Hide the partner's VAT field if the partner is an individual.
[spp_custom](spp_custom/) | 16.0.1.0.0 |  | Specifics customizations for SPP
[spp_pos_mustard](spp_pos_mustard/) | 16.0.1.0.0 | <a href='https://github.com/carmenbianca'><img src='https://github.com/carmenbianca.png' width='32' height='32' style='border-radius:50%;' alt='carmenbianca'/></a> | Make a button in the POS interface mustard-coloured.

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Coop IT Easy SC
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
<!-- /!\ Non OCA Context : Set here the full description of your organization. -->
