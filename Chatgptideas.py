def find_optimal_coplanting_options(ranked_options, num_coplants=4):
    optimal_options = {}
    used_options = set()
    for plant in ranked_options:
        optimal_options[plant] = []
        for option, rank, mutuals in ranked_options[plant]:
            if len(optimal_options[plant]) >= num_coplants:
                break
            if option not in used_options:
                mutual_options = mutuals
                if all([o in mutual_options for o in used_options]):
                    optimal_options[plant].append(option)
                    used_options.add(option)
    return optimal_options

ranked_options = {'Cabbage': [('Melon', 5, ['Nasturtium', 'Oregano', 'Onion', 'Garlic', 'Chamomile']), ('Carrot', 3, ['Melon', 'Onion', 'Garlic']), ('Onion', 3, ['Beetroot', 'Melon', 'Carrot']), ('Beetroot', 2, ['Onion', 'Sage']), ('Garlic', 2, ['Melon', 'Carrot']), ('Nasturtium', 1, ['Melon']), ('Oregano', 1, ['Melon']), ('Chamomile', 1, ['Melon']), ('Sage', 1, ['Beetroot']), ('Celeriac', 0, []), ('Thyme', 0, []), ('Dill', 0, []), ('Celery', 0, []), ('Rosemary', 0, []), ('Potatoes', 0, [])], 'Aubergine': [('Peppers', 5, ['Onion', 'Garlic', 'Nasturtium', 'Lettuce', 'Thyme']), ('Onion', 1, ['Peppers']), ('Garlic', 1, ['Peppers']), ('Nasturtium', 1, ['Peppers']), ('Lettuce', 1, ['Peppers']), ('Thyme', 1, ['Peppers']), ('Potatoes', 0, []), ('Mint', 0, []), ('Chickpea', 0, []), ('Sweet pea', 0, []), ('Bean', 0, []), ('Spinach', 0, [])], 'Celeriac': [('Cabbage', 0, []), ('Leek', 0, []), ('Tomato', 0, []), ('Black bean', 0, []), ('Runner beans', 0, [])], 'Beetroot': [('Peppers', 3, ['Lettuce', 'Radish', 'Onion']), ('Mustard', 3, ['Chickpea', 'Mint', 'Onion']), ('Onion', 3, ['Cabbage', 'Peppers', 'Mustard']), ('Cabbage', 2, ['Onion', 'Sage']), ('Lettuce', 1, ['Peppers']), ('Chickpea', 1, ['Mustard']), ('Mint', 1, ['Mustard']), ('Radish', 1, ['Peppers']), ('Sage', 1, ['Cabbage'])], 'Peppers': [('Carrot', 4, ['Lettuce', 'Radish', 'Garlic', 'Onion']), ('Lettuce', 1, ['Carrot']), ('Tomato', 1, ['Carrot']), ('Radish', 1, ['Carrot']), ('Garlic', 1, ['Carrot']), ('Onion', 1, ['Carrot']), ('Thyme', 0, []), ('Rosemary', 0, []), ('Cucumber', 0, []), ('Nasturtium', 0, []), ('Oregano', 0, []), ('bean', 0, []), ('Dill', 0, []), ('Marjoram', 0, []), ('Parsley', 0, []), ('squash', 0, []), ('Physalis', 0, [])], 'Mustard': [('Thyme', 0, []), ('Sweet pea', 0, []), ('Rosemary', 0, []), ('Chickpea', 0, []), ('Cucumber', 0, []), ('Mint', 0, []), ('Onion', 0, []), ('Celery', 0, [])], 'Melon': [('Carrot', 4, ['Lettuce', 'Radish', 'Garlic', 'Onion']), ('Lettuce', 1, ['Carrot']), ('Radish', 1, ['Carrot']), ('Garlic', 1, ['Carrot']), ('Onion', 1, ['Carrot']), ('Sweet pea', 0, []), ('Leek', 0, []), ('Chickptea', 0, []), ('Chamomile', 0, []), ('Nasturtium', 0, []), ('Oregano', 0, []), ('bean', 0, []), ('Lavender', 0, []), ('Mint', 0, [])], 'Loofah': [('Carrot', 1, ['Onion']), ('Onion', 1, ['Carrot']), ('Nasturtium', 0, []), ('Oregano', 0, []), ('squash', 0, []), ('Mint', 0, [])], 'Courgette': [('Radish', 0, []), ('Dill', 0, []), ('Oregano', 0, []), ('Nasturtium', 0, [])], 'Tomato': [('Potatoes', 0, [])], 'Carrot': [('Onion', 0, []), ('Garlic', 0, []), ('Bean', 0, []), ('Lettuce', 0, []), ('chickpeas', 0, []), ('Radish', 0, []), ('Tomato', 0, [])], 'Dill': [('Cabbage', 0, []), ('Peppers', 0, []), ('Courgette', 0, [])], 'Physalis': [('Peppers', 0, [])], 'Leek': [('Celeriac', 0, []), ('Melon', 0, [])], 'Lavender': [('Melon', 0, [])], 'Chamomile': [('Melon', 1, ['Cabbage']), ('Cabbage', 0, [])], 'Marjoram': [('Peppers', 0, [])], 'Sweet pea': [('Aubergine', 0, []), ('Mustard', 0, []), ('Melon', 0, [])], 'Sage': [('Cabbage', 1, ['Beetroot']), ('Beetroot', 1, ['Cabbage'])], 'Runner beans': [('Celeriac', 0, [])], 'Bean': [('Aubergine', 0, []), ('Carrot', 0, [])], 'bean': [('Peppers', 0, []), ('Melon', 0, [])], 'Parsley': [('Peppers', 0, [])], 'Oregano': [('Melon', 1, ['Cabbage']), ('Cabbage', 0, []), ('Peppers', 0, []), ('Loofah', 0, []), ('Courgette', 0, [])], 'Lettuce': [('Peppers', 2, ['Aubergine', 'Beetroot']), ('Carrot', 2, ['Peppers', 'Melon']), ('Aubergine', 0, []), ('Beetroot', 0, []), ('Melon', 0, [])], 'Radish': [('Carrot', 2, ['Peppers', 'Melon']), ('Peppers', 1, ['Beetroot']), ('Beetroot', 0, []), ('Melon', 0, []), ('Courgette', 0, [])], 'Onion': [('Carrot', 4, ['Cabbage', 'Peppers', 'Melon', 'Loofah']), ('Peppers', 2, ['Aubergine', 'Beetroot']), ('Cabbage', 1, ['Beetroot']), ('Beetroot', 1, ['Cabbage']), ('Mustard', 1, ['Beetroot']), ('Melon', 1, ['Cabbage']), ('Aubergine', 0, []), ('Loofah', 0, [])], 'Rosemary': [('Cabbage', 0, []), ('Peppers', 0, []), ('Mustard', 0, [])], 'Spinach': [('Aubergine', 0, [])], 'Garlic': [('Carrot', 3, ['Cabbage', 'Peppers', 'Melon']), ('Peppers', 1, ['Aubergine']), ('Melon', 1, ['Cabbage']), ('Cabbage', 0, []), ('Aubergine', 0, [])], 'chickpeas': [('Carrot', 0, [])], 'Cucumber': [('Peppers', 0, []), ('Mustard', 0, [])], 'Chickpea': [('Mustard', 1, ['Beetroot']), ('Aubergine', 0, []), ('Beetroot', 0, [])], 'Potatoes': [('Cabbage', 0, []), ('Aubergine', 0, []), ('Tomato', 0, [])], 'squash': [('Peppers', 0, []), ('Loofah', 0, [])], 'Mint': [('Mustard', 1, ['Beetroot']), ('Aubergine', 0, []), ('Beetroot', 0, []), ('Melon', 0, []), ('Loofah', 0, [])], 'Black bean': [('Celeriac', 0, [])], 'Thyme': [('Peppers', 1, ['Aubergine']), ('Cabbage', 0, []), ('Aubergine', 0, []), ('Mustard', 0, [])], 'Nasturtium': [('Peppers', 1, ['Aubergine']), ('Melon', 1, ['Cabbage']), ('Cabbage', 0, []), ('Aubergine', 0, []), ('Loofah', 0, []), ('Courgette', 0, [])], 'Chickptea': [('Melon', 0, [])], 'Celery': [('Cabbage', 0, []), ('Mustard', 0, [])]}


