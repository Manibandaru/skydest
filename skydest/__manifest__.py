
{
    'name': 'Skydest Recruitment',
    'version': '1.0',
    'website' : 'https://www.sidmectech.com',
    'category': 'Base',
    'summary': 'Badge view for skydest event',
    'description': """

""",
    'author': 'Mani Shankar',
    'depends': ['base','web','hr','hr_recruitment','website_partner','website_hr_recruitment',  'website_mail', 'website_form','website_sale','portal'],
    'data': [

        'views/badge_view.xml',
        'views/website_menu.xml',
        'views/res_partner_view.xml',
        'views/res_partner_portal.xml',


    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
