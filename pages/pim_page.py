from pages.base_page import BasePage
from playwright.sync_api import expect


class PimPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        #Locators
        self.pim_menu = page.get_by_role("link",name="PIM")
        self.btn_add_new_employee = page.get_by_role("button", name="Add")
        # En vez de XPaths o Names, buscamos por el placeholder gris de las cajas
        self.nombre_empleado = page.get_by_placeholder("First Name")
        self.apellido_paterno_empleado = page.get_by_placeholder("Middle Name")
        self.apellido_materno_empleado = page.get_by_placeholder("Last Name")
        self.id_empleado = page.get_by_role("textbox").nth(4)
        self.input_foto = page.locator("input[type='file']")
        self.btn_primer_save_empleado = page.get_by_role("button", name="Save")
        self.toast_success_alta_nuevo_empleado = page.locator(".oxd-toast-content p:last-child")
        self.num_licencia_empleado = page.locator("//label[text()=\"Driver's License Number\"]/parent::div/following-sibling::div/input")
        self.expiracion_licencia = page.locator("//label[text() ='License Expiry Date']/parent::div/following-sibling::div//input")
        self.dropdown_nacionalidad = page.locator("//label[text() = 'Nationality']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
        self.estado_civil = page.locator("//label[text() = 'Marital Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
        self.fecha_nacimiento = page.locator("//label[text() ='Date of Birth']/parent::div/following-sibling::div//input")
        self.genero_masculino = page.get_by_text("Male",exact = True)
        self.genero_femenino=page.get_by_text("Female",exact = True)
        self.btn_personal_details = page.locator("(//button[@type='submit'][normalize-space()='Save'])[1]")
        self.dropdown_tipo_sangre = page.locator("//label[text() = 'Blood Type']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
        self.btn_save_customfields = page.locator("(//button[@type='submit'][normalize-space()='Save'])[2]")
        self.btn_add_attachment = page.get_by_role("button", name = "Add")
        self.btn_save_attachment_employe = page.locator("(//button[@type='submit'][normalize-space()='Save'])[3]")
        #Locators contact details
        self.menu_contact_details = page.get_by_role("link", name ="Contact Details")
        self.calle_uno = page.locator("//label[text()= 'Street 1']/parent::div/following-sibling::div/input")
        self.calle_dos = page.locator("//label[text()= 'Street 2']/parent::div/following-sibling::div/input")
        self.ciudad = page.locator("//label[text()= 'City']/parent::div/following-sibling::div/input")
        self.ciudad_provincia = page.locator ("//label[text()= 'State/Province']/parent::div/following-sibling::div/input")
        self.codigo_postal = page.locator ("//label[text()= 'Zip/Postal Code']/parent::div/following-sibling::div/input")
        self.pais = page.locator("//label[text()= 'Country']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
        self.telefono_fijo = page.locator("//label[text()= 'Home']/parent::div/following-sibling::div/input")
        self.telefono_movil = page.locator("//label[text()= 'Mobile']/parent::div/following-sibling::div/input")
        self.telefono_trabajo = page.locator("//label[text()= 'Work']/parent::div/following-sibling::div/input")
        self.correo_trabajo = page.locator("//label[text()= 'Work Email']/parent::div/following-sibling::div/input")
        self.otro_correo = page.locator("//label[text()= 'Other Email']/parent::div/following-sibling::div/input")
        self.btn_save_contact_details = page.locator("(//button[@type='submit'][normalize-space()='Save'])[1]")
        self.btn_save_attachment_contact_details = page.locator ("(//button[@type='submit'][normalize-space()='Save'])[2]")
        #Locators emergency contacts
        self.tab_emergency_contacts = page.get_by_role("link", name="Emergency Contacts")
        self.add_emergency_contact = page.locator("(//button[@type='button'][normalize-space()='Add'])[1]")
        self.nombre_contacto_emergencia = page.locator("//label[text() = 'Name']/parent::div/following-sibling::div/input")
        self.parentezco_contacto_emergencia = page.locator("//label[text() = 'Relationship']/parent::div/following-sibling::div/input")
        self.telefono_casa_emergencia = page.locator("//label[text() = 'Home Telephone']/parent::div/following-sibling::div/input")
        self.telefono_movil_emergencia = page.locator("//label[text() = 'Mobile']/parent::div/following-sibling::div/input")
        self.btn_save_emergency_contact = page.locator("(//button[@type='submit'][normalize-space()='Save'])")
        self.btn_add_attachment_emergency_contact = page.locator("(//button[@type='button'][normalize-space()='Add'])[2]")
        self.btn_save_attachment_emergency_contact = page.locator("(//button[@type='submit'][normalize-space()='Save'])")
        #Locators dependents
        self.tab_dependents = page.get_by_role("link", name="Dependents")
        self.btn_add_dependent = page.locator("(//button[@type='button'][normalize-space()='Add'])[1]")
        self.nombre_dependiente = page.locator("//label[text()='Name']/parent::div/following-sibling::div/input")
        self.dropdonwn_parentezco_dependiente = page.locator("//label[text() = 'Relationship']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
        self.especificar_parentezco = page.locator("//label[text() = 'Please Specify']/parent::div/following-sibling::div/input")
        self.fecha_nacimiento_dependiente = page.locator("//label[text() = 'Date of Birth']/parent::div/following-sibling::div//input")
        self.btn_save_dependiente = page.locator("(//button[@type='submit'][normalize-space()='Save'])")
        self.btn_add_attachment_dependiente = page.locator("(//button[@type='button'][normalize-space()='Add'])[2]")
        self.btn_save_attachment_dependiente = page.locator("(//button[@type='submit'][normalize-space()='Save'])")




    def alta_nuevo_empleado(self,data, id_empleado):
        self.hacer_click(self.pim_menu)
        self.hacer_click(self.btn_add_new_employee)
        self.escribir_texto(self.nombre_empleado,data['first_name'])
        self.escribir_texto(self.apellido_paterno_empleado,data['middle_name'])
        self.escribir_texto(self.apellido_materno_empleado,data['last_name'])
        self.id_empleado.clear()
        self.escribir_texto(self.id_empleado,id_empleado)
        #Subir la foto del empleado
        self.subir_archivo(data['ruta_foto'],self.input_foto)
        self.hacer_click(self.btn_primer_save_empleado)
    def validar_toast_positivo(self):
        return self.toast_success_alta_nuevo_empleado
     
    def complementar_personal_details(self,data):
        self.escribir_texto(self.num_licencia_empleado,data['license_number'])
        self.escribir_texto(self.expiracion_licencia,data['license_exp'])
        opcion_nacionalidad = self.page.get_by_role("option", name = data['nationality'], exact=True ) # extact = True Valida la opción exacta descrita en el json
        self.llenar_dropdown(self.dropdown_nacionalidad,opcion_nacionalidad)
        opcion_estado_civil = self.page.get_by_role("option",name= data['marital_status'], exact = True)
        self.llenar_dropdown(self.estado_civil,opcion_estado_civil)
        self.escribir_texto(self.fecha_nacimiento,data['date_of_birth'])
        self.seleccionar_radiobutton(self.genero_masculino,self.genero_femenino)
        self.hacer_click(self.btn_personal_details)

    def completar_custom_fields(self,data):
        opcion_tipo_sangre = self.page.get_by_role("option", name= data['blood_type'], exact = True)
        self.llenar_dropdown(self.dropdown_tipo_sangre,opcion_tipo_sangre)
        self.hacer_click(self.btn_save_customfields)
    def subir_archivo_empleado(self,data):
        self.hacer_click(self.btn_add_attachment)
        self.subir_archivo(data['ruta_archivos'],self.input_foto)
        self.hacer_click(self.btn_save_attachment_employe)

    def llenar_contact_details(self,data):
        self.hacer_click(self.menu_contact_details)
        self.escribir_texto(self.calle_uno,data['street1'])
        self.escribir_texto(self.calle_dos,data['street2'])
        self.escribir_texto(self.ciudad,data['city'])
        self.escribir_texto(self.ciudad_provincia,data['state'])
        self.escribir_texto(self.codigo_postal,data['zip_code'])
        opcion_pais = self.page.get_by_role("option", name = data['country'], exact = True)
        self.llenar_dropdown(self.pais,opcion_pais)
        self.escribir_texto(self.telefono_fijo,data['home_phone'])
        self.escribir_texto(self.telefono_movil,data['mobile'])
        self.escribir_texto(self.telefono_trabajo,data['work_phone'])
        self.generar_correo_aleatorio(self.correo_trabajo)
        self.generar_correo_aleatorio(self.otro_correo)
        self.hacer_click(self.btn_save_contact_details)

    def subir_archivo_contacto_empleado(self,data):
        self.page.pause()
        self.hacer_click(self.btn_add_attachment)
        self.subir_archivo(data['archivo_contacto_empleado'],self.input_foto)
        self.hacer_click(self.btn_save_attachment_contact_details)

    def ir_contactos_emergencia(self):
        self.hacer_click(self.tab_emergency_contacts)

    def llenar_concatos_emergencia(self, contactos):
        self.hacer_click(self.add_emergency_contact)
        self.escribir_texto(self.nombre_contacto_emergencia,contactos['name'])
        self.escribir_texto(self.parentezco_contacto_emergencia,contactos['relationship'])
        self.escribir_texto(self.telefono_casa_emergencia,contactos['home_phone'])
        self.escribir_texto(self.telefono_movil_emergencia,contactos['mobile_phone'])
        

    def subir_archivos_contactos_emergencia(self,data):
        self.hacer_click(self.btn_add_attachment_emergency_contact)
        self.subir_archivo(data['ruta_archivo_contacto_emergencia'],self.input_foto)
        self.hacer_click(self.btn_save_attachment_emergency_contact)

    def ir_dependientes(self):
        self.hacer_click(self.tab_dependents)

    def agregar_dependientes(self, dependientes):
        self.hacer_click(self.btn_add_dependent)
        self.escribir_texto(self.nombre_dependiente,dependientes['name'])
        opcion_parentezco = self.page.get_by_role("option", name = dependientes['relationship'], exact = True)
        self.llenar_dropdown(self.dropdonwn_parentezco_dependiente,opcion_parentezco)
        if dependientes['relationship'] == 'Other':
            self.escribir_texto(self.especificar_parentezco,dependientes['specific_relationship'])
        self.escribir_texto(self.fecha_nacimiento_dependiente,dependientes['date_of_birth'])
        self.hacer_click(self.btn_save_dependiente)

            
            
            

            
            


    

        






















