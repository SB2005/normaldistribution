import pandas as pd 
import plotly.figure_factory as ff 
import statistics as st 

df = pd.read_csv("data.csv")
#print(df)

height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

h_mean = st.mean(height_list)
h_mode = st.multimode(height_list)
h_median = st.median(height_list)
h_sd = st.stdev(height_list)

print(h_mean)
print(h_median)
print(h_mode)
print(h_sd)

sd_1_s, sd_1_e = h_mean - h_sd, h_mean + h_sd
sd_2_s, sd_2_e = h_mean - 2*h_sd, h_mean + 2*h_sd
sd_3_s, sd_3_e = h_mean - 3*h_sd, h_mean+3*h_sd

h1 = 0
h2 = 0
h3 = 0
for h in height_list:
    if(h>=sd_1_s and h<=sd_1_e):
        h1 = h1 + 1
    if(h>=sd_2_s and h<=sd_2_e):
        h2 = h2 + 1
    if(h>=sd_3_s and h<=sd_3_e):
        h3 = h3 + 1

percent_sd1 = (h1/len(height_list))*100
print(percent_sd1)

percent_sd2 = (h2/len(height_list))*100
print(percent_sd2)

percent_sd3 = (h3/len(height_list))*100
print(percent_sd3)


#graph1 = ff.create_distplot([height_list,weight_list],["height distribution","weight distribution"],show_hist = False)
graph2 = ff.create_distplot([height_list],["height distribution"],show_hist=False)
graph2.show()
#graph1.show()