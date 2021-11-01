import requests

url = "http://localhost:1552/predict"
mushroom_data = {'cap_shape': 1.0, 'cap_surface': 1.0, 'cap_color': 1.0, 'bruises': 0.0, 'odor': 1.0, 'gill_attachment': 1.0, 'gill_spacing': 0.0, 'gill_size': 1.0, 'gill_color': 0.0, 'stalk_shape': 1.0, 'stalk_root': 0.0,
            'stalk_surface_above_ring': 1.0, 'stalk_surface_below_ring': 1.0, 'stalk_color_above_ring': 0.0, 'stalk_color_below_ring': 7.0, 'veil_color': 2.0, 'ring_number': 1.0, 'ring_type': 0.0, 'spore_print_color': 2.0, 'population': 4.0, 'habitat': 2.0}
resp = requests.post(url, json=mushroom_data).json()
print(resp)
