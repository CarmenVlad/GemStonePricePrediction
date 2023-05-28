import json,pickle,numpy as np

__locations=None
__data_columns=None
__model=None

def get_estimated_price(carat,cut,color,clarity,depth,table,x,y,z):
    clarity_dict={ 'IF':1, 'VVS1':2, 'VVS2':3, 'VS1':4, 'VS2':5, 'SI1':6, 'SI2':7, 'I1':8} 
    cut_dict={'Fair':1, 'Good':2, 'Very Good':3, 'Premium':4, 'Ideal':5}
    volume=x*y*z
    vect=np.array([])
    vect=np.zeros(len(__data_columns))
    vect[0]=cut_dict[cut]
    vect[1]=clarity_dict[clarity]
    vect[2]=table
    vect[3]=carat/volume
    vect[4]=table*z
    if color!='D':
        index_color=__data_columns.index('color_' + color)
        if index_color>0: 
                vect[index_color]=1
    else:
         vect[5]=vect[6]=vect[7]=vect[8]=vect[9]=vect[10]=0
    return np.round(__model.predict([vect])[0],4)


def load_saved_artifacts():
    print('loading saved artifacts..starting')
    
    global __data_columns
    global __locations
    global __model
    
    with open('./artifacts/gemstone_json_fm','r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations= __data_columns[3:]
    with open('./artifacts/gemstone_pickle_fm','rb') as fp:
        __model=pickle.load(fp)
    
    print('loading saved artifacts...ending')
    
if __name__=='__main__':
    load_saved_artifacts()
    get_location_names()
   
    