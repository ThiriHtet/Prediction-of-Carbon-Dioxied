import tkinter as tk
import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score


root= tk.Tk()
canvas1 = tk.Canvas(root, width = 600, height = 500,  relief = 'raised')
canvas1.pack()

#******************Reading and printing Datasets****************************

dataset = pandas.read_csv("carcpy.csv")
X = dataset [["Volume","Weight","Power"]]
Y = dataset ["GSG"]

#****************** Feature Scaling ****************************

scale = StandardScaler()
scaleX = scale.fit_transform(X) 
#****************** Fitting Linear Regression to the datasets **************************

reg = linear_model.LinearRegression()
reg.fit(scaleX,Y)

#*********************visualization***********************
def VisualVol():
    import VisualizationVolume 
    VisualizationVolume.VisualV()
def VisualWig():
    import VisualizationWeight 
    VisualizationWeight.visualW()
def VisualEnginePow():
    import VisualizationEnginePower 
    VisualizationEnginePower.visualP()
    
buttVisual = tk.Button(text='Click to Visualize \n Car Cylinder Volume',command=VisualVol, bg='red',relief = 'raised', fg='black', font=('helvetica', 11, 'bold'))
canvas1.create_window(160, 330, window=buttVisual)

buttVisual1 = tk.Button(text='Click to Visualize \n Car Weight', command=VisualWig, bg='Green', fg='black', font=('helvetica', 11, 'bold'))
canvas1.create_window(330, 330, window=buttVisual1)

buttVisual2 = tk.Button(text='Click to Visualize \n Enginer Power', command=VisualEnginePow, bg='blue', fg='black', font=('helvetica', 11, 'bold'))
canvas1.create_window(480, 330, window=buttVisual2)

#************************Finding the mean value of Cylinder Volume *************************************
def mean():
    volume = dataset.Volume
    summy = 0
    for i in volume:
        summy += i 
    mean_of_volume = summy/len(volume)
    return mean_of_volume
meanVolume = mean()

#***************************User interface and Getting user input****************************
# photoBg= PhotoImage(file=' C:\Users\DELL\Desktop\car\mickey_mouse.png ')
# my_label = tk.Label(root,image=photoBg)
# my_label.config(width=600,height=500)
# canvas1.create_window(0,0,window=my_label)
#***************photo background testing*********************
label1 = tk.Label(root, text='Predict the Greenhouse Gas')
label1.config(font=('helvetica', 16))
canvas1.create_window(300, 25, window=label1)

label2 = tk.Label(root, text='Enter car weight:')
label2.config(font=('helvetica', 11))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(350, 100, window=entry1)

unit1 = tk.Label(root, text='Kilogram')
unit1.config(font=('helvetica', 11))
canvas1.create_window(450, 100, window=unit1)

def on_button():
    
    if int(entry1.get()) < 790 or int(entry1.get()) > 2200: #corrected
        label3= tk.Label(root, text='Enter car volume:')
        label3.config(font=('helvetica', 11))
        canvas1.create_window(200, 180, window=label3)
        entry2=tk.Entry(root)
        canvas1.create_window(350, 180, window=entry2)
        unit2 = tk.Label(root, text='Centimeter cube')
        unit2.config(font=('helvetica', 11))
        canvas1.create_window(480, 180, window=unit2)
        def enter2():
            global CarVolume
            CarVolume=int(entry2.get())
            label4 = tk.Label(root, text='Enter car Engine Power:')
            label4.config(font=('helvetica', 11))
            canvas1.create_window(170, 260, window=label4)
            entry3 = tk.Entry (root) 
            canvas1.create_window(350, 260, window=entry3)
            unit3 = tk.Label(root, text='Kilowatt')
            unit3.config(font=('helvetica', 11))
            canvas1.create_window(450, 260, window=unit3)
        
            def preDict():
#************************* Predicting the result **************************************
                CarWeight = int(entry1.get())

                CarEngiePower = int(entry3.get())
            
                prediction = scale.transform([[CarWeight,CarVolume,CarEngiePower]])
                ans = reg.predict(prediction)
                answer = int(ans)
                ansBtn= tk.Button(root, text=f'The resulting Greenhouse Gas is : {answer} g/km',bg= 'Green',fg = 'white',font=('helvetica', 11))
                canvas1.create_window(300,460, window=ansBtn)
                def restart():
                    button.destroy()
                    entry1.delete(first=0,last=30)
                    unit2.destroy()
                    unit3.destroy()
                    label3.destroy()
                    label4.destroy()
                    ansBtn.destroy()
                    entry2.destroy()
                    entry3.destroy()
                restartBtn = tk.Button(root, text="Restart", command=restart,font=('helvetica', 11, 'bold'))
                canvas1.create_window(400,400, window=restartBtn)
            button1 = tk.Button(text='Predict', command=preDict, bg='aqua', fg='black', font=('helvetica', 11, 'bold'))
            canvas1.create_window(270, 400, window=button1)
        button = tk.Button(root, text="Enter", command=enter2,font=('helvetica', 11, 'bold'))
        canvas1.create_window(300,220, window=button)
            
        
                
    else:
        BtnVol = tk.Button(text=f'The appropriate Car Cylinder Volume can be {meanVolume}', bg='black', fg='white', font=('helvetica', 11, 'bold') )
        canvas1.create_window(280, 200, window=BtnVol)
        label4 = tk.Label(root, text='Enter car Engine Power:')
        label4.config(font=('helvetica', 11))
        canvas1.create_window(170, 260, window=label4)
        entry3 = tk.Entry (root) 
        canvas1.create_window(350, 260, window=entry3)
        unit3 = tk.Label(root, text='Kilowatt')
        unit3.config(font=('helvetica', 11))
        canvas1.create_window(450, 260, window=unit3)
        def preDict():
            
            CarWeight = int(entry1.get())
            CarVolume = int(meanVolume)
            CarEngiePower = int(entry3.get())
            
            prediction = scale.transform([[CarWeight,CarVolume,CarEngiePower]])
            ans = reg.predict(prediction)
            answer = int(ans)
            ansBtn= tk.Button(root, text=f'The resulting Greenhouse Gas is : {answer} g/km',bg= 'Green',fg = 'white',font=('helvetica', 11))
            canvas1.create_window(300,460, window=ansBtn)
            def restart():
                entry1.delete(first=0,last=30)
                BtnVol.destroy()
                unit3.destroy()
                label4.destroy()
                ansBtn.destroy()
                entry3.destroy()    
            restartBtn = tk.Button(root, text="Restart", command=restart,font=('helvetica', 11, 'bold'))
            canvas1.create_window(400,400, window=restartBtn)    
        button2 = tk.Button(text='Predict', command=preDict, bg='aqua', fg='black', font=('helvetica', 11, 'bold'))
        canvas1.create_window(270, 400, window=button2)

button = tk.Button(root, text="Go to System", command=on_button,font=('helvetica', 11, 'bold'))
canvas1.create_window(330,140, window=button)

def master_destroy():
     root.destroy() 

b_quit_destroy=tk.Button( text="Quit", command=master_destroy,font=('helvetica',11,'bold'))
canvas1.create_window(330, 400, window=b_quit_destroy)

Ypred = reg.predict(scaleX)
print(f'the score is :',reg.score(scaleX,Y))
# print(f'the accuracy score is:',accuracy_score(Y,Ypred))
print(f'the mean square error is :',mean_squared_error(Y,Ypred))

root.mainloop()



