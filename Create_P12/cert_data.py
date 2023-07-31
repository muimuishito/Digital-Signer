

class ContactName:
    
    def __init__(self, cert) -> None:
        self.__cert = cert
        self.__nombre = ''
        self.__country = ''
        self.__email = ''
        self.__rfc = ''
        self.__curp = ''   
    
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
    def country(self):
        return self.__country
    
    
    @country.setter
    def country(self, country):
        self.__country = country
        
    
    @property
    def email(self):
        return self.__email
    
    
    @email.setter
    def email(self, email):
        self.__email = email
        
        
    @property
    def rfc(self):
        return self.__rfc
    
    
    @rfc.setter
    def rfc(self, rfc):
        self.__rfc = rfc
        
        
    @property
    def curp(self):
        return self.__curp
    
    
    @curp.setter
    def curp(self, curp):
        self.__curp = curp
        
        
    def contact_builder(self):
        for certificado in self.cert.subject.rdns:            
            if certificado._attributes[0].oid._name == 'commonName':
                self.nombre = certificado._attributes[-1].value
                    
            if certificado._attributes[0].oid._name == 'countryName':
                self.country = certificado._attributes[-1].value
                    
            if certificado._attributes[0].oid._name == 'emailAddress':
                self.email = certificado._attributes[-1].value 
                
            if certificado._attributes[0].oid._name == 'x500UniqueIdentifier':
                self.rfc = certificado._attributes[-1].value
            
            if certificado._attributes[0].oid._name == 'serialNumber':
                self.curp = certificado._attributes[-1].value
        
        return self                     


    def __str__(self):
        return f'DATOS DEL FIRMANTE:\n Nombre:{self.nombre}\n Pais:{self.country}\n Correo:{self.email}\n RFC:{self.rfc}\n CURP:{self.curp}'
    