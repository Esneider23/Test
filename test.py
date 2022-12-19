from unittest import TestCase
from stock_controller import stock, delete_stock, vehicle, create_stock, create_vehicle
from app import connection, suma
import json


class TestStock(TestCase):
    info = {
        'name': 'Nivus',
        'motor': ' 200 TSI',
        'gearbox': 'Manual',
        'security': 'ABS, Front Assist',
        'type': 4,
        'url': 'https://awscdn.volkswagen.co/media/Abstract_Image_B960_Component.Content_Model_HighlightFeatureSection_Item_Content_Gallery_Item_Component/47530-1067663-750344-content-gallery-750345-b960/dh-857-e0864f/0fce03af/1657115420/Comf-MT-4.jpg',
        'description': 'Diseño, tecnología, modernidad y potencia. Nivus: una camioneta pensada para emocionar',
        'data_sheet': 'https://awscdn.volkswagen.co/media/Kwc_Basic_DownloadTag_Component/47530-1067658-750328-1141514-816457-linkTag-child/default/09ebc1ce/1668812829/ft-volkswagen-nivus-v2-my22.pdf?_ga=2.163114748.1129427029.1670683187-379648666.1669674914&_gl=1*1ehbr8z*_ga*Mzc5NjQ4NjY2LjE2Njk2NzQ5MTQ.*_ga_41DDCT7V7B*MTY3MDcwMjkzNC40LjEuMTY3MDcwMzc4OC4wLjAuMA..'
    }

    stock_vehicle = {
        'name': '304',
        'supplier': 2,
        "selling_price": 101990000,
        "quantity": 3,
    }

    def test_all_stock(self):
        r = stock(connection())
        result = json.loads(r)
        if 'vehicles' in result:
           info = 'Test passed'
        self.assertEqual(info, 'Test passed')
    
    def test_vehicle(self):
        r = vehicle(connection(), 1)
        result = json.loads(r)
        self.assertEqual(result['vehicle']['name'], 'Voyage')

    def test_create_vehicle(self):
        r = create_vehicle(connection(), TestStock.info)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Vehicle created')

    def test_create_stock(self):
        r = create_stock(connection(), TestStock.stock_vehicle)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Stock created')

    def test_delete_stock(self):
        r = delete_stock(connection(), 144)
        result = json.loads(r)
        self.assertEqual(result['message'], 'Stock deleted')

    def test_suma(self):
        r = suma(1, 2)
        self.assertEqual(r, 3)