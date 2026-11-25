Custom development to adapt res_partner to the context of social services for Accompagner.

## Data model

On `res.partner`:

Partners are divided into 4 types in the field social_type:
- accompagner, itself divided in two:
  - is_social_benefactor
  - is_social_volunteer
  - is_employee (standard field)
- beneficiary
- partner
- other

Partners that have fsm_location set to True, ie. which correspond
to location rather than to actual people, are filtered out from
dropdowns by default. They are also hidden by default from the partners
view in contacts and fieldservice -> master data -> customers.

The following fields have also been added:
- `social_beneficiary_ids` / `social_partner_ids`: many2many relations
  between partners and beneficiaries (through the
  `beneficiary_partner_rel` table).
- `social_file_creation_date`: date of creation of the social file
  (defaults to today, required).
- Properties fields per contact type (`social_beneficiary_properties`,
  `social_volunteer_properties`, `social_partner_properties`,
  `social_benefactor_properties`), defined per company.
- Per-type fields: orientation, GDPR, spoken language, residence permit
  title and residence right, contact person, civil status, children
  count, household type, resource and "in Belgium since" date for
  beneficiaries; professional status, personal email, nationality, contact
  method, volunteer types, motivations and volunteer course lines for
  volunteers; structure for partners.

On `res.company`:

- Properties definitions for each social contact type
  (`partner_properties_definition_social_beneficiary`,
  `..._social_volunteer`, `..._social_partner`, `..._social_benefactor`).

## Configuration

The following configuration models are manageable from Contacts >
Configuration > Social Service (with an "access social services
configuration" group), with full access for administrators and read-only
access for other internal users:

- Orientation (`partner.social.orientation`)
- Residence Permit Title (`partner.social.residence.permit.title`)
- Residence Right (`partner.social.residence.right`)
- Civil Status (`partner.social.civil.status`)
- Household Type (`partner.social.household.type`)
- Resource (`partner.social.resource`)
- Volunteer Professional Status
  (`partner.social.volunteer.professional.status`)
- Volunteer Contact Method (`partner.social.volunteer.contact.method`)
- Volunteer Type (`partner.social.volunteer.type`)
- Volunteer Motivation (`partner.social.volunteer.motivation`)
- Structure (`partner.social.structure`)

Volunteer course lines (`partner.social.volunteer.course`) are managed
directly on the partner form (editors need contact creation rights).

## Security

- An "Access Beneficiary Informations Group" group gates the visibility of
  the Beneficiary tab.
- An "Access social services configuration" group gates the Social Service
  configuration menu.

## Views adaptation

The partner form is adapted per social type:

Beneficiary (`social_type == 'beneficiary'`):

- Hide the VAT and the company name field.
- Hide the Salesperson, Purchase, Company Registry, Company and Sector of
  Activity fields on the Sales & Purchase tab (only the Reference and the
  File Creation Date stay).
- Hide the Invoicing tab.
- Hide the Fiscal Information group (fiscal position and tax receipt
  option).
- Hide the "Tax Receipt Option" field and the "Tax Receipts" stat button
  (from `donation_base`).
- Hide the "Partner Assignment" tab (from `base_geolocalize`).
- Hide the "Field Service" tab (from `fieldservice`).
- Show the "Beneficiary" tab (restricted to the "Access Beneficiary
  Informations Group" group) with linked partners, beneficiary properties
  and beneficiary information.

Accompagner (`social_type == 'accompagner'`):

- Hide the VAT and the company name field.
- Hide the Salesperson, Purchase, Company Registry, Company and Sector of
  Activity fields on the Sales & Purchase tab (only the Reference, the
  File Creation Date and the "Tax Receipt Option" stay).
- On the Invoicing tab, keep only the Bank Accounts table (hide Customer
  Invoices, Accounting Entries, Credit Limits and Automation groups).
- Hide the fiscal position field.
- Hide the "Partner Assignment" tab (from `base_geolocalize`).
- Hide the "Field Service" tab (from `fieldservice`).
- Show the "Volunteer" tab (when the partner is flagged as volunteer) with
  volunteer properties, information and course, and the "Benefactor" tab
  (when the partner is flagged as benefactor) with benefactor properties.

Partner (`social_type == 'partner'`):

- Hide the "Partner Assignment" tab (from `base_geolocalize`).
- Hide the "Field Service" tab (from `fieldservice`).
- Show the "Partner" tab with linked beneficiaries, partner properties and
  structure.
