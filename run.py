# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ed = search.GPSProblem('E', 'D', search.romania)
eo = search.GPSProblem('E', 'O', search.romania)
tn = search.GPSProblem('T', 'N', search.romania)
rn = search.GPSProblem('R', 'N', search.romania)


print "----------------------Primera iteracion:----------------------------"
print "El camino realizado es: %s \n" % search.problema_ramificacion_y_acotacion(ab).path()
print "El camino realizado es: %s" % search.problema_ramificacion_y_acotacion_conH(ab).path()
print "----------------------Segunda iteracion:----------------------------"
print "El camino realizado es: %s \n" % search.problema_ramificacion_y_acotacion(ed).path()
print "El camino realizado es: %s" % search.problema_ramificacion_y_acotacion_conH(ed).path()
print "----------------------Tercera iteracion:----------------------------"
print "El camino realizado es: %s \n" % search.problema_ramificacion_y_acotacion(eo).path()
print "El camino realizado es: %s" % search.problema_ramificacion_y_acotacion_conH(eo).path()
print "----------------------Cuarta iteracion:----------------------------"
print "El camino realizado es: %s \n" % search.problema_ramificacion_y_acotacion(tn).path()
print "El camino realizado es: %s" % search.problema_ramificacion_y_acotacion_conH(tn).path()
print "----------------------Quinta iteracion:----------------------------"
print "El camino realizado es: %s \n" % search.problema_ramificacion_y_acotacion(rn).path()
print "El camino realizado es: %s" % search.problema_ramificacion_y_acotacion_conH(rn).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
