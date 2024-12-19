class Vehicle:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model
        
    def start(self):
        return f"{self.brand} - {self.model} is starting."


class GasolinEngine:
    def __init__(self, fuel_capacity ):
        self.fuel_capacity= fuel_capacity
        self.fuel_efficiency=15

    def refuel(self,amount):
            self.amount = amount
            self.fuel_capacity += self.amount
            return f"{self.amount} Liters of gasoline added. Currnet  capacity: {self.fuel_capacity} Liter "
    def consume_fuel(self,amount):
            self.amount = amount
            self.fuel_capacity -= self.amount
            return f"{self.amount} of gasoline consumed. Remanining capacity: {self.fuel_capacity} ."
    def calculate_range(self,):
          return f"Remanining range on gasoline : {self.fuel_capacity * self.fuel_efficiency} KM. "

class ElectricEngine:
    def __init__(self, battery_capacity):
            self.battery_capacity = battery_capacity
            self.efficiency_per_kwh= 6
    def charge(self,amount):
          self.amount= amount
          self.battery_capacity += self.amount
          return f"{self.amount} kwh charged. Currnet battery capacity: {self.battery_capacity} kwh "

    def consume_battery(self,amount):
            self.amount = amount
            self.battery_capacity -= self.amount
            return f"{self.amount} of battery consumed. Remanining capacity: {self.battery_capacity} ."
        
    def calculate_range(self,):
        return f"Remanining range on battery : {self.fuel_capacity * self.fuel_efficiency} KM. "

          
         


class HybridCar( Vehicle, GasolinEngine,ElectricEngine ):
    def __init__(self, brand, model, fuel_capacity ,battery_capacity):
        Vehicle.__init__(self,brand,model)
        GasolinEngine.__init__(self,fuel_capacity)
        ElectricEngine.__init__(self,battery_capacity)

    
    def drive(self):
        return f"{self.brand} - {self.model} driving in hybird mode."
    
    def total_range(self):
         
         return f"Total range: {(self.fuel_capacity * self.fuel_efficiency) + (self.fuel_capacity * self.fuel_efficiency)} KM. "
         
    def consume_resources(self, fuel_amount, battery_amount):
    
        if fuel_amount > self.fuel_capacity:
         return f"Not enough fuel. Current fuel capacity: {self.fuel_capacity} liters."

        if battery_amount > self.battery_capacity:
            return f"Not enough battery charge. Current battery capacity: {self.battery_capacity} kWh."

        self.fuel_capacity -= fuel_amount
        self.battery_capacity -= battery_amount

        return (
        f"Consumed {fuel_amount} liters of fuel and {battery_amount} kWh of battery. "
        f"Remaining fuel: {self.fuel_capacity} liters, "
        f"Remaining battery: {self.battery_capacity} kWh."
    )
         
if __name__ == "__main__":
    hybrid_car = HybridCar("Toyota", "Prius", 40, 8.8)

    print(hybrid_car.start())  
    print(hybrid_car.refuel(20))  
    print(hybrid_car.charge(5))  
    print(hybrid_car.drive())  
    print(hybrid_car.consume_resources(10, 2))
    print(hybrid_car.calculate_range()) 
    print(hybrid_car.total_range()) 