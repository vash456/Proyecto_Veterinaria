class Person:
    """Class Person displaying person information."""
    def __init__(self, name, last_name, ID, age, phone, email, state):
        self.name = name
        self.last_name = last_name
        self.ID = ID
        self.age = age
        self.phone = phone
        self.email = email
        self.state = state
    
    # To get name:    
    def getName(self):
        return self.name
    
class Customer(Person):
    """Veterinary client. Pet's owner."""
    def __init__(self, name, last_name, ID, age, phone, email, state, pets = []):
        super().__init__(name, last_name, ID, age, phone, email, state)
        self.pets = pets
    
    def add_pet(self):
        pet_name = input("Ingrese el nombre de la mascota: ")
        pet_age = int(input("Ingrese la edad de la mascota: "))
        pet_specie = input("Ingrese la especie de la mascota: ")
        pet_race = input("Ingrese la raza de la mascota: ")
        pet_color = input("Ingrese el color de la mascota: ")
        pet_weight = float(input("Ingrese el peso de la mascota: "))
        pet_gender = input("Ingrese el género de la mascota (F/M): ")
        pet_owner = self.name
        pet = Pet(pet_name, pet_age, pet_specie, pet_race, pet_color, pet_weight, pet_gender, pet_owner) # Related to Pet class
        self.pets.append(pet)
        # Register pet in DB
    
    def delete_pet(self):
        pass

    # def set_up_appointment(available_days):
    #     print("Estas son las fechas disponibles: ", available_days)
    #     day = input("Ingrese la fecha que desea para su cita: ")
    #     print("Estos son los horarios disponibles para el día {0}: ".format(day), available_times)
    #     time = input("Ingrese el horario que desea para su cita: ")
    #     print("Su cita ha quedado agendada para el {0} a las {1}, con {3}".format(day, time, doctor)) # Doctor who has the availability
    #     # Remove the date and time from the available (Doctor and veterinary)
                
    def pay(self, bill):
        # print("{0} debe pagar {1} por motivo de {2}".format(self.name, bill.price, bill.service))
        pass

class VeterinaryDoctor(Person):
    """Veterinary employee."""
    def __init__(self, name, last_name, ID, age, phone, email, state, speciality, salary, availability):
        super().__init__(name, last_name, ID, age, phone, email, state)
        self.speciality = speciality
        self.salary = salary
        self.availability = availability # Dict with dates and times availables. Ex: {2022-06-20:[00:12:00, 12:00:00, 18:00:00]}
 
    def give_diagnosis(pet):
        pass             
        
    def operate(pet, diagnosis):
        pass
    
  