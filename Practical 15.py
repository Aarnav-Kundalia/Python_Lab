import math

def normalize_angle(angle, min_val, max_val):
    period = max_val - min_val
    while angle < min_val:
        angle += period
    while angle > max_val:
        angle -= period
    return angle

def validate_spherical(r, θ, φ):
    if r < 0:
        raise ValueError("r must be non-negative")
    return (r, 
            normalize_angle(θ, 0, math.pi),
            normalize_angle(φ, -math.pi, math.pi))

def validate_cylindrical(s, φ, z):
    if s < 0:
        raise ValueError("s must be non-negative")
    return (s, normalize_angle(φ, -math.pi, math.pi), z)

def get_coordinate_systems():
    print("\nAvailable coordinate systems:")
    print("1. Cartesian (x, y, z)")
    print("2. Cylindrical (s, φ, z)") 
    print("3. Spherical (r, θ, φ)")
    
    while True:
        try:
            input_system = int(input("\nEnter number for input coordinate system (1-3): "))
            output_system = int(input("Enter number for output coordinate system (1-3): "))
            if 1 <= input_system <= 3 and 1 <= output_system <= 3:
                return input_system, output_system
            print("Please enter valid numbers (1-3)")
        except ValueError:
            print("Please enter valid numbers")

def get_coordinates(system):
    try:
        if system == 1:
            x = float(input("Enter x: "))
            y = float(input("Enter y: "))
            z = float(input("Enter z: "))
            return (x, y, z)
        elif system == 2:
            s = float(input("Enter s: "))
            φ = float(input("Enter φ (in degrees): "))
            z = float(input("Enter z: "))
            return validate_cylindrical(s, math.radians(φ), z)
        else:
            r = float(input("Enter r: "))
            θ = float(input("Enter θ (in degrees): "))
            φ = float(input("Enter φ (in degrees): "))
            return validate_spherical(r, math.radians(θ), math.radians(φ))
    except ValueError as e:
        raise ValueError(f"Invalid input: {str(e)}")

def cartesian_to_cylindrical(x, y, z):
    s = math.sqrt(x*x + y*y)
    φ = math.atan2(y, x)
    return validate_cylindrical(s, φ, z)

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x*x + y*y + z*z)
    θ = math.acos(z/r) if r != 0 else 0
    φ = math.atan2(y, x)
    return validate_spherical(r, θ, φ)

def cylindrical_to_cartesian(s, φ, z):
    x = s * math.cos(φ)
    y = s * math.sin(φ)
    return (x, y, z)

def cylindrical_to_spherical(s, φ, z):
    r = math.sqrt(s*s + z*z)
    θ = math.acos(z/r) if r != 0 else 0
    return validate_spherical(r, θ, φ)

def spherical_to_cartesian(r, θ, φ):
    x = r * math.sin(θ) * math.cos(φ)
    y = r * math.sin(θ) * math.sin(φ)
    z = r * math.cos(θ)
    return (x, y, z)

def spherical_to_cylindrical(r, θ, φ):
    s = r * math.sin(θ)
    z = r * math.cos(θ)
    return validate_cylindrical(s, φ, z)

def transform_coordinates(input_system, output_system, coords):
    try:
        if input_system == 1:
            cart_coords = coords
        elif input_system == 2:
            cart_coords = cylindrical_to_cartesian(*coords)
        else:
            cart_coords = spherical_to_cartesian(*coords)
        
        if output_system == 1:
            return cart_coords
        elif output_system == 2:
            return cartesian_to_cylindrical(*cart_coords)
        else:
            return cartesian_to_spherical(*cart_coords)
    except Exception as e:
        raise ValueError(f"Transformation error: {str(e)}")

def main():
    print("Welcome to Coordinate System Transformer")
    
    try:
        input_system, output_system = get_coordinate_systems()
        coords = get_coordinates(input_system)
        result = transform_coordinates(input_system, output_system, coords)
        
        systems = {1: "Cartesian", 2: "Cylindrical", 3: "Spherical"}
        print(f"\nTransformed coordinates from {systems[input_system]} to {systems[output_system]}:")
        
        if output_system == 1:
            print(f"x = {result[0]:.4f}")
            print(f"y = {result[1]:.4f}")
            print(f"z = {result[2]:.4f}")
        elif output_system == 2:
            print(f"s = {result[0]:.4f}")
            print(f"φ = {math.degrees(result[1]):.4f}°")
            print(f"z = {result[2]:.4f}")
        else:
            print(f"r = {result[0]:.4f}")
            print(f"θ = {math.degrees(result[1]):.4f}°")
            print(f"φ = {math.degrees(result[2]):.4f}°")
            
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please try again with valid inputs")

if __name__ == "__main__":
    main()


