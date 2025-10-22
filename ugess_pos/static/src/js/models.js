odoo.define("ugess_pos.models", function (require) {
    "use strict";

    const {Order, Orderline, PosGlobalState} = require("point_of_sale.models");
    const Registries = require("point_of_sale.Registries");

    // eslint-disable-next-line no-shadow
    const OverloadPosGlobalState = (PosGlobalState) =>
        // eslint-disable-next-line no-shadow
        class OverloadPosGlobalState extends PosGlobalState {
            format_date_fr(date_value) {
                return new Date(date_value).toLocaleDateString("fr-FR");
            }
        };

    // eslint-disable-next-line no-shadow
    const UgessOrderline = (Orderline) =>
        // eslint-disable-next-line no-shadow
        class UgessOrderline extends Orderline {
            export_as_JSON() {
                var json = super.export_as_JSON(...arguments);
                const totals_without_any_discount =
                    this.get_total_without_any_discount();
                json.total_without_any_discount =
                    totals_without_any_discount.total_included;
                return json;
            }
        };

    // eslint-disable-next-line no-shadow
    const UgessOrder = (Order) =>
        // eslint-disable-next-line no-shadow
        class UgessOrder extends Order {
            get_expenditure_ceiling_current() {
                const partner = this.get_partner();
                if (partner && partner.expenditure_ceiling_current) {
                    return partner.expenditure_ceiling_current;
                }
                return undefined;
            }

            get_remaining_expenditure_amount() {
                const partner = this.get_partner();
                if (partner && partner.expenditure_ceiling_current) {
                    var res =
                        partner.expenditure_ceiling_current -
                        partner.expenditure_ceiling_current_total_sale_amount;
                    // The order is finalized when it is paid
                    // the order is locked when it is reloaded after
                    // In that both case, we don't want to take into account
                    // current order
                    if (!this.finalized && !this.locked) {
                        res -= this.get_total_with_tax() + this.get_rounding_applied();
                    }
                    return res;
                }
                return undefined;
            }

            get_remaining_expenditure_until() {
                const partner = this.get_partner();
                if (partner && partner.expenditure_ceiling_current_period_end_date) {
                    return moment(
                        partner.expenditure_ceiling_current_period_end_date
                    ).format("dddd Do MMMM");
                }
                return undefined;
            }

            export_for_printing() {
                var receipt = super.export_for_printing(...arguments);
                var remaining_expenditure_amount =
                    this.get_remaining_expenditure_amount();
                if (remaining_expenditure_amount) {
                    receipt.remaining_expenditure_amount = this.pos.format_currency(
                        remaining_expenditure_amount
                    );
                }
                receipt.remaining_expenditure_until =
                    this.get_remaining_expenditure_until();
                return receipt;
            }
        };

    Registries.Model.extend(Order, UgessOrder);
    Registries.Model.extend(PosGlobalState, OverloadPosGlobalState);
    Registries.Model.extend(Orderline, UgessOrderline);
});
