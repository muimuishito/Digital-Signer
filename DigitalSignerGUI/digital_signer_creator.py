from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QPushButton, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout
from PySide6 import QtGui
from PySide6 import QtCore
from digital_sign.Create_P12.p_12_creator import CreateP12 

import sys


class WidgetWindow(QWidget):
    
    def __init__(self):        
        super().__init__()            
        self.setWindowTitle("Firma Electrónica")
        self.setFixedSize(300, 200)
        self.setWindowIcon(QtGui.QIcon(r"..\resources\ran.ico"))
        self.widgets_creator()
        self.__key_file_name = ''
        self.__cer_file_name = ''
        self.__pdf_file_name = ''
        self.__password = ''        
        
        
    @property
    def key_file_name(self):
        return self.__key_file_name
    
    
    @key_file_name.setter
    def key_file_name(self, file_name):
        self.__key_file_name = file_name
        
        
    @property
    def cer_file_name(self):
        return self.__cer_file_name
    
    
    @cer_file_name.setter
    def cer_file_name(self, file_name):
        self.__cer_file_name = file_name
        
    @property
    def password(self):
        return self.__password
    
    
    @password.setter
    def password(self, password):
        self.__password = password
        
        
    @property
    def sel_pdf_file_name(self):
        return self.__pdf_file_name
    
    
    @sel_pdf_file_name.setter
    def sel_pdf_file_name(self, pdf_file):
        self.__pdf_file_name = pdf_file              
        
                
    def widgets_creator(self):
        private_key_lb = QLabel("Llave Privada (.key)")
        self.private_key_btn = QPushButton("Seleccionar archivo .key")
        self.private_key_btn.setFixedSize(140, 25)
        self.private_key_btn.clicked.connect(self.sel_key_file)                  
        
        h_l_1 = QHBoxLayout()
        h_l_1.addWidget(private_key_lb)
        h_l_1.addWidget(self.private_key_btn)
        
        cer_lb = QLabel("Certificado (.cer)")
        self.cer_btn = QPushButton("Seleccionar archivo .cer")
        self.cer_btn.setFixedSize(140, 25)
        self.cer_btn.clicked.connect(self.sel_cer_file)           
        
        h_l_2 = QHBoxLayout()
        h_l_2.addWidget(cer_lb)
        h_l_2.addWidget(self.cer_btn)               
        
        pdf_files_lb = QLabel("Archivos Para Firmar")
        self.pdf_files_btn = QPushButton("Seleccionar PDF's")
        self.pdf_files_btn.setFixedSize(140, 25)
        self.pdf_files_btn.clicked.connect(self.sel_pdf_files)         
        
        h_l_3 = QHBoxLayout()
        h_l_3.addWidget(pdf_files_lb)
        h_l_3.addWidget(self.pdf_files_btn)
        
        password_lb = QLabel("Contraseña")
        self.password_le = QLineEdit()
        self.password_le.setFixedSize(200, 25)
        self.password_le.setEchoMode(QLineEdit.Password)
        # self.password_le.installEventFilter(self)
                
        h_l_4 = QHBoxLayout()
        h_l_4.addWidget(password_lb)
        h_l_4.addWidget(self.password_le)        
        
        self.generar_btn = QPushButton("Generar Firma Electrónica")
        self.generar_btn.clicked.connect(self.digital_sign_generator)        
        
        v_l = QVBoxLayout()
        v_l.addLayout(h_l_1)
        v_l.addLayout(h_l_2)
        v_l.addLayout(h_l_3)
        v_l.addLayout(h_l_4)
        v_l.addWidget(self.generar_btn)       
        
        self.setLayout(v_l)
    
    
    # def eventFilter(self, obj, event):
    #     if self.password_le is obj and event.type() == QtCore.QEvent.KeyPress:
    #         if event.matches(QtGui.QKeySequence.Copy) or event.matches(
    #             QtGui.QKeySequence.Paste
    #         ):
    #         # or
    #         # if event in (QtGui.QKeySequence.Copy, QtGui.QKeySequence.Paste):
    #             return True
    #     return super().eventFilter(obj, event)
    
        
    
    def sel_key_file(self):       
        fileName = QFileDialog.getOpenFileName(self, ("Abrir Archivo"), "Clave privada", ("Archivo .key (*.key)"))
        
        if fileName[0] != '':            
            self.key_file_name = fileName[0]                     
        else:
            self. multiple_data_message("Error al cargar el archivo", "No se pudo cargar el archivo")
    
       
    
    def sel_cer_file(self):
        fileName = QFileDialog.getOpenFileName(self, ("Abrir Archivo"), "Certificado", ("Archivo .cer (*.cer)"))       
        
        if fileName[0] != '':
            self.cer_file_name = fileName[0]            
        else:
            self. multiple_data_message("Error al cargar el archivo", "No se pudo cargar el archivo")
            
            
    def sel_pdf_files(self):
        fileName = QFileDialog.getOpenFileNames(self, ("Abrir Archivo"), "PDF", ("Archivo .pdf (*.pdf)"))       
       
        if fileName[0] != '':
            self.sel_pdf_file_name = fileName[0]            
        else:
            self. multiple_data_message("Error al cargar el archivo", "No se pudo cargar el archivo")        
        
     
    def check_password(self):
        self.password = self.password_le.text().strip()
        return self.password
    
    
    def digital_sign_generator(self):        
        if self.key_file_name == '':
            self.multiple_data_message("Error en Archivo .key", "Seleccione archivo .key")
        elif self.cer_file_name == '':
            self.multiple_data_message("Error en Archivo .cer", "Seleccione archivo .cer")        
        elif self.sel_pdf_file_name == '' or self.sel_pdf_file_name == []:
            self.multiple_data_message("Error en Archivos PDF", "Seleccione archivos .pdf")
        elif self.check_password() == '':
            self.multiple_data_message("Error en Contraseña", "Ingrese su Contraseña")
        else:            
            p12 = CreateP12(self.key_file_name, self.cer_file_name, self.sel_pdf_file_name, self.password.strip())
            try:                
                p12.key_handler()
                p12.cer_handler()                       
                p12.create_dsa()
                
                while(True):            
                    if self.generar_btn.isEnabled():
                        self.multiple_data_message("Finalizado Correctamente", "La Firma Electrónica Se Creo Correctamente")
                        break          
            except:
                self.multiple_data_message("Error en contraseña", "Contraseña Incorrecta")                      
            
                
    
    def multiple_data_message(self, window_title="", message=""):              
        # Llamado a objeto de mensaje
        dlg = QMessageBox(self)
        # Título de cuadro de mensage        
        dlg.setWindowTitle(window_title)             
        # Texto que se muestra dentro del cuadro de mensage
        dlg.setText(str(message))
        # Tipo de icono que se muestra en la cuadro de mensage
        dlg.setIcon(QMessageBox.Information)      
        # Muestra el cuadro de mensage
        dlg.show()      


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WidgetWindow()
    window.show()
    sys.exit(app.exec())