from odoo import models, fields
import logging as log
import datetime


class VehiclesReportWizard(models.TransientModel):
    _name = 'vehicles.report.wizard'
    _description = 'Used for report - Vehicles by purchase date'

    purchase_date_from = fields.Date('From', default=datetime.date(1990, 1, 1))
    purchase_date_to = fields.Date('To', default=datetime.datetime.today())

    def generate_report(self):
        self.ensure_one()
        vehicles = self.env["fleet_vehicles.fleet_vehicles"].search_read(
            [
                ('purchase_date', '>=', self.purchase_date_from),
                ('purchase_date', '<=', self.purchase_date_to),
            ]
        )
        log.info(vehicles)
        data = {
            'form': self.read()[0],
            'vehicles': vehicles
        }
        return self.env.ref('fleet_vehicles.action_report_vehicles').report_action(self, data=data)
