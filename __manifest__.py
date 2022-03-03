# -*- coding: utf-8 -*-
{
    'name': "restaurante",

    'summary': """Modulo de platos y menus""",

    'description': """
        Módulo para manejar:
        -platos
        -menus
    """,

    'author': "Miriam Gutierrez",
    'website': "https://www.linkedin.com/feed/?legoTrackingToken=c34ZpnFFkTBxr71PqmgCc2UMfmlOrSdjtOoZsC5gr6litOoZp6Zdr6litOoVejAVejRApnhPpnlNpl9JtmUCjAZ9l4BjjR0Zuk9OpmhOjThBpShFtOpHsCZTnSZQnSVBs6ZvcDpAon1EoSVRomMZp4BQpmtAqnsCcjRKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoVejAVejRApnhPpnlNpl9JtkVMtmZOpOpPrCZFt6dxfmh9s7lLsCsCjAZ9l4BjjR0Zuk9OpmhOrOpQr7lxpClAfmh9t6VBrmtBsOpPoCZGfmh9t6ZIsOpQr7lxpClAfmh9t7lLum5I9z9Sp65Mq6dKtm5IfmlJokVBpS5M9CxQtSZOpPRAin1MoioSdzoVe3RAimVLqndOpnoCcj0Rcj8UcPAPfmh9tioSczkVoP5yojkQejAJpz0TeiRzojsQbjgQdPwJc6oSpmcPpmoZp4BQu6lQrCZz&trk=opento_lp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/plato.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
