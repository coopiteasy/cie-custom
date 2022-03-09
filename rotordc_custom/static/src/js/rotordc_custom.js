// Copyright 2022 Coop IT Easy SCRLfs
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("rotordc_custom.rotordc_custom", function (require) {
    "use strict";

    var sAnimations = require("website.content.snippets.animation");
    require("website_sale.website_sale");
    var WebsiteSale = sAnimations.registry.WebsiteSale;

    WebsiteSale.include({
        _onChangeCombination: function (ev, $parent, combination) {
            var $barcode = $parent.find(
                ".oe_product_barcode:first .oe_product_barcode_value"
            );
            $barcode.html(combination.barcode);
            this._super(ev, $parent, combination);
        },
    });
});
