from scipy.sparse import load_npz
import pandas as pd
import pickle
import json

anime_list = pd.read_pickle('server/files/anime_list.pickle')
csr_rating_matrix = load_npz('server/files/csr_rating_matrix.npz')

with open('server/files/rating_matrix_anime_id.json') as f:
    anime_id = json.load(f)
with open('server/files/rating_matrix_user_id.json') as f:
    user_id = json.load(f)

rating_matrix_pearson = pd.DataFrame(csr_rating_matrix.toarray(),index=user_id['user_id'],columns=anime_id['anime_id'])

def return_anime_list():
  return list(anime_list['name'].values)

def recommend_pearson(anime,filter):
  try:  
    user_anime = anime_list[anime_list['name']==anime]    
    user_anime_ratings = rating_matrix_pearson[int(user_anime['anime_id'])]  
    correlated_anime = rating_matrix_pearson.corrwith(user_anime_ratings).reset_index().rename(columns={0:'Correlation','index':'anime_id'})
    recommended_anime = pd.merge(correlated_anime,anime_list,on='anime_id',how='left')
    if filter != 'Select all':
      return recommended_anime[recommended_anime['type']==filter].sort_values(by='Correlation',ascending=False).head(21).iloc[1:].drop(columns=['anime_id','rating_count','Correlation','members']).to_dict()
    return recommended_anime.sort_values(by='Correlation',ascending=False).head(21).iloc[1:].drop(columns=['anime_id','rating_count','Correlation','members']).to_dict()
  except:
    return {}


