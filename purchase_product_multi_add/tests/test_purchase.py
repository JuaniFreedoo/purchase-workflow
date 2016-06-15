# -*- coding: utf-8 -*-
# © 2016  Denis Roussel, Acsone SA/NV (http://www.acsone.eu)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import openerp.tests.common as common
import re


class TestPurchase(common.TransactionCase):

    def setUp(self):
        common.TransactionCase.setUp(self)

        self.product_35 = self.env.ref("product.product_product_35")
        self.product_36 = self.env.ref("product.product_product_36")
        self.supplier = self.env.ref("base.res_partner_8")

    def test_import_product(self):
        """ Create PO
            Import products
            Check products are presents
        """

        po = self.env["purchase.order"].create(
            {"partner_id": self.supplier.id,
             'location_id': self.env.ref("stock.stock_location_stock").id,
             'pricelist_id': self.env.ref('purchase.list0').id})

        wiz_obj = self.env['purchase.import.products']
        wizard = wiz_obj.with_context(active_id=po.id,
                                      active_model='purchase.order')

        products = [(6, 0, [self.product_35.id, self.product_36.id])]

        wizard_id = wizard.create({'products': products,
                                   'quantity': 5.0})

        wizard_id.select_products()

        self.assertEqual(len(po.order_line), 2)

        for line in po.order_line:
            self.assertEqual(line.product_qty, 5.0)

    def test_import_product_no_quantity(self):
        """ Create PO
            Import products with no quantity
            Check products are presents
        """

        po = self.env["purchase.order"].create(
            {"partner_id": self.supplier.id,
             'location_id': self.env.ref("stock.stock_location_stock").id,
             'pricelist_id': self.env.ref('purchase.list0').id})

        wiz_obj = self.env['purchase.import.products']
        wizard = wiz_obj.with_context(active_id=po.id,
                                      active_model='purchase.order')

        products = [(6, 0, [self.product_35.id, self.product_36.id])]

        wizard_id = wizard.create({'products': products})

        wizard_id.select_products()

        self.assertEqual(len(po.order_line), 2)

        for line in po.order_line:
            self.assertEqual(line.product_qty, 1.0)

    def test_import_product_fields_view(self):
        """ Check if domain is well affected
        """

        po = self.env["purchase.order"].create(
            {"partner_id": self.supplier.id,
             'location_id': self.env.ref("stock.stock_location_stock").id,
             'pricelist_id': self.env.ref('purchase.list0').id})

        wiz_obj = self.env['purchase.import.products']
        wizard = wiz_obj.with_context(active_id=po.id,
                                      active_model='purchase.order')

        res = wizard.fields_view_get()
        self.assertEqual('arch' in res, True)
        match = re.compile(r'<field(.)+domain=(.)+&quot;seller_ids.name')
        find_res = re.findall(match,
                              res['arch'])
        self.assertEqual(len(find_res) > 0, True)
