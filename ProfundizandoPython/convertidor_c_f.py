class ConvertidorTemperatura:

    MAX_CELCIUS = 100
    MAX_FAHRENHEIT=213

    @classmethod
    def c_f(cls,celcius):
        if celcius > cls.MAX_CELCIUS:
            raise ValueError('Temperatura C demasiado alta:',celcius)
        return celcius * 9/5 + 32

    @classmethod
    def f_c(cls,fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError('Temperatura en F demasiado alta:',fahrenheit)
        return (fahrenheit - 32) * 5/9

if __name__=='__main__':
    resultado=ConvertidorTemperatura.c_f(15)
    print(f'celcius a fahrenheit:{resultado:.2f}')
    resultado=ConvertidorTemperatura.f_c(200)
    print(f'fahrenheit a celsius:{resultado:.2f}')