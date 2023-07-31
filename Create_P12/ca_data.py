import base64

class ContactCA:
    
    def __init__(self, cert) -> None:
        self.__cert = cert
        self.__nombre = ''
        self.__email = ''
        self.__street_address = ''
        self.__postal_code = ''
        self.__country = '' 
        self.__state_or_province = ''
        self.__locality = ''       
        self.__rfc = ''        
        self.__responsible = ''
        self.__encryption = ''
        self.__signature = ''
        
          
    
    @property
    def cert(self):
        return self.__cert
    
    
    @property
    def nombre(self):
        return self.__nombre
    
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def email(self):
        return self.__email
    
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    
    @property
    def street_address(self):
        return self.__street_address
    
    
    @street_address.setter
    def street_address(self, street_address):
        self.__street_address = street_address
        
        
    @property
    def postal_code(self):
        return self.__postal_code
    
    
    @postal_code.setter
    def postal_code(self, postal_code):
        self.__postal_code = postal_code  
    
    
    @property
    def country(self):
        return self.__country
    
    
    @country.setter
    def country(self, country):
        self.__country = country
        
        
    @property
    def state_or_province(self):
        return self.__state_or_province
    
    
    @state_or_province.setter
    def state_or_province(self, state_or_province):
        self.__state_or_province = state_or_province
        
        
    @property
    def locality(self):
        return self.__locality
    
    
    @locality.setter
    def locality(self, locality):
        self.__locality = locality 
        
        
    @property
    def rfc(self):
        return self.__rfc
    
    
    @rfc.setter
    def rfc(self, rfc):
        self.__rfc = rfc
        
        
    @property
    def responsible(self):
        return self.__responsible
    
    
    @responsible.setter
    def responsible(self, responsible):
        self.__responsible = responsible
        
    
    @property
    def encryption(self):
        return self.__encryption
    
    
    @encryption.setter
    def encryption(self, encryption):
        self.__encryption = encryption 
    
    
    @property
    def signature(self):
        return self.__signature
    
    
    @signature.setter
    def signature(self, signature):
        self.__signature = signature    
        
        
    def contact_ca_builder(self):
        for certificado in self.cert.issuer:            
            if certificado.oid._name == 'organizationName':
                self.nombre = certificado.value
                    
            if certificado.oid._name == 'emailAddress':
                self.email = certificado.value
                
            if certificado.oid._name == 'streetAddress':
                self.street_address = certificado.value     
            
            if certificado.oid._name == 'postalCode':
                self.postal_code = certificado.value
            
            if certificado.oid._name == 'countryName':
                self.country = certificado.value         
            
            if certificado.oid._name == 'stateOrProvinceName':
                self.state_or_province = certificado.value
                
            if certificado.oid._name == 'localityName':
                self.locality = certificado.value 
                
            if certificado.oid._name == 'x500UniqueIdentifier':
                self.rfc = certificado.value
            
            if certificado.oid._name == 'unstructuredName':
                self.responsible = certificado.value
                
        self.encryption = self.cert.signature_algorithm_oid._name
        self.signature = base64.b64encode(self.cert.signature)        
        
        return self                     


    def __str__(self):
        return f'DATOS DE LA AUTORIDAD CERTIFICADORA:\n Nombre: {self.nombre}\n Correo: {self.email}\n Calle: {self.street_address}\n Código Postal: {self.postal_code}\n País: {self.country}\n Estado o Provincia: {self.state_or_province}\n Localidad: {self.locality}\n RFC: {self.rfc}\n Unidad {self.responsible}\n Encriptación: {self.encryption}\n Firma Digital: {self.signature}'
