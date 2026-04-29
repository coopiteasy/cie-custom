/** @odoo-module **/
// SPDX-FileCopyrightText: 2026 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import PosComponent from "point_of_sale.PosComponent";
import Registries from "point_of_sale.Registries";

class LpcrPosButtons extends PosComponent {
    get companyId() {
        return this.env.pos.company && this.env.pos.company.id;
    }
}

LpcrPosButtons.template = "LpcrPosButtons";
Registries.Component.add(LpcrPosButtons);
export default LpcrPosButtons;
