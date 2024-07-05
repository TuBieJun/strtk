#encoding:utf-8
#!/usr/bin/env python

import sys
import argparse
from strtk.view import view_main
from strtk.stats import stats_main
from strtk.com import com_main
from strtk.com_plus import com_plus_main
from strtk.str2vcf import str2vcf_main
from strtk.version import __version__, __author__


def main():
    top_desc = """
    Tools for seq string file.
    version: {}
    author: {}
    """.format(__version__, __author__)
    parser = argparse.ArgumentParser(description=top_desc)
    subparsers = parser.add_subparsers()

    #view
    view_parser = subparsers.add_parser("view", help="view seq in specific region")
    view_parser.add_argument("-s", "--str_file", required=True, help="the input string file path", metavar="")
    view_parser.add_argument("-r", "--region", help="the region or the pos to view chr|chr:pos|chr:start-end", metavar="")
    view_parser.add_argument("-i", "--index_file", required=True, help="the index file", metavar="")
    view_parser.set_defaults(func=view_main)

    #stats
    stats_parser = subparsers.add_parser("stats", help="stats seq to get call ratio, het ratio...")
    stats_parser.add_argument("-s", "--str_file", required=True, help="the input string file path", metavar="")
    stats_parser.add_argument("-r", "--region", required=False, help="the region or the pos to stats chr|chr:pos|chr:start-end", metavar="")
    stats_parser.add_argument("-i", "--index_file", required=False, help="the index file. if -r specified, the argument should be provided", metavar="")
    stats_parser.set_defaults(func=stats_main)

    #compare two str file
    com_parser = subparsers.add_parser("com", help="compare two str seq file")
    com_parser.add_argument("-s1", "--str_file1", required=True, help="the input string file path", metavar="")
    com_parser.add_argument("-s2", "--str_file2", required=True, help="the other input string file path", metavar="")
    com_parser.add_argument("-f", "--filter_indel", action="store_true", help="filter indels, only compare snp, default is False", default=False)
    com_parser.add_argument("-r", "--region", required=False, help="the region or the pos to com chr|chr:pos|chr:start-end", metavar="")
    com_parser.add_argument("-i", "--index_file", required=False, help="the index file. if -r specified, the argument should be provided", metavar="")
    com_parser.set_defaults(func=com_main)

    #str2vcf
    str2vcf_parser = subparsers.add_parser("str2vcf", help="trans str file to vcf file")
    str2vcf_parser.add_argument("-s", "--str_file", required=True, help="the input string file path", metavar="")
    str2vcf_parser.add_argument("-f", "--filter_indel", action="store_true", help="filter indels, only compare snp, default is False", default=False)
    str2vcf_parser.add_argument("-n", "--filter_nocall", action="store_true", help="filter nocalls, default is False(gt=./.)", default=False)
    str2vcf_parser.add_argument("-r", "--region", required=False, help="the region or the pos to str2vcf chr|chr:pos|chr:start-end", metavar="")
    str2vcf_parser.add_argument("-i", "--index_file", required=False, help="the index file. if -r specified, the argument should be provided", metavar="")
    str2vcf_parser.add_argument("-o", "--out_vcf", required=True, help="the output vcf file path", metavar="")
    str2vcf_parser.add_argument("-I", "--sample_id", required=True, help="the sample id of output vcf file", metavar="")
    str2vcf_parser.set_defaults(func=str2vcf_main)

    #compare two str file with diff length
    com_plus_parser = subparsers.add_parser("com_plus", help="compare two str seq file, support diff length")
    com_plus_parser.add_argument("-s1", "--str_file1", required=True, help="the input string file path", metavar="")
    com_plus_parser.add_argument("-s2", "--str_file2", required=True, help="the other input string file path", metavar="")
    com_plus_parser.add_argument("-i1", "--index1", required=True, help="the index file of str file 1", metavar="")
    com_plus_parser.add_argument("-i2", "--index2", required=True, help="the index file of str file 2", metavar="")
    com_plus_parser.add_argument("-v", "--var_type", required=False, help="the var type to compare, can be SNP/INDEL/ALL,default is SNP", choices=["SNP", "INDEL", "ALL"], default="SNP", metavar="")
    com_plus_parser.add_argument("-k", "--key", required=False, help="the key to compare a var, can be rsid/pos, default is pos", choices=["rsid", "pos"], default="rsid", metavar="")
    com_plus_parser.add_argument("-l", "--limit_set", required=False, help="the limit pos set to compare", metavar="")
    com_plus_parser.set_defaults(func=com_plus_main)
    argslist = sys.argv[1:]
    if len(argslist) < 1:
        parser.print_help()
        sys.exit(1)
    else:
        args = parser.parse_args(argslist)
        args.func(args)
    


if __name__ == "__main__":
    main()
