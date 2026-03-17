/** @odoo-module **/
// SPDX-FileCopyrightText: 2026 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import {Model} from "point_of_sale.Registries";
import {PosGlobalState} from "point_of_sale.models";

const BloumCustomPrintZPLPosGlobalState = (PosGlobalState_) =>
    class extends PosGlobalState_ {
        get_zpl_barcode_label(
            title,
            barcode,
            value_str,
            label_width,
            label_height,
            label_offset_x,
            label_offset_y
        ) {
            const zpl_string = super.get_zpl_barcode_label(
                title,
                barcode,
                value_str,
                label_width,
                label_height,
                label_offset_x,
                label_offset_y
            );
            // Remove the text fields by filtering the instructions. In the
            // source string, text parts contain multiple instructions. They
            // start with a ^CF instruction (setting the font) and end (like
            // all fields) with a ^FS instruction. Note that the ^ sign in
            // regexes is not related to the one used to begin a ZPL
            // instruction: in regexes, it represents the beginning of the
            // string.
            let in_text = false;
            const filterZPL = (code) => {
                if (in_text) {
                    if (/^FS/.test(code)) {
                        in_text = false;
                    }
                    return false;
                }
                if (/^CF/.test(code)) {
                    in_text = true;
                    return false;
                }
                return true;
            };
            return zpl_string.split("^").filter(filterZPL).join("^");
        }
    };

Model.extend(PosGlobalState, BloumCustomPrintZPLPosGlobalState);
