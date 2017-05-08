USAGE="Usage: `basename $0` [BUSCO_full_table.tsv] [outfile.bed]"
EXAMPLE="Example: BUSCOfull2BED.sh full_table_myGenome.tsv DuplicatedGenes.bed"

# if no arguments or help statement, print usage
if ! [[ $# == 2 ]]; then
	echo $USAGE
	echo $EXAMPLE
	exit 0
fi

if [ "$1" == "-h" ]; then
	echo $USAGE
	echo $EXAMPLE
	exit 0
fi


IN=$1
OUT=$2


paste <(cut -f3-5 $IN) <(cut -f1-2 $IN ) | grep 'Duplicated' |  cut -f1-4 | sort -k1,1 -k2,2n > $OUT


