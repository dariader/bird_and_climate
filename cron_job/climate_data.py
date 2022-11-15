import requests as re
import os
# https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-sea-level-global?tab=form
#uid and apikey in ~/.cdsapirc
#https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-sea-level-global?tab=overview
# it is required to sign agreement here https://cds.climate.copernicus.eu/cdsapp/#!/terms/licence-to-use-copernicus-products
# documentation
#https://datastore.copernicus-climate.eu/documents/satellite-sea-level/vDT2021/D3.SL.1-v2.0_PUGS_of_v2DT2021_SeaLevel_products_v1.1_APPROVED_Ver1.pdf


import cdsapi
c = cdsapi.Client()
c.retrieve(
    'satellite-sea-level-global',
    {
        'version': 'vDT2021',
        'variable': 'all',
        'format': 'tgz',
        'year': [
            '1993', '1994', '1995',
            '1996', '1997', '1998',
            '1999', '2000', '2001',
            '2002', '2003', '2004',
            '2005', '2006', '2007',
            '2008', '2009', '2010',
            '2011', '2012', '2013',
            '2014', '2015', '2016',
            '2017', '2018', '2019',
            '2020', '2021', '2022',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': '15',
    },
    'satellite-sea-level-global.tar.gz')