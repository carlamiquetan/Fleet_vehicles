# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vehicle(models.Model):
    _name = 'fleet_vehicles.fleet_vehicles'
    _description = 'Vehicle in a fleet of vehicles'

    purchase_date = fields.Date('Purchase Date')
    mileage = fields.Integer('Mileage')
    purchase_price = fields.Float('Purchase Price in USD')
    model = fields.Char('Vehicle Model')
    brand = fields.Char('Brand')
    license_plate = fields.Char('License Plate')
    current_price = fields.Float('Current Price in USD')
    maintenances = fields.Integer('Maintenances', compute='_compute_maintenances')

    @api.onchange('mileage')
    def onchange_mileage(self):
        mileage_to_discount = 10000
        percentage_to_discount = 0.05
        for vehicle in self:
            discount_times = vehicle.mileage//mileage_to_discount
            current_price = vehicle.purchase_price - vehicle.purchase_price*percentage_to_discount*discount_times
            vehicle.current_price = current_price

    @api.depends('purchase_date')
    def _compute_maintenances(self):
        for vehicle in self:
            delta = fields.Date.today() - vehicle.purchase_date
            # assuming months always have 30 days. By using dateutil this might be make more realistic
            months = delta.days // 30
            vehicle.maintenances = months // 6


