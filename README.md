# advanced scientific programming with Python

## a description of the project:

### main goal:
creating a single concatenated dataframe of 5 cancer data types gene expression levels and their corresponding normal gene expression levels using pandas and numpy.

### procedure:
1)Collecting cancerous and non-cancerous 'gene expression levels' in tsv format for 5 different cancer types

2)trimming and cleaning the datasets

3)removing unnecessary columns

4)adding 'normal', 'cancerous', 'cancer type' columns for the future grouping use

5)converting (mapping) ensemble IDs on the Gene Ontology names

6)concatenating all datasets into one final dataframe

7)grouping by first three columns to facilitate access using 'cancer or normal', 'tissue' and 'cancer type'
