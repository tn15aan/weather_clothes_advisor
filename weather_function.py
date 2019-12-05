attire = {'sunny': 'take your shorts!',
          'stormy': 'take rain coat',
          'rainy': 'take your umbrella',
          'rainy and stormy': 'stay home'}

#refactoring while loop and exit condition
def weather_attire(weather):
    if weather == 'sunny':
        return attire['sunny']
    elif weather == 'stormy':
        return attire['stormy']
    elif weather == 'rainy':
        return attire['rainy']
    elif weather == 'rainy and stormy':
        return attire['rainy and stormy']
    else:
        return "sorry, i didn't quite catch that"


