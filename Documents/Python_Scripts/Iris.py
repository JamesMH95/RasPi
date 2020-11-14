import numpy as np

import pandas as pd

from tkinter import Tk
from tkinter import Label
from tkinter import Scale
from tkinter import Button
from tkinter import HORIZONTAL
from tkinter import Text

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as RFC



def plant_iris():
    url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv"
    df = pd.read_csv(url)
    species = df.species.unique().tolist() #keys
    values = [] # values
    count = 0 
    for i in species:
        values.append(count)
        count += 1
    replacement = dict(zip(species,values)) #  change the values in the table from text to numbers. 
    plant_dict = dict(zip(values,species))  # so when it predicts the number value it can also give us the name 

    df = df.replace({"species":replacement})
    
    return df, plant_dict

def popup():
    def brick():
        window.destroy()  # destroys the Window created
    def plant_seed():
        # Populates the row for prediction
        seedling.clear()  # make sure its empty to begin with
        seedling.append(sepal_length.get())
        seedling.append(sepal_width.get())
        seedling.append(petal_length.get())
        seedling.append(petal_width.get())
        return(seedling)
    def another_box():
        def bigger_brick():
            window.destroy()
        window = Tk()
        plantt = let_it_grow(test_row=seedling)
        result_text = Label(window, text="Predicted Plant is: {0}".format(plantt))
        result_text.grid(row=1, column=3)
        rerun_button = Button(text="Re-Run", command=lambda:[bigger_brick(),popup()])
        rerun_button.grid(row=2,column=2)
        exit_button = Button(text="Exit", command=exit)
        exit_button.grid(row=2, column=4)
        window.mainloop()
        
    seedling = []
    
    window = Tk()
    
    sepal_length = Scale(label = "Sepal Length", from_ = 0.1, to = 8, resolution = 0.1, orient = HORIZONTAL)
    sepal_length.grid(row=1,column=3)
    
    sepal_width = Scale(label="Sepal Width", from_= 0.1, to = 8, resolution = 0.1, orient = HORIZONTAL)
    sepal_width.grid(row=2,column=3)
    
    petal_length = Scale(label="Petal Length", from_= 0.1, to = 8, resolution = 0.1, orient = HORIZONTAL)
    petal_length.grid(row=3,column=3)
    
    petal_width = Scale(label="Petal Width", from_= 0.1, to = 8, resolution = 0.1, orient = HORIZONTAL)
    petal_width.grid(row=4,column=3)
    
    run_button = Button(text = "Run!", command=lambda:[plant_seed(),brick(), another_box()]) # get the test row, destroy the window, run rf model, reopen the tkinter box
    run_button.grid(row=5,column=3)
    
    window.mainloop()
    return seedling

def let_it_grow(test_row):
    """ 
    This is the "brain" it works out which plant you have decribed in
    the input through TKinter (the sliders in the popup)
    It was created based of the example here 
    https://www.kaggle.com/tcvieira/simple-random-forest-iris-dataset
    """
    iris, plant_dict = plant_iris() # for use wth pandas df
    
    X_data = iris[["sepal_length","sepal_width",\
                   "petal_length","petal_width"]]
    Y_data = iris[["species"]]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.1)
    
    gausian_classifier = RFC(n_estimators=100)
    gausian_classifier.fit(X_train,Y_train.values.ravel())
    Y_pred = gausian_classifier.predict(X_test)
    
    # Accuracy of the model based on the test / train split 
    #print("Accuracy: ",metrics.accuracy_score(Y_test,Y_pred))
    
    # this is where the prediction happens    
    species_idx = gausian_classifier.predict([test_row])[0]
    #print(test_row)
    plant = plant_dict.get(species_idx)
    #print(plant)
    
    return plant

if __name__ == "__main__":
    popup()
