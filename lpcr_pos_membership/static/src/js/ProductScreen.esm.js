/** @odoo-module **/

import {Component} from "point_of_sale.Registries";
import ProductScreen from "point_of_sale.ProductScreen";

const LPCRPosMembershipProductScreen = (OriginalProductScreen) =>
    class extends OriginalProductScreen {
        async _onClickPay() {
            const partnerCounts = {};
            const idToName = {};

            this.currentOrder.get_orderlines().forEach((line) => {
                if (line.product.membership) {
                    const partner = line.partner_for_membership;
                    const partnerId = partner.id;
                    if (partnerCounts[partnerId]) {
                        partnerCounts[partnerId]++;
                    } else {
                        idToName[partnerId] = partner.name;
                        partnerCounts[partnerId] = 1;
                    }
                }
            });

            const duplicatesWithCount = Object.entries(partnerCounts)
                .filter(([, count]) => count > 1)
                .map(([partnerId, count]) => `${idToName[partnerId]} (${count})`);

            if (duplicatesWithCount.length > 0) {
                const duplicatesStr = duplicatesWithCount.join(", ");
                this.showPopup("ErrorPopup", {
                    title: this.env._t("Only one membership allowed per person"),
                    body: _.str.sprintf(
                        this.env._t("Some people have several memberships: %s"),
                        duplicatesStr
                    ),
                });
                return;
            }

            return super._onClickPay(...arguments);
        }
    };

Component.extend(ProductScreen, LPCRPosMembershipProductScreen);
