# Copyright 2014 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


{
    "name": "Automatic Barcode on Products",
    "version": "15.0.1.0.0",
    "category": "Inventario",
    "author": "Bettaerp - Carlos Pirelli",
    "website": "https://bettaerp.com",
    "license": "AGPL-3",
    "depends": [
        "product",
        "sale",
        "uom",
        "stock"
    ],
    "data": [
      'views/product.xml',
      
      #'views/list_barcode.xml',
    ],
     
    'routes': [
        {'name': 'bettaerp_weight_barcode', 'path': '/home', 'controller': 'bettaerp_weight_barcode.bajatxt'},
    ],
    
    #'odoo': {
    #    'routes': {
    #        '/home': {'controller': 'bettaerp_weight_barcode'},
    #    }
    #},
        
    "demo": [],
    "installable": True,
    
}
