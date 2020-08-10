from image_match.goldberg import ImageSignature
gis = ImageSignature()
import os
import pandas as pd


directory_list = os.listdir('test')

k =1


while k < len(directory_list):
    file = 'test/{}'.format(directory_list[k])
    gis.generate_signature(file)
    k = k + 1


def generate_signatures(directory):
    k =0

    differences = []
    while k < len(checks):
        file = '{}/{}'.format(directory, checks[k])
        foregrounds = []
        foreground = gis.generate_signature(file)
        foregrounds.append(foreground)
        k = k+1
    signatures = pd.DataFrame(data=[directory_list,foregrounds]).T
    signature.to_csv('')
    return signatures


def background_checker(backgrounds, checks,directory):
    k =0

    differences = []
    while k < len(checks):
        file = '{}/{}'.format(directory, checks[k])
        foregrounds = []
        foreground = gis.generate_signature(file)
        foregrounds.append(foreground)
        x = []
        m = 0
        while m < len(backgrounds):
            file = '{}/{}'.format(directory, backgrounds[m])
            background = gis.generate_signature(file)
            difference = gis.normalized_distance(background,foreground)
            x.append(difference)
            m = m +1
        difference = min(x)
        #print('Image: {}'.format(checks[k]))
        #print('Difference: {}'.format(difference))
        differences.append(difference)
        k = k + 1
    order = pd.DataFrame(data=[directory_list,differences]).T


    order = order.sort_values(1,ascending=False)
    return order


directory_list = os.listdir('test')
known_backgrounds = ['DSCF0316.JPG']#,'DSCF0002.JPG','DSCF0305.JPG','DSCF0288.JPG']
order = background_checker(known_backgrounds,directory_list,'test')

print(order)
