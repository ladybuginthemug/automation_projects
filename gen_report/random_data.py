import json
import random

def generate_random_data(num_records):
    data = []
    car_makes = ["Ford", "Acura", "Volkswagen", "Chevrolet", "Plymouth", "GMC", "Lamborghini", "GMC", "Maybach", "Chevrolet",
                 "Toyota", "Honda", "Nissan", "Mercedes-Benz", "BMW", "Maserati", "Ram", "Mitsubishi", "Subaru", "Bentley",
                 "Kia", "Land Rover", "Volvo", "Mazda", "Infiniti", "Jeep", "Chrysler", "Lexus", "Audi", "Hyundai", "Saturn"]

    car_models = ["Club Wagon", "TL", "Jetta", "Uplander", "Roadrunner", "Safari", "Murciélago", "3500", "62", "Cavalier",
                  "Camry", "Accord", "Altima", "C-Class", "3 Series", "Quattroporte", "1500", "Eclipse", "Outback", "Continental GT",
                  "Optima", "Range Rover", "XC90", "Mazda6", "QX", "Grand Cherokee", "300", "RX", "A6", "Elantra", "Aura"]

    car_years = [1997, 2005, 2009, 2006, 1969, 2000, 2003, 1999, 2004, 2001,
                 2010, 2012, 2007, 2008, 2011, 2005, 1995, 2002, 2004, 2007,
                 2007, 2004, 2008, 2010, 2006, 1997, 1999, 2007, 2006, 2004]

    for i in range(1, num_records + 1):
        record = {
            "id": i,
            "car": {
                "car_make": random.choice(car_makes),
                "car_model": random.choice(car_models),
                "car_year": random.choice(car_years)
            },
            "price": f"${random.uniform(5000, 20000):.2f}",
            "total_sales": random.randint(300, 1200)
        }
        data.append(record)

    return data

def write_to_json(data, json_file):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    num_records = 100  # Change this to the desired number of records
    output_json_file = 'random_data.json'

    random_data = generate_random_data(num_records)
    write_to_json(random_data, output_json_file)

    print(f"Generated {num_records} random records and saved to {output_json_file}.")
