import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-intrastat-extrastat",
    description="Meta package for sygel-technology-sy-intrastat-extrastat Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-product_harmonized_system_country>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
