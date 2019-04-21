from Bio import Phylo
import os

script_path = os.path.abspath(__file__)
path_list = script_path.split(os.sep)
script_directory = path_list[0:len(path_list)-1]
rel_path = "Output.nex"
path = "/".join(script_directory) + "/" + rel_path

tree = Phylo.read(path, "nexus")
Phylo.draw(tree)
