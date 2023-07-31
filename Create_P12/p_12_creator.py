from __future__ import absolute_import, division, print_function

from cryptography.hazmat.primitives.serialization import BestAvailableEncryption, load_pem_private_key, pkcs12
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from endesive.pdf import cms
from cryptography.hazmat import backends
from pathlib import Path
from cryptography.x509 import load_der_x509_certificate
from cryptography.hazmat.primitives.serialization import load_der_private_key
from cryptography.hazmat.primitives.serialization import Encoding
from digital_sign.DateTime.datetime_formatter import DateTimeFormatter
from digital_sign.FormattedDate.formatted_date import FormattedDate
from digital_sign.Create_P12.ca_data import ContactCA
from digital_sign.Create_P12.cert_data import ContactName
from digital_sign.CreateShortcuts.shortcut_creator import shortcut_creator
    

class CreateP12:
    
    _key = None
    _cer_p12 = None     
    
    @classmethod
    def key(cls, key):        
        CreateP12._key = key        
        
    @classmethod
    def cer_p12(cls, cer):
        CreateP12._cer_p12 = cer
        
    @classmethod
    def get_key(cls):
        return CreateP12._key            
    
    @classmethod    
    def get_cer_p12(cls):
        return CreateP12._cer_p12       
    
    def __init__(self, key_path, cer_path, pdf_files, password) -> None:
        self.__key_path = key_path
        self.__cer_path = cer_path
        self.__pdf_files = pdf_files
        self.__password = password
        self.__c_a = None
        self.__cert = None
                  
    
    @property
    def key_path(self):
        return self.__key_path
    
    @key_path.setter
    def key_path(self, path):
        self.__key_path = path
        
    @property
    def cer_path(self):
        return self.__cer_path
    
    @cer_path.setter
    def cer_path(self, path):
        self.__cer_path = path
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password        
        
    @property
    def pdf_files(self):
        return self.__pdf_files
    
    @pdf_files.setter
    def pdf_files(self, pdf_files):
        self.__pdf_files = pdf_files       
        
    @property
    def c_a(self):
        return self.__c_a    
    
    @c_a.setter
    def c_a(self, c_a):
        self.__c_a = c_a
        
    @property
    def cert(self):
        return self.__cert    
    
    @cert.setter
    def cert(self, cert):
        self.__cert = cert   
                                   
    
        
    def key_handler(self):        
        try:            
            key_file = open(self.key_path, 'rb').read()            
            p_key = load_der_private_key(key_file, bytes(self.password, 'utf-8'))            
                        
            CreateP12.key(p_key.private_bytes(
                                        encoding=serialization.Encoding.PEM,
                                        format=serialization.PrivateFormat.PKCS8,
                                        encryption_algorithm=serialization.NoEncryption()
                                    ))                        
        except:
            raise ValueError("Contraseña Incorrecta")
    
    
    
    def cer_handler(self):              
        cer_file = open(self.cer_path, 'rb').read()      
        cer = load_der_x509_certificate(cer_file)
        
        # print(base64.standard_b64encode(cer.fingerprint(hashes.SHA256())))
        #print(cer.issuer._attributes)
        #print(cer.version)
        #print(cer.not_valid_after)
        #print(cer.not_valid_before)
        #print(cer.serial_number)
        #print(cer.signature_algorithm_oid._name)
        #print(base64.standard_b64encode(cer.tbs_certificate_bytes))
        
        ca_cer = cer.public_bytes(encoding=Encoding.PEM)               
        cn = ContactName(x509.load_pem_x509_certificate(ca_cer))
        self.c_a = cn.contact_builder()
        
        _cert = ContactCA(self.c_a.cert)
        self.cert = _cert.contact_ca_builder()
                
        #print(cert.extensions)
        #print(base64.standard_b64encode(cert.signature))
        #print(cert.signature_hash_algorithm.digest_size)        
        #print(cert.serial_number)
        #print(cert.subject.rdns)
        #print(cert.tbs_certificate_bytes)
                
        if CreateP12.get_key() != None:
            key = load_pem_private_key(CreateP12.get_key(), None)
                
            CreateP12.cer_p12(pkcs12.serialize_key_and_certificates(
                        b"friendlyname", 
                        key,
                        self.cert.cert,
                        None,
                        BestAvailableEncryption(b"1234567890")
                    ))
        
        # # Crea la ruta para almacenar las imágenes provenientes de un PDF
        # p = Path(__file__).parent.parent.parent
        # p12 = p.joinpath('Configurations').joinpath('Configs')        
        # # Verifica si no existe la carpeta
        # if not p12.exists():
        #     # Crea la carpeta para almacenar las imágenes
        #     p12.mkdir(exist_ok=False, parents=True)       
        # with open(str(p12.joinpath('certificate.p12')), 'wb') as f:
        #     f.write(CreateP12.get_cer_p12())  
    
    
    def create_dsa(self):        
        # Crea una instancia de la clase Path
        p = Path().cwd().parent        
        # Crea la ruta para almacenar las imágenes provenientes de un PDF
        pdf_signed_folder = p.cwd().parent.joinpath('PDFs Firmados')      
        # Verifica si no existe la carpeta de imágenes
        if not pdf_signed_folder.exists():
            # Crea la carpeta para almacenar las imágenes
            pdf_signed_folder.mkdir(exist_ok=False, parents=True)        
        
        shortcut_creator(str(pdf_signed_folder), str(pdf_signed_folder))
        
        
        _date = FormattedDate
        time = DateTimeFormatter        
        date = f"{_date.formated_date_by_year()}{_date.formated_date_by_month()}{_date.formated_date_by_day()}{time.by_now('hours')}{time.by_now('minutes')}{time.by_now('seconds')}" 
        
        dct = {
            "aligned": 0,
            "sigflags": 3,
            "sigflagsft": 132,
            "sigpage": 0,
            "sigbutton": True,
            "sigfield": self.cert.__str__(),
            "auto_sigfield": True,
            "sigandcertify": True,
            "signaturebox": (0, 0, 150, 150),
            #"signature": "Dokument podpisany cyfrowo ąćęłńóśżź",
            "signature_img": r"..\resources\firma.png",
            "contact": self.c_a.__str__(),
            "location": 'REGISTRO AGRARIO NACIONAL',
            "signingdate": date,
            "reason": f"SE CONTESTA PETICIÓN",
            "password": "",
        }
        p12 = pkcs12.load_key_and_certificates(
                CreateP12.get_cer_p12(), b"1234567890", backends.default_backend()
            )
                     
        for pdf_file in self.pdf_files:           
            datau = open(pdf_file, 'rb').read()        
            datas = cms.sign(datau, dct, p12[0], p12[1], p12[2], "sha256")       
            file_name_splitted = pdf_file.split('/')[-1].split('.')[0]            
            pdf_file_name = str(pdf_signed_folder) + f'\{file_name_splitted} {date}.pdf'
            
            with open(pdf_file_name, "wb") as fp:
                fp.write(datau) 
                fp.write(datas)

        

# if __name__ == '__main__':
#     cd = CreateP12("a", "b", "c", "d")
#     cd.create_dsa()