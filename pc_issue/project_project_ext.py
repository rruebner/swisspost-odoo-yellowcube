# b-*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2015 brain-tec AG (http://www.brain-tec.ch)
#    All Right Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv, fields
from openerp.tools.translate import _
import logging
logger = logging.getLogger(__name__)


class project_project_ext(osv.Model):
    _inherit = 'project.project'

    _columns = {
        'categ_id': fields.many2one('project.category', string='Issues category', help='Associated category for automated creation of issues', required=False),
        'categ_ids': fields.one2many('project.category', 'project_id', string='Issues category', help='Associated category for automated creation of issues', required=False)
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
