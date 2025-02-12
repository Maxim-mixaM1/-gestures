import yaml

data_yaml_path = 'dt/data21.yaml'
data = {
  'train': "C:/PycharmProjects/pythonProject1/dt/train",
  'val': "C:/PycharmProjects/pythonProject1/dt/valid",
  'test': "CC:/PycharmProjects/pythonProject1/dt/test",
  'nc': 2,
  'names': ['hand', 'left_click']
}
with open(data_yaml_path, 'w') as f:
  yaml.dump(data, f, default_flow_style=None, sort_keys=False)
print(f"Updated {data_yaml_path}")