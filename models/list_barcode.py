from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, date, timedelta
import json, requests, re

import logging
_logger = logging.getLogger(__name__)



#class ProductlistBarcode(models.Model):

class ProductlistBarcode(models.TransientModel):    
    _name = 'bettaerp_weight_barcode.productlistbarcode'
    _description = 'Listado de Productos para la Balanza Electronica'
    
    #name    = fields.Char(string="Descripcion",default="Directorio de exportacion")

    archivo = fields.Char(string = "Seleccion de Directorio", default = 'C:/')
    #fields.Many2one('bettaerp.weight.barcode.directorio', string='Directorios')
    #fields.Char(string = "Seleccion de Directorio", store=True, default = 'C:/')
    

    def barcode_list(self):
        _logger.warning(self,)
        product_data = self.env['product.template'].sudo().search([('weight_barcode', '=', True)])
        
        _logger.warning(product_data,)
        if product_data :
            _logger.warning("encontre producto s",)    
        
        
                 #for rec in self:
        #    if rec.weight_barcode:
        _logger.warning("Comienzo a armar el txt",)

        #def direccionarchivo(self):
        #    _logger.warning(self.id,)
        #    return self.id
    
    class DirectirioArchivo(models.Model):
        _name = 'bettaerp_weight_barcode.directirioarchivo'
        _description = 'base de directorios para enviar archivo'
            
        name    = fields.Char(string="Descripcion",default="Directorio")    
        directorio = fields.Char(string = "Directorio", store=True, default = 'C:/')

