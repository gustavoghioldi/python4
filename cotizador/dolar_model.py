from datetime import datetime


class DolarModel:
    def __init__(self, oficial, solidario, blue, ccb, mep, ccl):
        self.__oficial = oficial
        self.__solidario = solidario
        self.__blue = blue
        self.__ccb = ccb
        self.__mep = mep
        self.__ccl = ccl
        self.__time = None
        
        
    def get(self, dolar_type):
        if dolar_type == 'oficial':
            return self.__oficial
        elif dolar_type == 'solidario':
            return self.__solidario
        elif dolar_type == 'blue':
            return self.__blue
        elif dolar_type == 'ccb':
            return self.__ccb
        elif dolar_type == 'mep':
            return self.__mep
        elif dolar_type == 'ccl':
            return self.__ccl
        else:
            pass    

    def set_time(self, time):
        self.__time = time    

    def get_list(self)->list:
        return [self.__oficial,
            self.__solidario,
            self.__blue,
            self.__ccb ,
            self.__mep ,
            self.__ccl ,
            str(datetime.now()) ]      

                            
         
        