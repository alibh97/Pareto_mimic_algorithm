
def read_file(name):
    f = open(name, 'r')  # open file
    n = int(f.readline().removeprefix('n '))  # read n = number of vertices
    p = int(f.readline().removeprefix('m '))  # read p = number of paths
    tmax = float(f.readline().removeprefix('tmax '))  # read Tmax = available time budget per path

    nodes = []  # a list to append the nodes(points) in it
    index = 0  # make index for nodes

    for line in f:
        x, y, s = line.split('\t')  # extract x coordinate , y coordinate and score from rest of the lines
        nodes.append([float(x), float(y), int(s), index])  # append nodes to nodes list
        index += 1
    return n, p, tmax, nodes  # return extracted variables


no_nodes, no_paths, Tmax, Points = read_file('p7.4.t.txt')  # extract variables from the file ,
# first is the number of vertices , n
# seconds is the number of paths , m
# Tmax is the available time budget per path
# points is a list of nodes(points) with their x & y coordinates and scores

N = 10  # N is the maximum number of incumbent solutions
integer_parameter = 10  # The integer parameter (γ)
similarity_ratio = 0.95  # similarity ratio ( α )
