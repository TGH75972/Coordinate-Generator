import random
import os

def generate_secret_base_coordinates(dimension, x_range, z_range, y_min, y_max):
    x = random.randint(x_range[0], x_range[1])
    z = random.randint(z_range[0], z_range[1])
    y = random.randint(y_min, y_max)
    return (x, y, z)

def select_biome():
    biomes = [
        "Plains", "Forest", "Desert", "Mountain", "Swamp",
        "Savanna", "Jungle", "Snowy Tundra", "Taiga", "Mushroom Fields"
    ]
    print("Available biomes:")
    for i, biome in enumerate(biomes):
        print(f"{i + 1}. {biome}")
    choice = int(input("Select a biome by number (or press Enter to skip): ") or 0)
    if 0 < choice <= len(biomes):
        return biomes[choice - 1]
    return None

def save_coordinates_to_file(coords, filename="secret_base_coords.txt"):
    with open(filename, "a") as file:
        file.write(f"X={coords[0]}, Y={coords[1]}, Z={coords[2]}\n")

def validate_dimension(dimension):
    return dimension in ["overworld", "nether"]

def get_coordinate_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter an integer.")

def main():
    print("Minecraft Secret Base Coordinate Generator")

    dimension = input("Enter the dimension (overworld/nether): ").lower()
    while not validate_dimension(dimension):
        print("Invalid dimension. Please enter 'overworld' or 'nether'.")
        dimension = input("Enter the dimension (overworld/nether): ").lower()

    min_x = get_coordinate_input("Enter the minimum x-coordinate: ")
    max_x = get_coordinate_input("Enter the maximum x-coordinate: ")
    min_z = get_coordinate_input("Enter the minimum z-coordinate: ")
    max_z = get_coordinate_input("Enter the maximum z-coordinate: ")

    if dimension == "overworld":
        y_min = get_coordinate_input("Enter the minimum y-coordinate (recommended 63 for ground level): ")
        y_max = get_coordinate_input("Enter the maximum y-coordinate (recommended 128 for underground base): ")
    elif dimension == "nether":
        y_min = get_coordinate_input("Enter the minimum y-coordinate (recommended 32 for ground level): ")
        y_max = get_coordinate_input("Enter the maximum y-coordinate (recommended 64 for underground base): ")

    x_range = (min_x, max_x)
    z_range = (min_z, max_z)

    biome = select_biome()
    if biome:
        print(f"Selected biome: {biome}")

    coordinates = generate_secret_base_coordinates(dimension, x_range, z_range, y_min, y_max)
    print(f"Generated coordinates for secret base: X={coordinates[0]}, Y={coordinates[1]}, Z={coordinates[2]}")

    save_option = input("Do you want to save these coordinates to a file? (yes/no): ").lower()
    if save_option == "yes":
        save_coordinates_to_file(coordinates)
        print(f"Coordinates saved to secret_base_coords.txt")
    else:
        print("Coordinates not saved.")
        
    generate_another = input("Do you want to generate another set of coordinates? (yes/no): ").lower()
    if generate_another == "yes":
        main()

if __name__ == "__main__":
    main()
