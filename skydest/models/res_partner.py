
from odoo import fields, models,api,_

class PortalUser(models.Model):
    _inherit = "res.partner"


    experience = fields.Selection([('0','0-1'),('1','1-2'),('2','2-3'),('3','3-4'),('4','4-5'),('5','5+')],string='Experience')
    education = fields.Selection([('school','School'),('higher_secondary','Higher Secondary'),('diploma','Diploma'),('degree','Degree'),('post_graduate','Post Graduate')],string='Education')
    visa_status=fields.Selection([('student','Student Visa'),('visit','Visit Visa'),('employed','Employment Visa'),('dependent','Depended Visa')],string='Visa Status')
    availability= fields.Selection([('immediate','Immediate'),('30','30 Days'),('60','60 Days'),('90','90 Days')],string='Availability')
    salary_exp = fields.Selection([('no_salary','No Salary'),('1000-2000','1,000 to 2,000'),('2000-3000','2 to 3'),('3000-5000','3 to 5'),('5000-10000','5 to 10'),('10000-15000','10 to 15'),('15000+','15+')],string='Expected Salary')
    nationality = fields.Many2one('res.country',string='Nationality')
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],string='Gender')
    emirate = fields.Selection([
        ('dubai','Dubai'),
        ('sharjah', 'Sharjah'),
        ('ajman', 'Ajman'),
        ('ras_al_kaimah', 'RAK'),
        ('umm_al_quwain', 'UAQ'),
        ('fujairah', 'Fujairah'),
        ('abudhabi', 'Abu Dhabi'),
                ],string='Emirate')
    dob = fields.Date(string='Date of Birth')
    university = fields.Char(string='University')
    course = fields.Char(string='Course of study')
    year_of_study = fields.Char(string='Year of Study')
    intern_role = fields.Selection([('accounts','Accounting or Finance'),('admin','Administration'),('architecture','Architecture'),
                                    ('sales', 'Sales, Marketing and business development'),
                                    ('social', 'Community and Social Services Internships'),
                                    ('consultant', 'Consultant'),
                                    ('customer_service', 'Customer Services and Support'),
                                    ('education', 'Education Internships'),
                                    ('engineering', 'Engineering'),
                                    ('data_analytics', 'Data and Analytics'),
                                    ('animation', 'Design and Animation'),
                                    ('healthcare', 'Healthcare Services'),
                                    ('hr', 'Human Resources'),
                                    ('interior', 'Interior Design'),
                                    ('it', 'IT, Web and Software Development'),
                                    ('legal', 'Legal'),
                                    ('media', 'Media and Communications'),
                                    ('operations', 'Operations'),
                                    ('photography', 'Photography and Videography'),
                                    ('logistics', 'Supply chain and logistics management'),
                                    ('project_management', 'Project Management'),
                                    ('events', 'Promotions and events'),
                                    ('research', 'Research'),
                                    ('journalism', 'Journalism and writing'),
                                    ('other', 'Others'),






                                    ],string='Internship Role')
    other_job_role = fields.Char('Other Job Role')
    description = fields.Text("Cover Letter")
    whatsapp = fields.Char('WhatsApp Number')
    availability_intern = fields.Selection([('immediate','Immediate'),
                                            ('0-3','0-3 Months'),('3-6','3-6 Months'),('6-12','6-12 Months')

                                            ] , string='Intern Availability')
    previous_emp = fields.Char('Previous Employer')
    certification = fields.Char('Certifications')

