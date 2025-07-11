/** @odoo-module **/

import {Component} from "point_of_sale.Registries";
import ProductScreen from "point_of_sale.ProductScreen";

const LPCRPosMembershipProductScreen = (OriginalProductScreen) =>
    class extends OriginalProductScreen {
        async _onClickPay() {
            const partnerCounts = {};
            const idToName = {};
            const membershipLinesWithoutPartner = [];
            const membershipLinesWithIncorrectQuantity = [];

            this.currentOrder.get_orderlines().forEach((line) => {
                if (line.product.membership) {
                    if (line.quantity !== 1) {
                        membershipLinesWithIncorrectQuantity.push(line);
                        return;
                    }
                    const partner = line.partner_for_membership;
                    if (!partner) {
                        membershipLinesWithoutPartner.push(line);
                        return;
                    }
                    const partnerId = partner.id;
                    if (partnerCounts[partnerId]) {
                        partnerCounts[partnerId]++;
                    } else {
                        idToName[partnerId] = partner.name;
                        partnerCounts[partnerId] = 1;
                    }
                }
            });

            if (membershipLinesWithIncorrectQuantity.length !== 0) {
                this.showPopup("ErrorPopup", {
                    title: this.env._t("Quantity other than 1 not allowed"),
                    body: this.env._t(
                        "Membership products must have a quantity equal to one."
                    ),
                });
                return;
            }

            if (membershipLinesWithoutPartner.length !== 0) {
                this.showPopup("ErrorPopup", {
                    title: this.env._t("Membership without people"),
                    body: this.env._t("Please select a person for the membership."),
                });
                return;
            }

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
