import sys
from strtk.utils import parse_region


def str2vcf_main(args):

    if args.region:
        query_chrom, query_start, query_end = parse_region(args.region)
    else:
        query_chrom, query_start, query_end = None, None, None
    O = open(args.out_vcf, "w")
    write_vcf_header(O, args.sample_id)
    with open(args.str_file) as F:
        seq = F.readline().strip()
    with open(args.index_file) as F:
        for i,j in enumerate(F):
            ( index, rsid, chrom, pos, var_type,
            allele1, allele2, ref_base, alt_base) = j.strip().split("\t")
            i = int(index)

            #judge pos in select region or not
            if query_chrom and chrom != query_chrom:
                continue
            pos = int(pos)
            if query_start:
                if query_end:
                    if pos < query_start or pos > query_end:
                        continue
                else:
                    if pos != query_start:
                        continue

            #filter indel
            if args.filter_indel and var_type == "INDEL":
                continue
        
            #determine gt
            genotype = seq[i*2:(i+1)*2]
            gt = []
            if genotype == "--" or genotype == "00":

                # filter nocall
                if args.filter_nocall:
                    continue
                else:
                    gt_s = "./."
            else:
                if var_type == "SNP":
                    for base in genotype:
                        if base == alt_base:
                            gt.append("1") 
                        else:
                            gt.append("0")
                else:
                    for base in genotype:
                        if base == allele2:
                            gt.append("1") 
                        else:
                            gt.append("0")
                gt_s = "/".join(sorted(gt))
            context = "{chrom}\t{pos}\t{rsid}\t{ref}\t{alt}\t.\tPASS\t.\tGT\t{gt_s}\n".format(
                                                            chrom = chrom,
                                                            pos = pos,
                                                            rsid = rsid,
                                                            ref = ref_base,
                                                            alt = alt_base,
                                                            gt_s = gt_s)
            O.write(context)
    O.close()

