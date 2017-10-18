import codecs, json, re, networkx as nx
from networkx.drawing import nx_agraph
import pygraphviz as pg

path = '/Users/mayankkejriwal/datasets/memex/rahul-experiments/extraction-graphs/'
def convert_edgelist_graphviz(edge_list=path+'edge_list_city_hr',dot_file=path+'edge_list_city_hr.dot'):
    G = nx.read_edgelist(edge_list, delimiter=' ')
    print G.is_directed()
    nx_agraph.write_dot(G, dot_file)

bible_path = '/Users/mayankkejriwal/datasets/religious-texts/bible/'
# convert_edgelist_graphviz(bible_path+'bible-characters.edgelist',bible_path+'bible-characters.dot')
convert_edgelist_graphviz()