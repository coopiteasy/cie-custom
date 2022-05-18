/*
    Copyright 2022 Coop IT Easy SCRLfs
    License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
*/

odoo.define("spp_custom.models", function (require) {
    "use strict";

    var models = require("point_of_sale.models");
    var order_prototype = models.Order.prototype;

    models.load_fields("product.product", ["is_foodprint_label"]);

    models.Order = models.Order.extend({
        get_total_foodprint_amount: function () {
            var fp_amount = 0.0;

            this.orderlines.each(function (orderline) {
                var product = orderline.get_product();
                if (product.is_foodprint_label) {
                    fp_amount += orderline.get_price_with_tax();
                }
            });

            return fp_amount;
        },

        export_for_printing: function () {
            var receipt = order_prototype.export_for_printing.apply(this);
            receipt.total_foodprint_amount = this.get_total_foodprint_amount();
            return receipt;
        },
    });
});
