from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n   <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Wind speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '   </body>\n</html>'

    with open('GB_Python\Lections\Lection_04\meteo_station\index.html', 'w') as page:
        page.write(html)
    
    return html

def create_another(data, device = 1):
    t, p, w = data
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n   <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '   <p {}>Wind speed: {} m/s</p>\n'\
        .format(style, w)
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '   </body>\n</html>'

    with open('GB_Python\Lections\Lection_04\meteo_station\index_another.html', 'w') as page:
        page.write(html)
    
    return data