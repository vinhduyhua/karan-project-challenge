# Enter width, length of the floor, width and length of the tile, and cost per tile to calculate total cost of the floor

def find_slash(s):
	return s.find('/')

def get_width(s):
	return int(s[:find_slash(s)])

def get_length(s):
	return int(s[find_slash(s)+1:])

try:
	floor_dim = input("Enter width and length of the floor (unit: feet, format: 'W/L'): ")
	tile_dim = input("Enter width and lenght of the tile (unit: inch, format: 'W/L'): ")
	cost_per_tile = input("Enter cost per tile (unit: dollar): ")
	cost_per_tile = int(cost_per_tile)

	floor_area = get_width(floor_dim) * get_length(floor_dim)
	tile_area = get_width(tile_dim)/12 * get_length(tile_dim)/12

	total_cost = (floor_area / tile_area) * cost_per_tile

	print(total_cost)

except:
	print("Invalid Input. Program stop working.")