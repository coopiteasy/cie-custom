odoo.define("rotordc_one_optional_product_per_categ.o_p_modal", function (require) {
    "use strict";

    var OptionalProductsModal = require("sale.OptionalProductsModal");

    OptionalProductsModal.include({
        _getCategId: function ($element) {
            return $element.find("input.product_categ_id").val();
        },
        _categIdFromProductId: function (product_id) {
            var $product = this.$modal.find(`input.product_id[value=${product_id}]`);
            if ($product === null) {
                // FIXME: error handling idk
                return undefined;
            }
            $product = $product.parents(".js_product:first");
            return this._getCategId($product);
        },
        _onAddOption: function ($modal, $parent, productTemplateId) {
            var categ_id = this._getCategId($parent);
            var self = this;

            // Disable all 'add to cart' buttons of products of the same
            // internal category.
            $modal
                .find(".js_product:not(.in_cart):not(.main_product)")
                .each(function () {
                    var $item = $(this);
                    var item_product_id = $item.find(".product_id").val();
                    if (
                        item_product_id !== $parent.find(".product_id").val() &&
                        self._getCategId($item) === categ_id
                    ) {
                        var $button = $item.find("a.js_add");
                        $button.addClass("disabled");
                    }
                });

            this._super($modal, $parent, productTemplateId);
        },
        _onRemoveOption: function ($modal, $parent, productTemplateId) {
            var categ_id = this._getCategId($parent);
            var self = this;

            // Re-enable all buttons.
            $modal.find(".js_product:not(.main_product)").each(function () {
                var $item = $(this);
                if (self._getCategId($item) === categ_id) {
                    var $button = $item.find("a.js_add");
                    $button.removeClass("disabled");
                }
            });

            this._super($modal, $parent, productTemplateId);
        },
    });
});
