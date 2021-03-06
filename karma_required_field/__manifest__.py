# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Karma Required Field',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://bit.ly/numigi-com',
    'license': 'LGPL-3',
    'category': 'Karma',
    'summary': 'Score users based on form view fields.',
    'depends': [
        'karma',
        'date_range_field_template',  # TA#7472 TA#7659  needs compute.field.template
    ],
    'data': [
        'data/field_template.xml',
        'views/assets.xml',
        'views/karma_required_field.xml',
        'views/karma_required_field_log.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/required_fields.xml',
    ],
    'installable': True,
}
