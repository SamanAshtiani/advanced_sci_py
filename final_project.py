import numpy as np 
import pandas as pd
import csv
import glob
route = '/Users/saman/Dropbox/systems_biology_projects/unified_data3/'

# test to see how concat with sort=False merges dataframes
test_df1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4], 'col3': [5, 6], 'col4': [7, 8]}, index=['yek', 'dow'])
test_df2 = pd.DataFrame({'col1': ['yek','dow'], 'col2': ['seh','char'], 'col4': ['haft', 'hasht']}, index=['yek', 'dow'])
test_df3 = pd.DataFrame({'col3': ['five', 'six'], 'col1': ['one','two']}, index=['yek', 'dow'])
test_df3
pd.concat([test_df1, test_df2, test_df3], sort=False)

# all normals from gtex and tcga




#getting all files in the directory for normal and putting in n_dict
n_dict = {}
#fp = '../unified_data3/bladder-rsem-fpkm-gtex.txt.gz'   #in order to test the pipeline without looping over all
for fp in sorted(glob.glob('../unified_data3/*[!-t].txt.gz')):
    #print(fp)
    f = fp.split(sep='/')[2]   # use os.path 
    #print(f)
    tissue = f.split(sep='-')[0]
    db = f.split(sep='-')[3]
    db = db.split(sep='.')[0]
    print(db)
    #print(tissue)
    df = tissue+'_n_df' 
    print(df)
    df = pd.read_csv(route+tissue+'-rsem-fpkm-'+db+'.txt.gz', sep='\t', compression='gzip')
    df = df.T
    
    df.sort_values(by='Hugo_Symbol', axis=1, inplace=True)
    new_col_lst = df.loc['Hugo_Symbol'].tolist()
    df.columns = new_col_lst
    
    
    #print(df.shape)
    val = df.shape[0]
    #print(val)
    df.insert(loc=0, column = 'status', value=np.full((val), 'normal'))
    df.insert(loc=0, column = 'tissue', value=np.full((val), tissue))
    n_dict[tissue] = df
    print(df.shape)
    print()
    print()
    
    

print(list(n_dict.keys()))
n_dict['thyroid'].head()


# all tumor samples from TCGA

#getting all files in the directory for tumor and putting in t_dict
t_dict = {}

count = 0
for fp in sorted(glob.glob('../unified_data3/*-t.txt.gz')):
    #print(fp)
    f = fp.split(sep='/')[2]
    #print(f)
    tissue = f.split(sep='-')[0]
    db = f.split(sep='-')[3]
    db = db.split(sep='.')[0]
    print(db)
    #print(tissue)
    df_t = tissue+'_t_df' 
    print(df_t)
    df_t = pd.read_csv(route+tissue+'-rsem-fpkm-'+db+'-t.txt.gz', sep='\t', compression='gzip')
    df_t = df_t.T
    
    
    df_t.sort_values(by='Hugo_Symbol', axis=1, inplace=True)
    new_col_lst = df_t.loc['Hugo_Symbol'].tolist()
    df_t.columns = new_col_lst
    
    #print(df_t.shape)
    val = df_t.shape[0]
    #print(val)
    df_t.insert(loc=0, column = 'status', value=np.full((val), 'cancer'))
    df_t.insert(loc=0, column = 'tissue', value=np.full((val), tissue))
    t_dict[tissue+'_t'] = df_t
    df_t.at[0:2, 0:2] = np.NaN
    #print(df_t[['tissue', 'status']].iloc[[0, 1]])
    print(df_t.iloc[0:2,0:2])
    print()
    print(df_t.head(3))
    print()
    print()
    print()
#    count += 1
#    if count == 3:
#        break
    

#### sorting df by gene_names and renaming column names using gene_names list


#df.sort_index(axis=1)
#df = df.reindex(sorted(df.columns), axis=1)

print(list(t_dict.keys()))
#print(t_dict['brca_t'][3981].iloc[0])

t_dict['brca_t'].head(3)

t_dict['luad_t'].head(3)

test_concat_df = pd.concat([t_dict['brca_t'], t_dict['luad_t'], t_dict['blca_t']], sort=False)
test_concat_df.head()

for i in range(len(test_concat_df['tissue'])):
    #print(i)
    if test_concat_df['tissue'].iloc[i] == 'luad':
        print(test_concat_df['A1BG'].iloc[i])
        break

unified_dic = {**t_dict, **n_dict}
print(len(unified_dic.keys()))
unified_dic.keys()
tissue_lst = list(unified_dic.keys())
print(tissue_lst)

df_lst = ['unified_dic['+"'"+tissue+"'"+']' for tissue in unified_dic.keys()]
df_lst = [df.replace('"', '') for df in df_lst]
df_lst = [df.strip('"') for df in df_lst]
print(df_lst)

####concatenate all dataframes
final_df = pd.concat([unified_dic[tissue] for tissue in tissue_lst], sort=False)



print(final_df.shape)
final_df.head()




sample_names_arr = np.asarray(list(final_df.index))
print(sample_names_arr[:5])
#final_df.insert(loc=0, column = 'sample_names', value=sample_names_arr)
final_df.reset_index(drop=True, inplace=True)  #drop: avoid the old index to be added as a column named 'index'




####didn't work well but inserting and popping of list was awesome:

for i in range(len(final_df['tissue'])):
    #print(i)
    if final_df['tissue'].iloc[i] == 'luad':
        print(final_df['A4GALT'].iloc[i])
        break

final_df.head()

gene_names = final_df.iloc[0].tolist()[3:]
gene_names[0:10]

entrez_id = final_df.iloc[1].tolist()[3:]
entrez_id[0:5]



final_df.drop(final_df.loc[(final_df['sample_names'] == 'Hugo_Symbol') |
                           (final_df['sample_names'] == 'Entrez_Gene_Id')].index, inplace=True)

#also:
#df = df[df.line_race != 0]

#### after dropping two rows, index starts from two,though iloc[0] shows 0th line, index needs reset:
print(final_df['sample_names'].iloc[0])
#final_df.reset_index(drop=True, inplace=True)
final_df.head()


data = final_df.iloc[:, 3:].to_numpy()
print(type(data))
data
final_df.head()

sample_names = final_df['sample_names'].to_numpy()
sample_names[0:5]

sample_status = final_df['status'].to_numpy()
sample_status[-4000:-3990]

sample_tissue = final_df['tissue'].to_numpy()
sample_tissue[-2000:-1990]

# for row in range(df.shape[0]): 
#          for col in range(df.shape[1]):
#              if df.get_value(row,col) == 'security_id':
#                  print(row, col)
#                  break



