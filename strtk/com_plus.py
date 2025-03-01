#!/usr/bin/env python

import sys

def read_genotype(str_file, index_file, var_type="ALL", key="rsid"):
    genotype_dict = {}
    with open(str_file) as F:
        seq = F.readline().strip()
    n = 0
    with open(index_file) as F:
        for i in F:
            if i.startswith("#"):
                continue
            genotype = "".join(sorted(seq[2*n:2*(n+1)]))
            n+=1
            feilds = i.strip().split("\t")
            if feilds[4] != var_type and var_type != "ALL":
                continue
            if key == "rsid":
                k = feilds[1]
            else:
                k = (feilds[2], feilds[3])
            genotype_dict[k] = genotype
    return genotype_dict

def com_plus_main(args):
    genotype_dict_1 = read_genotype(args.str_file1, args.index1,
                                    var_type=args.var_type, key=args.key)
    genotype_dict_2 = read_genotype(args.str_file2, args.index2,
                                    var_type=args.var_type, key=args.key)

    limit_set = set()
    if args.limit_set:
        with open(args.limit_set) as F:
            for i in F:
                limit_set.add(i.strip())

    n = 0
    s_n = 0
    het_n_1 = 0
    het_n_2 = 0
    for k,geno1 in genotype_dict_1.items():
        if limit_set and (k not in limit_set):
            continue
        if k not in genotype_dict_2:
            continue
        geno2 = genotype_dict_2[k]
        if geno1 == "--" or geno2 == "--":
            continue
        n += 1
        if geno1 == geno2:
            s_n += 1
        else:
            if geno1[0] != geno1[1]:
                het_n_1 += 1
            if geno2[0] != geno2[1]:
                het_n_2 += 1
            print(f"#{k}\t{geno1}\t{geno2}")
            
    r = s_n/n if n != 0 else 0
    print("{}\t{}\t{}\t{}\t{}".format(n, s_n, r, het_n_1/(n-s_n), het_n_2/(n-s_n) ))

