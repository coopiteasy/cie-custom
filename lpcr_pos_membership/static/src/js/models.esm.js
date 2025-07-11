/** @odoo-module **/

import {Order, Orderline, PosGlobalState} from "point_of_sale.models";
import {Gui} from "point_of_sale.Gui";
import {Model} from "point_of_sale.Registries";
import {parseDate} from "@web/core/l10n/dates";

const LPCRPosMembershipOrder = (OriginalOrder) =>
    class extends OriginalOrder {
        select_orderline(line) {
            super.select_orderline(line);
            this.pos.numpadMode = "price";
        }
    };

Model.extend(Order, LPCRPosMembershipOrder);

const LPCRPosMembershipOrderline = (OriginalOrderline) =>
    class extends OriginalOrderline {
        set_quantity(quantity, keep_price) {
            // Quantity values "" and "remove" must be allowed because these
            // are the normal values the quantity passes through when removing
            // an order line.
            if (this.product.membership && ![1, "1", "", "remove"].includes(quantity)) {
                Gui.showPopup("ErrorPopup", {
                    title: this.pos.env._t("Quantity other than 1 not allowed"),
                    body: this.pos.env._t(
                        "Membership products must have a quantity equal to one."
                    ),
                });
                return false;
            }
            return super.set_quantity(quantity, keep_price);
        }
    };

Model.extend(Orderline, LPCRPosMembershipOrderline);

const LPCRPosMembershipPosGlobalState = (OriginalPosGlobalState) =>
    class extends OriginalPosGlobalState {
        constructor(obj) {
            super(obj);
            this.numpadMode = "price";
        }
        isMembershipEnding(partner) {
            if (partner && partner.is_member && partner.membership_stop) {
                return parseDate("+1m") > parseDate(partner.membership_stop);
            }
            return false;
        }
    };

Model.extend(PosGlobalState, LPCRPosMembershipPosGlobalState);
