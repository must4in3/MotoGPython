import random

class Moto:
    def __init__(self, marca, modelo, acceleration, top_speed, handling):
        self.marca = marca
        self.modelo = modelo
        self.acceleration = acceleration
        self.top_speed = top_speed
        self.handling = handling

    def print_info(self):
        print(self.marca, self.modelo, self.acceleration, self.top_speed, self.handling)  

    def setup_moto(self):
        self.mean_speed = self.top_speed*self.acceleration*self.handling
        skills_pilot = 0
        


class Yamaha(Moto):
    def __init__(self, marca, modelo, acceleration, top_speed, handling, name_pilot):
        super().__init__(marca, modelo, acceleration, top_speed, handling)
        self.name_pilot = name_pilot

    def pilot(self):
        if self.name_pilot == 'Valentino Rossi':
            skills_pilot = 0.85
        elif self.name_pilot == 'Maverick Viñales':
            skills_pilot = 0.79
        self.setting_pilot = self.mean_speed * skills_pilot
        return f'{self.name_pilot} has finished setting his motorcycle. Mean speed that can be achieved: {round(self.setting_pilot,2)} km/h'



class Honda_Hrc(Moto):
    def __init__(self, marca, modelo, acceleration, top_speed, handling, name_pilot):
        super().__init__(marca, modelo, acceleration, top_speed, handling)
        self.name_pilot = name_pilot

    def pilot(self):
        if self.name_pilot == 'Marc Marquez':
            skills_pilot = 0.81
        elif self.name_pilot == 'Dani Pedrosa':
            skills_pilot = 0.79
        self.setting_pilot = self.mean_speed * skills_pilot
        return f'{self.name_pilot} has finished setting his motorcycle. Mean speed that can be achieved: {round(self.setting_pilot,2)} km/h'


class Ducati(Moto):
    def __init__(self, marca, modelo, acceleration, top_speed, handling, name_pilot):
        super().__init__(marca, modelo, acceleration, top_speed, handling)
        self.name_pilot = name_pilot

    def pilot(self):
        if self.name_pilot == 'Andrea Dovizioso':
            skills_pilot = 0.80
        elif self.name_pilot == 'Danilo Petrucci':
            skills_pilot = 0.77
        self.setting_pilot = self.mean_speed * skills_pilot
        return f'{self.name_pilot} has finished setting his motorcycle. Mean speed that can be achieved: {round(self.setting_pilot,2)} km/h'


