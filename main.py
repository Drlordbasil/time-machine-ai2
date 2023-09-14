import math

def calculate_energy(mass, velocity):
    energy = (mass * velocity ** 2) / 2
    return energy

def calculate_time_traveled(distance, velocity):
    time = distance / velocity
    return time

def calculate_acceleration(force, mass):
    acceleration = force / mass
    return acceleration

def calculate_required_power(energy, time):
    power = energy / time
    return power

def calculate_force(mass, acceleration):
    force = mass * acceleration
    return force

def calculate_mass(energy, velocity):
    mass = (2 * energy) / velocity ** 2
    return mass

def calculate_velocity(distance, time):
    velocity = distance / time
    return velocity

def calculate_distance(velocity, time):
    distance = velocity * time
    return distance

def generate_schematics():
    schematics = ''' 
    --------------------------------------------------
              Time Machine Schematics 
    --------------------------------------------------
                 
                       Energy                    
                 ------------------
                 |                |
            Mass |                | Velocity
                 |                |
                 ------------------
                    
                      [ Calculate ]
                      
            The energy formula is given by:
            E = (m * v^2) / 2
            
            The time traveled formula is given by:
            t = d / v
      
            The acceleration formula is given by:
            a = F / m
            
            The required power formula is given by:
            P = E / t
            
            The force formula is given by:
            F = m * a
            
            The mass formula is given by:
            m = (2 * E) / v^2
            
            The velocity formula is given by:
            v = d / t
            
            The distance formula is given by:
            d = v * t
            
    --------------------------------------------------
    '''
    return schematics

def main():
    print(generate_schematics())
    
    print("Enter the values for the variables:")
    mass = float(input("Mass (in kg): "))
    velocity = float(input("Velocity (in m/s): "))
    distance = float(input("Distance (in meters): "))
    time = float(input("Time (in seconds): "))
    force = float(input("Force (in N): "))
    energy = float(input("Energy (in J): "))
    
    print("Calculating results...\n")
    
    acceleration = calculate_acceleration(force, mass)
    power = calculate_required_power(energy, time)
    
    print("Results:")
    print("Acceleration:", acceleration, "m/s^2")
    print("Power:", power, "W")
    
    if mass == 0:
        mass = calculate_mass(energy, velocity)
        print("Mass:", mass, "kg")
    
    if velocity == 0:
        velocity = calculate_velocity(distance, time)
        print("Velocity:", velocity, "m/s")
    
    if distance == 0:
        distance = calculate_distance(velocity, time)
        print("Distance:", distance, "m")
    
    if time == 0:
        time = calculate_time_traveled(distance, velocity)
        print("Time Traveled:", time, "s")
    
    if force == 0:
        force = calculate_force(mass, acceleration)
        print("Force:", force, "N")

if __name__ == "__main__":
    main()