def write_vcf_header(handle, sample_id):
    VCF_HEADER="""##fileformat=VCFv4.2
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##contig=<ID=1,length=249250621,assembly=b37>
##contig=<ID=2,length=243199373,assembly=b37>
##contig=<ID=3,length=198022430,assembly=b37>
##contig=<ID=4,length=191154276,assembly=b37>
##contig=<ID=5,length=180915260,assembly=b37>
##contig=<ID=6,length=171115067,assembly=b37>
##contig=<ID=7,length=159138663,assembly=b37>
##contig=<ID=8,length=146364022,assembly=b37>
##contig=<ID=9,length=141213431,assembly=b37>
##contig=<ID=10,length=135534747,assembly=b37>
##contig=<ID=11,length=135006516,assembly=b37>
##contig=<ID=12,length=133851895,assembly=b37>
##contig=<ID=13,length=115169878,assembly=b37>
##contig=<ID=14,length=107349540,assembly=b37>
##contig=<ID=15,length=102531392,assembly=b37>
##contig=<ID=16,length=90354753,assembly=b37>
##contig=<ID=17,length=81195210,assembly=b37>
##contig=<ID=18,length=78077248,assembly=b37>
##contig=<ID=19,length=59128983,assembly=b37>
##contig=<ID=20,length=63025520,assembly=b37>
##contig=<ID=21,length=48129895,assembly=b37>
##contig=<ID=22,length=51304566,assembly=b37>
##contig=<ID=X,length=155270560,assembly=b37>
##contig=<ID=Y,length=59373566,assembly=b37>
##contig=<ID=MT,length=16569,assembly=b37>
##contig=<ID=GL000207.1,length=4262,assembly=b37>
##contig=<ID=GL000226.1,length=15008,assembly=b37>
##contig=<ID=GL000229.1,length=19913,assembly=b37>
##contig=<ID=GL000231.1,length=27386,assembly=b37>
##contig=<ID=GL000210.1,length=27682,assembly=b37>
##contig=<ID=GL000239.1,length=33824,assembly=b37>
##contig=<ID=GL000235.1,length=34474,assembly=b37>
##contig=<ID=GL000201.1,length=36148,assembly=b37>
##contig=<ID=GL000247.1,length=36422,assembly=b37>
##contig=<ID=GL000245.1,length=36651,assembly=b37>
##contig=<ID=GL000197.1,length=37175,assembly=b37>
##contig=<ID=GL000203.1,length=37498,assembly=b37>
##contig=<ID=GL000246.1,length=38154,assembly=b37>
##contig=<ID=GL000249.1,length=38502,assembly=b37>
##contig=<ID=GL000196.1,length=38914,assembly=b37>
##contig=<ID=GL000248.1,length=39786,assembly=b37>
##contig=<ID=GL000244.1,length=39929,assembly=b37>
##contig=<ID=GL000238.1,length=39939,assembly=b37>
##contig=<ID=GL000202.1,length=40103,assembly=b37>
##contig=<ID=GL000234.1,length=40531,assembly=b37>
##contig=<ID=GL000232.1,length=40652,assembly=b37>
##contig=<ID=GL000206.1,length=41001,assembly=b37>
##contig=<ID=GL000240.1,length=41933,assembly=b37>
##contig=<ID=GL000236.1,length=41934,assembly=b37>
##contig=<ID=GL000241.1,length=42152,assembly=b37>
##contig=<ID=GL000243.1,length=43341,assembly=b37>
##contig=<ID=GL000242.1,length=43523,assembly=b37>
##contig=<ID=GL000230.1,length=43691,assembly=b37>
##contig=<ID=GL000237.1,length=45867,assembly=b37>
##contig=<ID=GL000233.1,length=45941,assembly=b37>
##contig=<ID=GL000204.1,length=81310,assembly=b37>
##contig=<ID=GL000198.1,length=90085,assembly=b37>
##contig=<ID=GL000208.1,length=92689,assembly=b37>
##contig=<ID=GL000191.1,length=106433,assembly=b37>
##contig=<ID=GL000227.1,length=128374,assembly=b37>
##contig=<ID=GL000228.1,length=129120,assembly=b37>
##contig=<ID=GL000214.1,length=137718,assembly=b37>
##contig=<ID=GL000221.1,length=155397,assembly=b37>
##contig=<ID=GL000209.1,length=159169,assembly=b37>
##contig=<ID=GL000218.1,length=161147,assembly=b37>
##contig=<ID=GL000220.1,length=161802,assembly=b37>
##contig=<ID=GL000213.1,length=164239,assembly=b37>
##contig=<ID=GL000211.1,length=166566,assembly=b37>
##contig=<ID=GL000199.1,length=169874,assembly=b37>
##contig=<ID=GL000217.1,length=172149,assembly=b37>
##contig=<ID=GL000216.1,length=172294,assembly=b37>
##contig=<ID=GL000215.1,length=172545,assembly=b37>
##contig=<ID=GL000205.1,length=174588,assembly=b37>
##contig=<ID=GL000219.1,length=179198,assembly=b37>
##contig=<ID=GL000224.1,length=179693,assembly=b37>
##contig=<ID=GL000223.1,length=180455,assembly=b37>
##contig=<ID=GL000195.1,length=182896,assembly=b37>
##contig=<ID=GL000212.1,length=186858,assembly=b37>
##contig=<ID=GL000222.1,length=186861,assembly=b37>
##contig=<ID=GL000200.1,length=187035,assembly=b37>
##contig=<ID=GL000193.1,length=189789,assembly=b37>
##contig=<ID=GL000194.1,length=191469,assembly=b37>
##contig=<ID=GL000225.1,length=211173,assembly=b37>
##contig=<ID=GL000192.1,length=547496,assembly=b37>
##FILTER=<ID=NO_PASS,Description="filter failure">
"""
    handle.write(VCF_HEADER)
    item_header = "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t%s\n"%(sample_id)
    handle.write(item_header)
