/** @odoo-module **/
// Copyright 2022 Coop IT Easy SC
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import {WebsiteSale} from "website_sale.website_sale";
import {patch} from "@web/core/utils/patch";

patch(WebsiteSale.prototype, "RotorDC customization", {
    _onChangeCombination: function (ev, $parent, combination) {
        var $barcode = $parent.find(
            ".oe_product_barcode:first .oe_product_barcode_value"
        );
        $barcode.html(combination.barcode);
        this._super(ev, $parent, combination);
    },
});
