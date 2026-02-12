{
    "name": "UGESS Membership Reporting",
    "summary": "Rapports membres custom UGESS",
    "version": "16.0.1.0.0",
    "category": "Membership",
    "website": "https://coopiteasy.be",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "ugess_membership",
        "ugess_partner_household",
        "ugess_partner_revenue",
    ],
    "data": [
        "report/report_membership_views.xml",
    ],
    "demo": [],
    "qweb": [],
}
