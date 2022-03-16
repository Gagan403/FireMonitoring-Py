import geocoder
import folium
import webbrowser
def map1():

    g = geocoder.ip('me')
    print( g.latlng)

    my_address = 12.933972,77.692192
    print(my_address)
    map1=folium.Map(location=my_address)


    folium.CircleMarker(location=my_address).add_to(map1)
    map1.save("map.html")
    webbrowser.open('http://localhost:63342/5thminiproject/map.html?_ijt=535e9605pvlitalnlgphds40kd')



