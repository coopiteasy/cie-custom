/** @odoo-module */

// SPDX-FileCopyrightText: 2025 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import {Order, Orderline} from "point_of_sale.models";
import Registries from "point_of_sale.Registries";

const SppCustomOrder = (OriginalOrder) =>
    class extends OriginalOrder {
        get_total_foodprint_amount() {
            let fp_amount = 0.0;

            this.orderlines.forEach(function (orderline) {
                const product = orderline.get_product();
                if (product.is_foodprint_label) {
                    fp_amount += orderline.get_price_with_tax();
                }
            });

            return fp_amount;
        }

        export_for_printing() {
            const receipt = super.export_for_printing();
            receipt.total_foodprint_amount = this.get_total_foodprint_amount();
            return receipt;
        }
    };

const SppCustomOrderline = (OriginalOrderline) =>
    class extends OriginalOrderline {
        export_for_printing() {
            const receiptline = super.export_for_printing();
            receiptline.is_foodprint_label = this.get_product().is_foodprint_label;
            return receiptline;
        }
    };

Registries.Model.extend(Order, SppCustomOrder);
Registries.Model.extend(Orderline, SppCustomOrderline);
