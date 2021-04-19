import sys
from utils import parse_region
from utils import load_index_file

def stats_main(args):
    if args.region:
        if not args.index_file:
            print("if region(-r) be specified, index_file(-i) should be provied")
            sys.exit(2)
        query_chrom, query_start, query_end = parse_region(args.region)
        index_info_dict = load_index_file(args.index_file)
    
    called_number = 0
    all_number = 0
    het_number = 0

    with open(args.str_file) as F:
        seq = F.readline().strip()
        for i in range(int(len(seq)/2)):
            genotype = seq[i*2:(i+1)*2]
            if args.region:
                index_info = index_info_dict[i]
                if index_info[1] != query_chrom:
                    continue
                pos = int(index_info[2]) 
                if query_start:
                    if query_end:
                        if pos < query_start or pos > query_end:
                            continue
                    else:
                        if pos != query_start:
                            continue
            all_number += 1
            if genotype == "--" or genotype == "00":
                continue
            else:
                called_number += 1
                if genotype[0] != genotype[1]:
                    het_number += 1
    print("#all_pos_number\tcalled_pos_number\tcalled_ratio\thet_number\thet_ratio")
    print("{}\t{}\t{}\t{}\t{}".format(all_number, called_number, 
                                      called_number/all_number,
                                      het_number, het_number/called_number))