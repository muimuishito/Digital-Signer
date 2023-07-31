from datetime import datetime


class DateTimeFormatter():
    
    
    def by_now(ranges):
        
        ''' Método que recibe como parámetro de la parte de la hora 
            que se va a retornar, los paramtros pueden ser:
            hours, minutes, seconds, miliseconds
        
        '''
        
        now = datetime.now()
               
        just_hour = str(now).split(' ')       
        # Retorna solo la hora
        if ranges == 'hours':
            
            h = just_hour[-1].split(':')
                
            return h[0]
        # Retorna solo los minutos
        elif ranges == 'minutes':
            m = just_hour[-1].split(':')
            
            return m[1]
        # Retorna solo los segundos
        elif ranges == 'seconds':
            
            s_ms = just_hour[-1].split(':')
            
            s = s_ms[-1].split('.')
            
            return  s[0]
        # Retorna solo los milisegundos
        elif ranges == 'miliseconds':
            
            s_ms = just_hour[-1].split(':')
            
            ms = s_ms[-1].split('.')
            
            return  ms[-1]
               
        
        
        
    
    
    

      

 
# if __name__ == '__main__':
     
#     hour =  DateTimeFormatter.by_now('seconds')
    
    
    
#     print(hour)