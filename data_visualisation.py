import matplotlib.pyplot as plt

from store_data import read_humidity_data, read_temperature_data

humidity = read_humidity_data()
temperature = read_temperature_data()

humidity_dates, humidity_values, temperature_dates, temperature_values = [], [], [], []
temperature_labels = ['VERY COLD', 'COLD', 'NORMAL', 'HOT', 'VERY HOT']
humidity_labels = ['LOW', 'MEDUIM', 'HIGH']
temperature_pie_chart_sizes = [0, 0, 0, 0, 0]
humidity_pie_chart_sizes = [0, 0, 0]

for h_row, t_row in zip(humidity, temperature):
    humidity_dates.append(h_row[0])
    humidity_values.append(h_row[3])
    temperature_dates.append(t_row[0])
    temperature_values.append(t_row[3])
    print(t_row[4])
    temperature_pie_chart_sizes[temperature_labels.index(t_row[4])] += 1
    humidity_pie_chart_sizes[humidity_labels.index(h_row[4])] += 1
print(temperature_pie_chart_sizes, humidity_pie_chart_sizes)
fig = plt.figure()
fig.canvas.set_window_title('Dashboard')

plt.subplot("221")
plt.title("temperature data")
plt.xlabel("time")
plt.ylabel("temperature C°")
plt.plot(temperature_dates, temperature_values)

plt.subplot("222")
plt.title("humidity data")
plt.xlabel("time")
plt.ylabel("humidity g/m3")
plt.plot(humidity_dates, humidity_values)

plt.subplot("223")
plt.title("Temperature data by level")
plt.pie(temperature_pie_chart_sizes, labels=temperature_labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')

plt.subplot("224")
plt.title("Humidity data by level")
plt.pie(humidity_pie_chart_sizes, labels=humidity_labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')


plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.get_current_fig_manager().full_screen_toggle()  # fullscreen mode
plt.show()
