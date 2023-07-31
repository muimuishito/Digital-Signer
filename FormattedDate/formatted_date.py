from datetime import datetime, timedelta, date


class FormattedDate:
    
    # Obtiene fecha actual
    now = datetime.now()
    
    month = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    
    days = {
        0: "Domingo",
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
    }
    
    # Función que recibe fecha string con formato dia/mes/año y retorna el mes en letras 
    def number_month_to_letters(date):
        
        # Transforma el tipo de dato en caso de ser diferente de string
        if date.__class__.__name__ != 'class str':
            date = date
        
        # Divide la cadena por cada símbolo '/'
        splitted_date = date.split('/')
        # Recive entero y retorna mes en letras según número de mes
        month = FormattedDate.month.get(int(splitted_date[1]))
        
        return month
    
    
    def transformed_date(date):        
        '''Método que recibe string como argumento
            con entrada 12/04/2022 y retorna 12 de Abril de 2022
        '''        
        # Transforma el tipo de dato en caso de ser diferente de string
        if date.__class__.__name__ != 'class str':
            date = date        
        # Divide la cadena por cada símbolo /
        splitted_date = date.split('/')        
        return splitted_date[0] + ' de ' + FormattedDate.number_month_to_letters(date) + ' de ' + splitted_date[2]
        
    
    
    def formated_date_by_month_with_letters():
        ''' Método que proporciona la fecha actual 
            ejemplo:
            en lugar de 01/04/2023 retorna 1 de Abril del 2023'''    
        # Obtiene numero de mes
        month_number = FormattedDate.now.month
        # formatea fecha para obtener dia de la semana
        day_number = int(FormattedDate.now.strftime("%w"))
        # Lee diccionario days y obtiene día de semana según su número 
        day = FormattedDate.days.get(day_number)
        # Lee diccionario month y obtiene el mes sgún su número
        month = FormattedDate.month.get(month_number)
        # Obtiene la fecha formateada 
        formated_date = "{} de {} del {}".format(FormattedDate.now.day, month, FormattedDate.now.year)
        
        return formated_date


    def formated_date(): 
        '''Regresa fecha en formato dd/mm/aa'''
        day = FormattedDate.now.day
        month = FormattedDate.now.month
        year = FormattedDate.now.year
    
        if FormattedDate.now.day < 10:
            day = FormattedDate.now.day
            day = '0'+str(day)
        if FormattedDate.now.month < 10:
            month = FormattedDate.now.month      
            month = '0'+str(month)
        
        return str(day)+'/'+str(month)+'/'+str(year)     


    def formated_date_by_day():      
        '''Retorna el número de día de la fecha actual'''
        day = FormattedDate.now.day
        
        if FormattedDate.now.day < 10:
            day = FormattedDate.now.day
            day = '0'+str(day)          
        
        return  day
    
    
    def formated_date_by_month():         
        '''Retorna el número de mes de la fecha actual'''
        month = FormattedDate.now.month
        
        if FormattedDate.now.month < 10:
            month = FormattedDate.now.month      
            month = '0'+str(month)        
        
        return month                       
            
            
    def formated_date_by_year():       
        return str(FormattedDate.now.year)
    
    
    
    def by_added_days(days):
        ''' Suma los días que se envian en el parámetro days 
            a la fecha actual y retorna la dicha fecha en formato dd/mm/aaaa'''
        curr_date = date.today()                    
        added_days = curr_date + timedelta(days= days)       
        splitted_date = str(added_days).split('-')
        
        return splitted_date[2]+ '/' + splitted_date[1] +  '/' + splitted_date[0]
        
        
# if __name__ == '__main__':
#     fd = FormattedDate()
#     print(fd.by_added_days(4))