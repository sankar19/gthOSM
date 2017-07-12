import osmium as o
import sys

class WayFilter(o.SimpleHandler):

    def __init__(self):
        o.SimpleHandler.__init__(self)
        self.nodes = set()

    def way(self, w):
        if 'landuse' in w.tags and w.tags['landuse'] == 'forest':
            for n in w.nodes:
                self.nodes.add(n.ref)


class CoastlineWriter(o.SimpleHandler):

    def __init__(self, writer, nodes):
        o.SimpleHandler.__init__(self)
        self.writer = writer
        self.nodes = nodes

    def node(self, n):
        if n.id in self.nodes:
            self.writer.add_node(n)

    def way(self, w):
        if 'landuse' in w.tags and w.tags['landuse'] == 'forest':
            self.writer.add_way(w)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python filter_coastlines.py <infile> <outfile>")
        sys.exit(-1)


    # go through the ways to find all relevant nodes
    ways = WayFilter()
    ways.apply_file(sys.argv[1])

    # go through the file again and write out the data
    writer = o.SimpleWriter(sys.argv[2])
    CoastlineWriter(writer, ways.nodes).apply_file(sys.argv[1])

    writer.close()

