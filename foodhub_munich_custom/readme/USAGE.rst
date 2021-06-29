Override the following record rules:
- `easy_my_coop.email_template_confirmation`
- `easy_my_coop.email_template_confirmation_company`
fields added:
- report_template
- report_name

Note: the parent record rule is inside a `<data noupdate="1">` element and
- will be rewritten on module install
- will not be rewritten on module updates.
In the latter, the record rule should be first deleted in order to be recreated.
