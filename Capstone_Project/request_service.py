import requests

url = "http://localhost:1552/predict"
laptop_details = {'company': 'dell',
                 'product': 'xps_13',
                 'type_name': 'ultrabook',
                 'inches': 13.3,
                 'cpu': 'intel_core_i7_7560u_2.4ghz',
                 'ram_in_gb': 8,
                 'gpu': 'intel_iris_plus_graphics_640',
                 'op_sys': 'windows_10',
                 'weight_in_kg': 1.23,
                 'y_res': '1080',
                 'x_res': 1920,
                 'touch_screen': 0,
                 'screen_resolution_type': 'full_hd',
                 'processor': 'intel_core_i7_7560u',
                 'clock_speed_ghz': '2.4',
                 'hard_disk_type': 'ssd',
                 'memory_gb': 256}
resp = requests.post(url, json=laptop_details).json()
print(resp)
