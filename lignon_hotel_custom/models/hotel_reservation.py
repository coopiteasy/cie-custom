from odoo import fields, models


class HotelReservation(models.Model):
    _inherit = "hotel.reservation"

    linked_to_event_hall_rental = fields.Boolean(
        string="Linked to Event Hall Rental"
    )
