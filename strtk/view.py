#!/usr/bin/env python3
#from strtk.utils import load_index_file
from strtk.utils import parse_region
#from utils import parse_region

def view_main(args):
    query_chrom = None
    query_start = None
    query_end = None
    if args.region:
        query_chrom, query_start, query_end = parse_region(args.region)
    query_pos = {}
    if args.pos_file:
        with open(args.pos_file) as F:
            for line in F:
                chrom, pos = line.strip().split("\t")
                query_pos.setdefault(chrom, set()).add(int(pos))

    with open(args.str_file) as F:
        seq = F.readline().strip()
        with open(args.index_file) as F:
            for line in F:
                if line.startswith("#"):
                    continue
                index_info = line.strip().split("\t")
                i = int(index_info[0])
                genotype = seq[i*2:(i+1)*2]

                chrom, pos = index_info[2], int(index_info[3])
                # judge pos is in query region or not 
                if args.region:
                    if query_chrom:
                        #if index_info[2] != query_chrom:
                        if chrom != query_chrom:
                            continue
                        #pos = int(index_info[3]) 
                        if query_start:
                            if query_end:
                                if pos < query_start or pos > query_end:
                                    continue
                            else:
                                if pos != query_start:
                                    continue
                if args.pos_file:
                    if chrom not in query_pos: 
                        continue
                    if pos not in query_pos[chrom]:
                        continue
                print("{}\t{}\t{}".format(i, "\t".join(index_info), genotype))
