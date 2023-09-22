from odoo import http
from werkzeug.wrappers import Response
from odoo.exceptions import  ValidationError

import logging
_logger = logging.getLogger(__name__)


class bettaerp_weight_barcode(http.Controller):
        
    @http.route('/home', type='http', auth='public')
    def download_txt(self):
        
        regis_1=''
        divisortxt = "|"
        
        product_templ = http.request.env['product.template'].sudo().search([('weight_barcode','=',True),('expiration_time','!=','0')])
        #FIXME Deberia ver esto para que no grabe un registro en blanco
        for rec in product_templ:
            produ = str((rec.id)).zfill(5)
            produ_cero = (str(rec.id)+'0').zfill(5)
            _logger.warning(rec.use_expiration_date)
            
            _logger.warning(rec.tracking)
            #if rec.tracking == 'lot' :
            if rec.use_expiration_date and rec.tracking == 'lot' :
                    regis = produ + divisortxt + produ_cero + divisortxt + rec.name + divisortxt + str(rec.list_price) + divisortxt + str(rec.pesable) + divisortxt + str(rec.expiration_time) + divisortxt + str(rec.categ_id.id) + divisortxt + str(rec.tara) + divisortxt+ str(rec.marca) + divisortxt + str(rec.tipo_vencimiento)
                    regis_1 +=  regis + "\n"
           
                    _logger.warning(regis)
                
            #    else :
            #        valor = 'El producto '+' '+ rec.name + ' '+ 'no tiene fecha de vencimiento corrija antes de continuar.'        
            #        raise ValidationError(valor)    
            #else:
            #    valor = 'Productos sin fecha de expiracion ...'        
            #    raise ValidationError(valor)
                

            
        _logger.warning(regis_1)
        
        
        return http.request.make_response(
                regis_1, headers=[
                      ('Content-Disposition', 'attachment; filename="balanza.txt"'),
                     ('Content-Type', 'text/plain')
                     ])