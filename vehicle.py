class Vehicle:
    def __init__(self, max_speed, mileage, seating_capacity):
        self._seating_capacity=seating_capacity
        self._max_speed = max_speed
        self._mileage = mileage
 
    def fare(self):
        total_fare = self._seating_capacity * 100
        return total_fare
 
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage,seating_capacity)
        
    def fare(self):
        total_fare = self._seating_capacity * 100
        maintenance_charge = total_fare * 0.10
        final_fare = total_fare + maintenance_charge
        return final_fare
        
# Example 1 for Bus:
bus = Bus(60, 15, 40)
print(f"Bus fare: {bus.fare()}")  # Output: Bus fare: 4400.0

# Example for Vehicle:
car = Vehicle(120,18,5)
print(f"Car fare: {car.fare()}")  # Car fare: 500



