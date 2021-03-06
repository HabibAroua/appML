#from dijkstra.Vertex import Vertex;
#from dijkstra.Edge import Edge;
#from dijkstra.Algorithm import Algorithm;
import sys
sys.path.append('Edge.py')
sys.path.append('Vertex.py')
sys.path.append('Algorithm.py')

node1=Vertex("A");
node2=Vertex("B");
node3=Vertex("C");

edge1=Edge(1,node1,node2);
edge2=Edge(1,node2,node3);
edge3=Edge(10,node1,node3);

node1.adjacenciesList.append(edge1);
node1.adjacenciesList.append(edge2);
node2.adjacenciesList.append(edge3);

vertextList = {node1 , node2 , node3}

algorithm=Algorithm();
algorithm.calculateShortestPath(vertextList,node1);
algorithm.getShortestPathTo(node3);