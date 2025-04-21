/** @odoo-module **/
// SPDX-FileCopyrightText: 2025 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import {PosGlobalState} from "point_of_sale.models";
import Registries from "point_of_sale.Registries";

const LPCRPosGlobalState = (PosGlobalState_) =>
    class extends PosGlobalState_ {
        get isManager() {
            if (!this.user) {
                return false;
            }
            return this.user.role === "manager";
        }
    };

Registries.Model.extend(PosGlobalState, LPCRPosGlobalState);

export default PosGlobalState;
