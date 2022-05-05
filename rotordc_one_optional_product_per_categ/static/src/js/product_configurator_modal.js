odoo.define("rotordc_one_optional_product_per_categ.o_p_modal", function (require) {
    "use strict";

    var OptionalProductsModal = require("sale.OptionalProductsModal");

    OptionalProductsModal.include({
        _getCategId: function (element) {
            return element.find("input.product_categ_id").val();
        },
        _categIdFromProductId: function (product_id) {
            var product = this.$modal.find(`input.product_id[value=${product_id}]`);
            if (product === null) {
                // FIXME: error handling idk
                return undefined;
            }
            product = product.parents(".js_product:first");
            return this._getCategId(product);
        },
        _onAddOption: function ($modal, $parent, productTemplateId) {
            var categ_id = this._getCategId($parent);
            var products = this.getSelectedProducts();
            for (var i = 0; i < products.length; i++) {
                if (this._categIdFromProductId(products[i].product_id) === categ_id) {
                    // TODO: Pop-up, cleanly abort.
                    console.log("SAME CATEGORY ABORT");
                    return;
                }
            }
            this._super($modal, $parent, productTemplateId);
        },
    });
});
