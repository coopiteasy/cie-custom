/** @odoo-module **/

import "website.s_website_form";
import {patch} from "@web/core/utils/patch";
import publicWidget from "web.public.widget";

patch(publicWidget.registry.s_website_form.prototype, "lpcr_website_parner_form", {
    getURLParameters() {
        const params = {};
        // Get params and remove leading "&"
        const url_params = window.location.search.substring(1);

        const items = url_params.split("&");

        items.forEach((item) => {
            const [key, value] = item.split("=");
            params[decodeURIComponent(key)] = decodeURIComponent(value);
        });

        return params;
    },

    start() {
        const res = this._super(...arguments);
        // Magic field
        // The presence of a magic field in the form trigger custom
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

            // Only one of the email or postal address must be required
            const $email_input = $target.find("input[name='email']");
            const $phone_input = $target.find("input[name='phone']");
            const $street_input = $target.find("input[name='street']");
            const $city_input = $target.find("input[name='city']");
            const $zip_input = $target.find("input[name='zip']");
            const $country_input = $target.find("input[name='contry_id']");
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
