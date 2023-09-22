from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo import http
from werkzeug.utils import redirect
import requests

import webbrowser

#from datetime import datetime, date, timedelta
#import json, requests, re
#import platform
#import os

import logging
_logger = logging.getLogger(__name__)


class ProductTemplateProductWeight(models.Model):
    _inherit = "product.template"
    weight_barcode   = fields.Boolean('Genera Codigo de Barra', default=False)
    
    v_VENCIMIENTO = [("1","No muestra nada.(ni envasado ni vencimiento)"),
                   ("2","Muestra solo fecha de envasado"),
                   ("3","Fecha actual y vencimiento"),
                   ("4","Solo fecha de vencimiento")
                   ]
    tipo_vencimiento = fields.Selection(v_VENCIMIENTO,required= True,string="Tipo de Vencimiento", default='4')
    
    #fields.Integer(string = "Tipo de Vencimiento", required=True ,default = 4)
    #categoria_padre  = fields.Integer(string = "Categoria Padre", required=True)
    #categoria_padre  = fields.Many2one(
    #    'product.category', 'Product Category')
    
    
    p_PESABLE = [("1","Pesable"),
                 ("2","Solo Etiqueta")
                 ]
    pesable = fields.Selection(p_PESABLE,string="Producto Pesable",index=True,default='1')
    #fields.Integer(string = "Pesable", required=True ,default = 1)
    tara = fields.Float(string = "Tara", required=True ,default = 0.000)
    marca = fields.Integer(string = "Marca", required=True ,default = 1)



    def buscarcategoria(self):
        return self.categ_id[0].id
        
    @api.onchange('weight_barcode')
    def weight_barcode_fieldc(self):
        #FIXME Generar si el uom_id es pesable generar el barcode de acuerdo a la mascara del barcode rule
        #_logger.warning("*************************************")
        #_logger.warning(self,)
        #_logger.warning("*************************************")
        for rec in self:
            prod_pes =self.env['barcode.rule'].sudo().search([('type','=', 'weight')]).pattern
            if rec.weight_barcode:
                produ = str((rec._origin.id)).zfill(prod_pes.count('.'))
                ceroz=prod_pes.count('N')+prod_pes.count('D')
                rec.barcode =prod_pes[0:2]+produ+"0".zfill(ceroz)
                #rec.categoria_padre=rec.categ_id.id
            else: rec.barcode=""

    # def barcode_list(self):
    #     _logger.warning("*********barcode_list****************************")
    #     _logger.warning("*************************************")
    #     regis_1=''
    #     divisortxt = "|"
        
    #     for rec in self:
    #         produ = str((rec.id)).zfill(5)
    #         produ_cero = (str(rec.id)+'0').zfill(5)
    #         regis = produ + divisortxt + produ_cero + divisortxt + rec.name + divisortxt + str(rec.list_price) + divisortxt + str(rec.pesable) + divisortxt + str(rec.expiration_time) + divisortxt + str(rec.categ_id.id) + divisortxt + str(rec.tara) + divisortxt+ str(rec.marca) + divisortxt + str(rec.tipo_vencimiento)
            
    #         regis_1 = regis_1 + "\n" +regis
           
    #         _logger.warning(regis)
        
    #     _logger.warning(regis_1)
    #     lugar = "/home/balanzas.txt"
    #     fichero = open(lugar,'w')
    #     fichero.write(regis_1)
    #     fichero.close()
        
    #     #self.download_txt()
     
    
    def download_txt(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/home',
            'target': 'self',
        }
     
        
    #def download_txt(self):
        
        
    #    return redirect('https://www.hotmail.com')
        
    #    #action = self.env['ir.actions.act_url'].create({
        #    'name': 'Abrir Google',
        #    'url': 'https://www.google.com',
        #    'target': 'new',
        #})
        #return action
        
        
        #url = 'http://168.197.49.28:8069/home'
        
        #url = '/home' # Reemplaza esto con la ruta real de tu controlador
        #_logger.warning(url)
        #response = requests.get(url)
        #_logger.warning(response)
        
        #import webbrowser

        #url = 'https://www.google.com'
        #webbrowser.open(url)

        
        
        #return response
        
        #action = self.env.ref('bettaerp_weight_barcode.customer_index_action')
        #_logger.warning(action)
        
        #action_data = action.read()[0]
        #_logger.warning(action_data)
        #return action_data

        #url = 'http://168.197.49.28:8069/home'
        #_logger.warning(url)
        
        #webbrowser.open_new(url)
        
        #webbrowser.get('google-chrome').open(url)
        
        
        
        
        # response = http.requests.get(url)

        # _logger.warning(response)

        # if response.status_code == 200:
        #     #    La petición fue exitosa
        #     contenido = response.content
        
        # else:
        #     # La petición falló
        #     contenido = None
        # _logger.warning(contenido)
        # return contenido



        #controller_url = http.request.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/home'
        #_logger.warning(controller_url)
        
        #return controller_url
        
        
        ## Guardar los registros en el TXT
              
 
 
    
    
        
    #def guardartxt(self,cdna,inicio):
    #    lugar = "/home/balanzas.txt"
        
    #    if inicio: valor='a'
    #    else: valor='w'
            
    #    fichero = open(lugar,valor)
        
    #    cdna = cdna + "\n"
    #    _logger.warning(cdna)
    #    fichero.write(cdna)
    #    fichero.close()
            

class ProductProductWeight(models.Model):
    _inherit = "product.product"
    weight_barcode = fields.Boolean(related='product_tmpl_id.weight_barcode', string='Codigo de Barra Balanzas', default=False)



            
