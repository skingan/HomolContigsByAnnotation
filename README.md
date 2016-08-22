FindSharedGenes
===========

python script to identify genes that are present on multiple contigs


Introduction
============

Genome assemblies of non-inbred diploid individuals may result in the assembly of "homologous contigs", contig pairs that capture homologous genomic regions but are sufficiently divergent from each other as to be assembled independently. This phenomenom often results in a genome length that is longer than expected. Unlike other tools which merge homologous regions based on DNA sequence similarity ([Redundans](http://nar.oxfordjournals.org/content/44/12/e113), [HaploMerger](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3409271/pdf/1581.pdf)), my method uses genome annotation information to identify pairs of homologous contigs. The source of the genome annotation is flexible but I recommend a conservative approach based on identifying conserved core (single-copy) genes using [BUSCO](http://busco.ezlab.org/). Contigs that lack BUSCO genes will be missed by this analysis so adding an transcript-based annotation is more sensitive, but also prone to error due to true gene duplications or ambiguous mapping of transcripts.


User Inputs
===========

At the command line, the user must specify the file paths for the following inputs:

1. BED file containing annotated genes and their gene spans (do not include mRNA, exons etc!).
2. Tab delimited text file with contig IDs and lengths.

Output
===========

Tab delimited text file with the following fields:

1. contigA ID
2. contigB ID
3. contigA length (always the longer contig) 
4. contigB length
5. number of genes shared for contig pair
6. comma-delimited list of shared gene IDs 


Downstream analysis recommendations
===========

A non-redundant list of contigB IDs is a reasonable starting list of contigs that should be flagged as allelic (haplotype) variants. Simply substracting their total length from the genome assembly length may result in a more accurate estimate of genome size.

This approach has been fruitful for PacBio assemblies with contig N50 stats on the order of > 1Mbp. I cannot vouch for its effectiveness on more fragmented NGS-bases assemblies.








