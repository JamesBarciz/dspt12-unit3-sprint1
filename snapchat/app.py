from geofence import Edge, Vertex, GeoFence
import datetime


nw_corner_manhattan = Edge(40.815, -73.959)
ne_corner_manhattan = Edge(40.799, -73.900)
sw_corner_manhattan = Edge(40.714, -74.015)
se_corner_manhattan = Edge(40.708, -74.001)

north = Vertex(ne_corner_manhattan, nw_corner_manhattan)
west = Vertex(nw_corner_manhattan, sw_corner_manhattan)
south = Vertex(sw_corner_manhattan, se_corner_manhattan)
east = Vertex(se_corner_manhattan, ne_corner_manhattan)

manhattan_geofence_nye_promotion = GeoFence(
    vertices=[north, west, south, east], lifetime=datetime.timedelta(hours=24)
)

print(
    [
        (e.latitude, e.longitude)
        for v in manhattan_geofence_nye_promotion.vertices
        for e in [v.edge1, v.edge2]
    ]
)
print(north.length())

ne_corner_manhattan.latitude = 40.847
ne_corner_manhattan.longitude = -73.886

print(
    [
        (e.latitude, e.longitude)
        for v in manhattan_geofence_nye_promotion.vertices
        for e in [v.edge1, v.edge2]
    ]
)
print(north.length())
