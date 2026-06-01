import os
import json
from pages.pim_page import PimPage
from playwright.sync_api import expect
import random

#Cargar datos json
DATA_DIR = os.path.abspath("./data")
with open(os.path.join(DATA_DIR, 'employee_data.json')) as f:
    EMPLOYEE_DATA = json.load(f)

def test_alta_empleado(page_autenticada):
    id_dinamico = str(random.randint(100000,999999))
    pim = PimPage(page_autenticada)
    pim.alta_nuevo_empleado(EMPLOYEE_DATA['alta_empleado'],id_dinamico)
    toast = pim.validar_toast_positivo()
    #Validación de texto flexible, se usa to_have_text si se desea que el texto del elemento sea exactamente igual
    expect(toast).to_contain_text("Successfully Saved") 
    expect(toast).to_be_hidden() #Limpiamos la pantalla (esperamos a que el Toast desaparezca)
    pim.complementar_personal_details(EMPLOYEE_DATA['personal_details'])
    expect(toast).to_contain_text("Successfully Updated") 
    expect(toast).to_be_hidden()
    pim.completar_custom_fields(EMPLOYEE_DATA['custom_fields'])
    expect(toast).to_contain_text("Successfully Saved") 
    expect(toast).to_be_hidden()
    pim.subir_archivo_empleado()
    expect(toast).to_contain_text("Successfully Saved") 
    expect(toast).to_be_hidden()
    pim.llenar_contact_details(EMPLOYEE_DATA['contact_details'])
    expect(toast).to_contain_text("Successfully Updated") 
    expect(toast).to_be_hidden()
    pim.subir_archivo_contacto_empleado()
    expect(toast).to_contain_text("Successfully Saved") 
    expect(toast).to_be_hidden()
    pim.agregar_contactos_emergencia(EMPLOYEE_DATA['emergency_contacts'])



# ====================================================================
    # 3. EL FUTURO: LA BÚSQUEDA
    # Como la variable `id_dinamico` vive en esta función, ahora puedes 
    # usarla directamente para continuar tu flujo. Por ejemplo:
    # 
    # pim.ir_a_lista_de_empleados()
    # pim.buscar_por_id(id_dinamico)
    # expect(pim.obtener_resultado_tabla()).to_contain_text(id_dinamico)
    # ====================================================================