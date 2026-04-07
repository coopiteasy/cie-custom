/** @odoo-module **/
// SPDX-FileCopyrightText: 2026 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import {Component} from "point_of_sale.Registries";
import NumpadWidget from "point_of_sale.NumpadWidget";

const PosFixedPriceNumpadWidget = (OriginalNumpadWidget) =>
    class extends OriginalNumpadWidget {
        changeMode(mode) {
            const orderLine = this.env.pos.get_order().get_selected_orderline();
            if (mode === "price" && orderLine) {
                const product = orderLine.product;
                if (product.is_pos_price_fixed) {
                    this.showPopup("ErrorPopup", {
                        title: this.env._t("Restricted access to product price"),
                        body: this.env
                            ._t(
                                "It is not allowed to change the price of this product: %(name)s"
                            )
                            .replace("%(name)s", product.display_name),
                    });
                    return;
                }
            }
            super.changeMode(mode);
        }
    };

Component.extend(NumpadWidget, PosFixedPriceNumpadWidget);

export default NumpadWidget;
