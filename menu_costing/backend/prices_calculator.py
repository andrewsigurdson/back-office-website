import json
#from urllib.request import urlopen

#SEE sample_input.json FOR INPUT SHAPE
#NOTES:
#   unit must be the same between bulk and individual
#   (if I order cheese in ounces, the menu must use ounces)

#return output format
#menu_items
#   name
#   item_name:
#   30% price (costx3):
#   25% price (costx4):
#   current price % markup:


#***************** GET THE JSON INFO FROM WEB **********************
#with urlopen(***endpoint?***) as response:
#    source = response.read()

#***************** TEMPORARY GET JSON FROM FILE ********************
with open('sample_input.json') as source:
    data = json.load(source)

class Info:
    def __init__(self, material_cost, thirty_price, twenty_five_price, current_markup):
        self.material_cost = material_cost
        self.thirty_price = thirty_price
        self.twenty_five_price = twenty_five_price
        self.current_markup = current_markup


#***************** CALCULATE INGREDIENT UNIT COSTS ****************
unit_costs = {}

for ingredient in data['ingredients']:
    unit_price = ingredient['bulk_total_price'] / (ingredient['bulk_size'] * ingredient['bulk_individual_size'])
    unit_costs[ingredient['name']] = round(unit_price, 2)

print(unit_costs)

output = {}

output['menu_items'] = []

for item in data['menu']:
    material_cost = 0
    for ingredient in item['ingredients']:
        material_cost += (unit_costs[ingredient['name']] * ingredient['quantity'])
    thirty_price = 3 * material_cost
    twenty_five_price = 4 * material_cost
    current_markup = material_cost / item['asking_price']
    output['menu_items'].append({
        "name": item['name'],
        "total_material_cost": round(material_cost, 2),
        "twenty_five_p_menu_price": round(twenty_five_price, 2),
        "thirty_p_menu_price": round(thirty_price, 2),
        "current_markup_percent": round(current_markup, 2) * 100
    })

with open('output.json', 'w') as outfile:
    json.dump(output, outfile, indent=2)



#***************** SEND THE JSON INFO BACK TO THE WEB **********************
# TODO
#



# END