class Circuit:
    def __init__(self, name, length, rounds):
        self.name = name
        self.length = length
        self.rounds = rounds

    def print_info(self):
        print(f'''\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
To all the lovers of the world championship of motorcycle welcome to our beautiful valley of {self.name}! {self.length} km, {self.rounds} laps. We wish you the most pleasant stay!
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n''') 


    def meteo(self):
        wheather = ['Sunny', 'Rainy', 'Cloudy', 'Windy']
        meteo = random.choice(wheather)
        print('Today\'s weather:', meteo)
        if meteo == 'Sunny':
            yamaha_Rossi.setting_pilot = yamaha_Rossi.setting_pilot * 1.01 
            yamaha_Viñales.setting_pilot =  yamaha_Viñales.setting_pilot * 1.01 
            honda_Marquez.setting_pilot = honda_Marquez.setting_pilot *1.01
            ducati_Dovi.setting_pilot = ducati_Dovi.setting_pilot * 0.99 
            ducati_Petrux.setting_pilot = ducati_Petrux.setting_pilot * 0.99 
            honda_Pedrosa.setting_pilot = honda_Pedrosa.setting_pilot * 0.99
            print('\nBonus weather: Rossi, Viñales and Marquez. Malus weather: Dovi, Petrux and Pedrosa\n')
        elif meteo == 'Rainy':
            yamaha_Rossi.setting_pilot = yamaha_Rossi.setting_pilot * 1.01 
            yamaha_Viñales.setting_pilot =  yamaha_Viñales.setting_pilot * 0.99 
            honda_Marquez.setting_pilot = honda_Marquez.setting_pilot *0.99
            ducati_Dovi.setting_pilot = ducati_Dovi.setting_pilot * 1.01 
            ducati_Petrux.setting_pilot = ducati_Petrux.setting_pilot * 0.99 
            honda_Pedrosa.setting_pilot = honda_Pedrosa.setting_pilot * 1.01
            print('\nBonus weather: Rossi, Dovi and Pedrosa. Malus weather: Viñales, Marquez and Petrux\n')
        elif meteo == 'Cloudy':
            yamaha_Rossi.setting_pilot = yamaha_Rossi.setting_pilot * 0.99 
            yamaha_Viñales.setting_pilot =  yamaha_Viñales.setting_pilot * 1.01 
            honda_Marquez.setting_pilot = honda_Marquez.setting_pilot *0.99
            ducati_Dovi.setting_pilot = ducati_Dovi.setting_pilot * 1.01 
            ducati_Petrux.setting_pilot = ducati_Petrux.setting_pilot * 1.01 
            honda_Pedrosa.setting_pilot = honda_Pedrosa.setting_pilot * 0.99
            print('\nBonus weather: Viñales, Dovi and Petrux. Malus weather: Rossi, Marquez and Pedrosa\n')    
        elif meteo == 'Windy':
            yamaha_Rossi.setting_pilot = yamaha_Rossi.setting_pilot * 0.99 
            yamaha_Viñales.setting_pilot =  yamaha_Viñales.setting_pilot * 0.99
            honda_Marquez.setting_pilot = honda_Marquez.setting_pilot * 1.01
            ducati_Dovi.setting_pilot = ducati_Dovi.setting_pilot * 0.99 
            ducati_Petrux.setting_pilot = ducati_Petrux.setting_pilot * 1.01 
            honda_Pedrosa.setting_pilot = honda_Pedrosa.setting_pilot * 1.01  
            print('\nBonus weather: Marquez, Petrux and Dovi. Malus weather: Rossi, Viñales and Dovi\n')

    def Race(self):
        pilots = ['Rossi', 'Viñales', 'Marquez', 'Pedrosa', 'Dovizioso', 'Petrucci']
        for lap in range(self.rounds):
            position = []
            print(f'\nLap {lap+1}\n')
            position.append(yamaha_Rossi.setting_pilot * random.uniform(0.99,1.01))
            position.append(yamaha_Viñales.setting_pilot * random.uniform(0.99,1.01))
            position.append(honda_Marquez.setting_pilot * random.uniform(0.99,1.01))
            position.append(ducati_Dovi.setting_pilot * random.uniform(0.99,1.01))
            position.append(ducati_Petrux.setting_pilot * random.uniform(0.99,1.01))
            position.append(honda_Pedrosa.setting_pilot * random.uniform(0.99,1.01))
            new_position = [*position]
            new_position.sort(reverse= True)
            orden = []
            for x in new_position:              
                orden.append(position.index(x))
            for p in orden:
                print(f'{orden.index(p)+1} position: {pilots[p]}')


            

#m1 = Moto('Yamaha', 'M1', 0.74, 358, 0.84)
#m1.Setup_moto()
print('''\n#   #        #  #          #   #   #          #     #  #
#   #        #  #          #  # #  #          #     #  #
#   #   ##   #  #   ##      # # # #   ##   ## #   ###  #
#####  #  #  #  #  #  #     # # # #  #  #  #  #  #  #  #
#   #  ####  #  #  #  # ##  # # # #  #  #  #  #  #  #  #
#   #  #     #  #  #  #     # # # #  #  #  #  #  #  #   
#   #   ###  #  #   ##       #   #    ##   #  #   ###  #\n''')

print(' ################Welcome to MotoGPython###############\n\n')

yamaha_Rossi = Yamaha('Yamaha', 'M1', 0.75, 359, 0.78, 'Valentino Rossi')
yamaha_Viñales = Yamaha('Yamaha', 'M1', 0.77, 360, 0.80, 'Maverick Viñales')
honda_Marquez = Honda_Hrc('Honda', 'RC212V', 0.78, 362, 0.78, 'Marc Marquez')
honda_Pedrosa = Honda_Hrc('Yamaha', 'RC212V', 0.77, 360, 0.81, 'Dani Pedrosa')
ducati_Dovi = Ducati('Ducati', 'Desmosedici', 0.81, 365, 0.75, 'Andrea Dovizioso')
ducati_Petrux = Ducati('Ducati', 'Desmosedici', 0.83, 362, 0.76, 'Danilo Petrucci')

yamaha_Rossi.setup_moto()
yamaha_Viñales.setup_moto()
honda_Marquez.setup_moto()
honda_Pedrosa.setup_moto()
ducati_Dovi.setup_moto()
ducati_Petrux.setup_moto()

print(yamaha_Rossi.pilot())
print(yamaha_Viñales.pilot())
print(honda_Marquez.pilot())
print(honda_Pedrosa.pilot())
print(ducati_Dovi.pilot())
print(ducati_Petrux.pilot())


mugello = (Circuit('Mugello', 5.245, 23))
mugello.print_info()
mugello.meteo()

mugello.Race()



#rc212v = Moto('Honda', 'rc212v', 0.78, 360, 0.80)
#rc212v.print_info()
#rc212v.Setup_moto()

#Circuit('Mugello', 5.245, 23)