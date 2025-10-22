odoo.define("ugess_pos.PaymentScreen", function (require) {
    "use strict";

    const PaymentScreen = require("point_of_sale.PaymentScreen");
    const Registries = require("point_of_sale.Registries");

    // eslint-disable-next-line no-shadow
    const OverloadPaymentScreen = (PaymentScreen) =>
        // eslint-disable-next-line no-shadow
        class OverloadPaymentScreen extends PaymentScreen {
            async _finalizeValidation() {
                var client = this.currentOrder.get_partner();

                if (client && client.expenditure_ceiling_current) {
                    client.expenditure_ceiling_current_total_sale_amount +=
                        this.currentOrder.get_total_with_tax();
                }

                return await super._finalizeValidation(...arguments);
            }

            async _isOrderValid() {
                var has_membership_products = false;
                var has_normal_products = false;
                this.currentOrder.get_orderlines().forEach(function (order_line) {
                    if (order_line.product.membership) {
                        has_membership_products = true;
                    } else {
                        has_normal_products = true;
                    }
                });
                if (has_membership_products && has_normal_products) {
                    this.showPopup("ErrorPopup", {
                        title: this.env._t("Incorrect Order"),
                        body: this.env._t(
                            "You can not create an order with membership" +
                                " products and normal products."
                        ),
                    });
                    return false;
                }

                return await super._isOrderValid(...arguments);
            }
            get remainingExpenditureAmountText() {
                if (this.currentOrder.get_remaining_expenditure_amount()) {
                    return (
                        this.env._t("Ceiling remaining: ") +
                        this.env.pos.format_currency(
                            this.currentOrder.get_remaining_expenditure_amount()
                        )
                    );
                }
                return this.env._t("No ceiling");
            }
            get remainingExpenditureUntilText() {
                if (this.currentOrder.get_remaining_expenditure_until()) {
                    return (
                        this.env._t("Until: ") +
                        this.currentOrder.get_remaining_expenditure_until()
                    );
                }
                return this.env._t("No ceiling");
            }
        };

    Registries.Component.extend(PaymentScreen, OverloadPaymentScreen);

    return PaymentScreen;
});
