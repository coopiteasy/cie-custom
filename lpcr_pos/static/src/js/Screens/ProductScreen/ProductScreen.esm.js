/** @odoo-module **/
// SPDX-FileCopyrightText: 2025 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import ProductScreen from "point_of_sale.ProductScreen";
import Registries from "point_of_sale.Registries";

const LPCRProductScreen = (ProductScreen_) =>
    class extends ProductScreen_ {
        get controlButtons() {
            if (this.env.pos.isManager) {
                return super.controlButtons;
            }
            return super.controlButtons.filter(
                (button) =>
                    ![
                        "OrderlineCustomerNoteButton",
                        "RefundButton",
                        "ProductInfoButton",
                    ].includes(button.name)
            );
        }
    };

Registries.Component.extend(ProductScreen, LPCRProductScreen);

export default ProductScreen;