optimal_options = find_optimal_coplanting_options(ranked_options)
print(optimal_options)





def select_optimal_coplanting_options(ranked_options, num_options):
    optimal_options = {}
    for plant in ranked_options:
        optimal_options[plant] = []
        selected_options = set()
        for option, rank in ranked_options[plant]:
            if len(optimal_options[plant]) >= num_options:
                break
            if option not in selected_options:
                optimal_options[plant].append(option)
                selected_options.add(option)
                for mutual_option, mutual_rank in ranked_options[option]:
                    if len(optimal_options[mutual_option]) < num_options and mutual_option not in selected_options:
                        optimal_options[mutual_option].append(plant)
                        selected_options.add(mutual_option)
    return optimal_options

ranked_options = {
    'tomatoes': [('basil', 2), ('carrots', 1), ('onions', 1)],
    'basil': [('peppers', 1), ('tomatoes', 2)],
    'peppers': [('basil', 1), ('cucumbers', 1)],
    'cucumbers': [('peppers', 1), ('radishes', 1)],
    'radishes': [('cucumbers', 1), ('carrots', 1)],
    'carrots': [('radishes', 1), ('tomatoes', 1), ('onions', 1)],
    'onions': [('carrots', 1), ('tomatoes', 1)]
}

num_options = 4

optimal_options = select_optimal_coplanting_options(ranked_options, num_options)
print(optimal_options)