import pickle
import sklearn

print('\nMobile price classifier\n')
ram = int(input('Amount of RAM in megabytes: '))
battery_power = int(input('Amount of battery power (mAh): '))
px_width = int(input('Pixel resolution (width - horizontal view): '))
px_height = int(input('Pixel resolution (height - horizontal view): '))
internal_memory = int(input('Internal memory in gigabytes: '))

model = pickle.load(open('model/mobile_price_model.pickle','rb'))
predicted_value = model.predict([[ram,battery_power,px_width,px_height,internal_memory]])
phone_cost = ['low','medium','high','very high']


print('\nPrice cost:',phone_cost[predicted_value[0]])