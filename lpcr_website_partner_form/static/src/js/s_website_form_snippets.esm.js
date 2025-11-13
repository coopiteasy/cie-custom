/** @odoo-module **/
// SPDX-FileCopyrightText: 2025 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import "website.s_website_form";
import {patch} from "@web/core/utils/patch";
import publicWidget from "web.public.widget";

patch(publicWidget.registry.s_website_form.prototype, "lpcr_website_parner_form", {
    getURLParameters() {
        // This code comes from https://stackoverflow.com/a/827378. A more
        // modern approach would be to use URLSearchParams
        // (https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams),
        // but this is more compatible.
        const params = {};
        // Get params and remove leading "?"
        const url_params = window.location.search.substring(1);

        const items = url_params.split("&");

        items.forEach((item) => {
            const [key, value] = item.split("=");
            params[decodeURIComponent(key)] = decodeURIComponent(value);
        });

        return params;
    },

    setCompany() {
        // Magic field
        // The presence of a magic field in the form triggers custom
        // validation of the form.
        const $target = this.$target;
        const $magic_input = $target.find("input[name='form_type']");
        if ($magic_input.length && $magic_input.val() === "customer_form") {
            const params = this.getURLParameters();
            const $company_select = $target.find("select[name='company_id']");
            if ($company_select.length) {
                $company_select[0].value = params.company_id;
            }
        }
    },

    start() {
        const res = this._super(...arguments);
        this.setCompany();
        return res;
    },

    update_status(status) {
        const res = this._super(...arguments);
        console.log("in update_status function");
        if (status === "success") {
            this.__started.then(() => this.setCompany());
        }
        return res;
    },

    async send(e) {
        // Prevent the default submit behavior
        e.preventDefault();

        const $target = this.$target;

        // Magic field
        // The presence of a magic field in the form trigger custom
        // validation of the form.
        const $magic_input = $target.find("input[name='form_type']");
        if ($magic_input.length && $magic_input.val() === "customer_form") {
            // Set some field required if company and other if not
            const is_company = $target.find("input[name='is_company']").is(":checked");
            const $name_input = $target.find("input[name='name']");
            const $siret_input = $target.find("input[name='siret']");
            const $firstname_input = $target.find("input[name='firstname']");
            const $lastname_input = $target.find("input[name='lastname']");
            if (is_company) {
                $name_input.prop("required", true);
                $siret_input.prop("required", true);
                $firstname_input.prop("required", false);
                $lastname_input.prop("required", false);
            } else {
                $name_input.prop("required", false);
                $siret_input.prop("required", false);
                $firstname_input.prop("required", true);
                $lastname_input.prop("required", true);
            }

            // Only one of the email, phone or postal address must be required
            const $email_input = $target.find("input[name='email']");
            const $phone_input = $target.find("input[name='phone']");
            const $street_input = $target.find("input[name='street']");
            const $city_input = $target.find("input[name='city']");
            const $zip_input = $target.find("input[name='zip']");
            const $country_input = $target.find("input[name='country_id']");
            if ($email_input.length && $email_input.val()) {
                $email_input.prop("required", true);
                $phone_input.prop("required", false);
                $street_input.prop("required", false);
                $city_input.prop("required", false);
                $zip_input.prop("required", false);
                $country_input.prop("required", false);
            } else if ($phone_input.length && $phone_input.val()) {
                $email_input.prop("required", false);
                $phone_input.prop("required", true);
                $street_input.prop("required", false);
                $city_input.prop("required", false);
                $zip_input.prop("required", false);
                $country_input.prop("required", false);
            } else if ($street_input.length && $street_input.val()) {
                $email_input.prop("required", false);
                $phone_input.prop("required", false);
                $street_input.prop("required", true);
                $city_input.prop("required", true);
                $zip_input.prop("required", true);
                $country_input.prop("required", true);
            } else {
                $email_input.prop("required", true);
                $phone_input.prop("required", true);
                $street_input.prop("required", true);
                $city_input.prop("required", true);
                $zip_input.prop("required", true);
                $country_input.prop("required", true);
            }
        }
        return this._super(...arguments);
    },
});
