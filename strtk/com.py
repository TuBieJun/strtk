import sys
from strtk.utils import load_index_file
from strtk.utils import parse_region

def com_main(args):
    if args.region:
        if not args.index_file:
            print("if region(-r) be specified, index_file(-i) should be provied")
            sys.exit(2)
        query_chrom, query_start, query_end = parse_region(args.region)
        index_info_dict = load_index_file(args.index_file)
    
    count_number = 0
    consistent_number = 0
    with open(args.str_file1) as F1, open(args.str_file2) as F2:
        seq1 = F1.readline().strip()
        seq2 = F2.readline().strip()
        if len(seq1) != len(seq2):
            print("the size of input str_files is different", file=sys.stderr)
            sys.exit(3)

        for i in range(int(len(seq1)/2)):
            # judge pos is in query region or not 
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
            genotype_1 = seq1[i*2:(i+1)*2]
            genotype_2 = seq2[i*2:(i+1)*2]

            #filter no call and indels
            filter_base_set = set(["--", "00"])
            if args.filter_indel:
                filter_base_set.add("II")
                filter_base_set.add("ID")
                filter_base_set.add("DI")
                filter_base_set.add("DD")
            if genotype_1 in filter_base_set or genotype_2 in filter_base_set:
                continue
            count_number += 1
            if sorted(genotype_1) == sorted(genotype_2):
                consistent_number += 1
    print("#count_number\tconsistent_number\tconsistency")
    print("{}\t{}\t{}".format(count_number, consistent_number, consistent_number/count_number))

        
                