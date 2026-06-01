import json
import os

USUARIOS = [
    ("Admin","admin123")
]

# Cargar datos de empleado desde JSON
DATA_DIR = os.path.dirname(__file__)
EMPLOYEE_DATA_PATH = os.path.join(DATA_DIR, 'employee_data.json')

with open(EMPLOYEE_DATA_PATH, 'r') as f:
    EMPLOYEE_DATA = json.load(f)