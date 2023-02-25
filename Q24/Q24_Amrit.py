HOUSEHOLD_ENERGY_DATA = [
  {
    "info": {
      "address": "1837 Westview Lane",
      "city": "Surrey",
      "province": "BC",
      "house_type": "Townhouse"
    },
    "number_of_residents": 3,
    "number_of_families": 1,
    "monthly_energy_in_kwh": 1300
  },
  {
    "info": {
      "address": "2768 Windy Avenue",
      "city": "Toronto",
      "province": "ON",
      "house_type": "Apartment"
    },
    "number_of_residents": 1,
    "number_of_families": 1,
    "monthly_energy_in_kwh": 990
  },
    {
    "info": {
      "address": "9008 Westview Lane",
      "city": "Vancouver",
      "province": "BC",
      "house_type": "Apartment"
    },
    "number_of_residents": 2,
    "number_of_families": 1,
    "monthly_energy_in_kwh": 812
  },
  {
    "info": {
      "address": "77 Lincoln Lane",
      "city": "Windsor",
      "province": "ON",
      "house_type": "House"
    },
    "number_of_residents": 7,
    "number_of_families": 2,
    "monthly_energy_in_kwh": 900
  }
  ]

# IN THESE FOLLOWING LINES OF CODE THERE IS A DESCRIPTION OF WHAT SHOULD BE DONE.
# DEBUG THE FUNCTIONALITIES UNTIL THEIR OUTCOME IS WHAT IS DESCRIBED.

# GET AVERAGE ENERGY CONSUMPTION OF RESIDENCES IN ONTARIO AND PRINT IT
number_of_homes = 0
total_energy_in_every_home = 0
for data in HOUSEHOLD_ENERGY_DATA:
    number_of_homes += int(data["number_of_families"])
    if data['info']['province'] == "Ontario":
        total_energy_in_every_home = data['monthly_energy_in_kwh']

average = total_energy_in_every_home // number_of_homes
print(average)

# GET THE LARGEST NUMBER OF HOUSEHOLD OCCUPANTS IN RESIDENCES AND PRINT IT
maximum_residents = 0
for data in HOUSEHOLD_ENERGY_DATA:
    if data["number_of_residents"] > maximum_residents:
        maximum_residents = data["number_of_families"]

print(maximum_residents)
