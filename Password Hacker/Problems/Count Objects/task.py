wall_street_houses = House.objects.filter(street='Wall st.')
wall_street_houses_number = wall_street_houses.count()
