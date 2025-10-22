# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "UGESS - multiprice pricetag",
    "summary": "Tag generation able to handle up to 5 different pricelists per"
    "tag and an additionnal pricelist for price per unit of measurement",
    "version": "16.0.1.0.0",
    "category": "Custom",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["mihien"],
    "license": "AGPL-3",
    "depends": [
        "base",
        "product_print_category",
        "ugess_pricelist_weight",
        "ugess_pricetag",
        "ugess_product_short_name",
        "ugess_supply_source",
    ],
    "data": [
        "data/multipricetag.xml",
        "views/view_product_print_category.xml",
    ],
}
