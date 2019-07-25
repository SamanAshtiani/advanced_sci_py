import pandas as pd
import numpy as np
import os

ens_go_table = '/mnt/4tb/Dropbox/systems_biology_projects/\
TCGA_exp_from_transcripts_21032019/symbol_mapped_ensemble.txt'
p = '/mnt/4tb/Dropbox/systems_biology_projects/\
TCGA_exp_from_transcripts_21032019/'
genes_fl_path = os.path.join(p, 'genes_fl.txt')
print(genes_fl_path)


ens_go_df = pd.read_table(ens_go_table)
genes_lst = ens_go_df['symbol'].tolist()
print(genes_lst[0:10])


genes_fl = open(genes_fl_path, 'w+')
for g in genes_lst:
    genes_fl.write('%s\n' %g)
genes_fl.close()


ens_go_dic = dict(zip(ens_go_df.ensemble, ens_go_df.symbol))
# ens_go_dic

enst_go_table = 

annot_df = pd.read_csv('GTEx_v7_Annotations_SampleAttributesDS.txt', sep='\t')
print(annot_df.shape)

annot_df.head()
annot_df.groupby('SMTS')['SAMPID'].apply(np.size, axis=0)
annot_dic = annot_df.groupby('SMTS')['SAMPID'].apply(list).to_dict()
#annot_dic['Kidney']
#len([item for item in annot_dic['Kidney'] if item])


# Pathology data
Staining profiles for proteins in human tumor tissue based on immunohistochemisty using tissue micro arrays and log-rank P value for Kaplan-Meier analysis of correlation between mRNA expression level and patient survival. The tab-separated file includes Ensembl gene identifier ("Gene"), gene name ("Gene name"), tumor name ("Cancer"), the number of patients annotated for different staining levels ("High", "Medium", "Low" & "Not detected") and log-rank p values for patient survival and mRNA correlation ("prognostic - favourable", "unprognostic - favourable", "prognostic - unfavourable", "unprognostic - unfavourable"). The data is based on The Human Protein Atlas version 18.1 and Ensembl version 88.38.

import re

# atlas_df = pd.read_csv('proteinatlas.tsv', error_bad_lines=False)  # many lines are skipped
atlas_obj = open('pathology.tsv', 'r')
print(atlas_obj.readline())
last_l = ''
for l in atlas_obj:
    breast_per_l = re.search('breast', l)
    if breast_per_l:
        last_l = l
        ens = re.search('ENSG...........', l)
        if(ens):
            pass
            #print(ens[0])
            
        #exp = re.search()
print(last_l)
    
atlas_obj.close()

pathology_df = pd.read_csv('pathology.tsv', sep='\t')



pathology_df.head()

