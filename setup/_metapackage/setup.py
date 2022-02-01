import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-purchase-workflow",
    description="Meta package for oca-purchase-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-procurement_purchase_no_grouping',
        'odoo13-addon-procurement_purchase_sale_no_grouping',
        'odoo13-addon-product_form_purchase_link',
        'odoo13-addon-product_supplierinfo_qty_multiplier',
        'odoo13-addon-purchase_all_shipments',
        'odoo13-addon-purchase_allowed_product',
        'odoo13-addon-purchase_blanket_order',
        'odoo13-addon-purchase_commercial_partner',
        'odoo13-addon-purchase_delivery_split_date',
        'odoo13-addon-purchase_deposit',
        'odoo13-addon-purchase_discount',
        'odoo13-addon-purchase_exception',
        'odoo13-addon-purchase_force_invoiced',
        'odoo13-addon-purchase_invoice_plan',
        'odoo13-addon-purchase_isolated_rfq',
        'odoo13-addon-purchase_landed_cost',
        'odoo13-addon-purchase_last_price_info',
        'odoo13-addon-purchase_line_procurement_group',
        'odoo13-addon-purchase_location_by_line',
        'odoo13-addon-purchase_manual_currency',
        'odoo13-addon-purchase_minimum_amount',
        'odoo13-addon-purchase_open_qty',
        'odoo13-addon-purchase_order_approval_block',
        'odoo13-addon-purchase_order_approved',
        'odoo13-addon-purchase_order_archive',
        'odoo13-addon-purchase_order_line_deep_sort',
        'odoo13-addon-purchase_order_line_menu',
        'odoo13-addon-purchase_order_line_packaging_qty',
        'odoo13-addon-purchase_order_line_price_history',
        'odoo13-addon-purchase_order_line_price_history_discount',
        'odoo13-addon-purchase_order_line_stock_available',
        'odoo13-addon-purchase_order_product_recommendation',
        'odoo13-addon-purchase_order_product_recommendation_brand',
        'odoo13-addon-purchase_order_product_recommendation_xlsx',
        'odoo13-addon-purchase_order_qty_change_no_recompute',
        'odoo13-addon-purchase_order_secondary_unit',
        'odoo13-addon-purchase_order_supplierinfo_update',
        'odoo13-addon-purchase_order_type',
        'odoo13-addon-purchase_order_type_dashboard',
        'odoo13-addon-purchase_order_uninvoiced_amount',
        'odoo13-addon-purchase_partner_selectable_option',
        'odoo13-addon-purchase_product_usage',
        'odoo13-addon-purchase_propagate_qty',
        'odoo13-addon-purchase_reception_notify',
        'odoo13-addon-purchase_reception_status',
        'odoo13-addon-purchase_representative',
        'odoo13-addon-purchase_request',
        'odoo13-addon-purchase_request_department',
        'odoo13-addon-purchase_request_order_approved',
        'odoo13-addon-purchase_request_tier_validation',
        'odoo13-addon-purchase_requisition_grouped_by_procurement',
        'odoo13-addon-purchase_requisition_tier_validation',
        'odoo13-addon-purchase_security',
        'odoo13-addon-purchase_stock_picking_show_currency_rate',
        'odoo13-addon-purchase_stock_price_unit_sync',
        'odoo13-addon-purchase_stock_secondary_unit',
        'odoo13-addon-purchase_substate',
        'odoo13-addon-purchase_tier_validation',
        'odoo13-addon-purchase_tier_validation_forward',
        'odoo13-addon-purchase_warn_message',
        'odoo13-addon-purchase_work_acceptance',
        'odoo13-addon-supplier_calendar',
        'odoo13-addon-vendor_transport_lead_time',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
