import sys

def load_index_file(index_file):
    d = {}
    with open(index_file) as F:
        for i in F:
            if not i.startswith("#"):
                items = i.strip().split("\t")
                d[int(items[0])] = items[1:]
    return d

def parse_region(region):
    try:
        items = region.split(":")
        chrom = items[0]
        start = None
        end = None
        if len(items) > 1:
            pos_l = items[1].split("-")
            start = int(pos_l[0])
            if len(pos_l) > 1:
                end = int(pos_l[1]) 
        return chrom, start, end
    except:
        print("the region %s is unsupport region format"%(region), file=sys.stderr)
        sys.exit(1)
    
