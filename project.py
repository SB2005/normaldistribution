import pandas as pd
import statistics as st 
import plotly.figure_factory as ff 

df = pd.read_csv("StudentsPerformance.csv")

#print(df)

reading_list = df["reading score"].tolist()

r_mean = st.mean(reading_list)
r_mode = st.multimode(reading_list)
r_median = st.median(reading_list)
r_sd = st.stdev(reading_list)

print(r_mean, r_mode, r_median, r_sd)


sd_1_s, sd_1_e = r_mean - r_sd, r_mean + r_sd
sd_2_s, sd_2_e = r_mean - 2*r_sd, r_mean + 2*r_sd
sd_3_s, sd_3_e = r_mean - 3*r_sd, r_mean+3*r_sd

h1 = 0
h2 = 0
h3 = 0
for h in reading_list:
    if(h>=sd_1_s and h<=sd_1_e):
        h1 = h1 + 1
    if(h>=sd_2_s and h<=sd_2_e):
        h2 = h2 + 1
    if(h>=sd_3_s and h<=sd_3_e):
        h3 = h3 + 1

percent_sd1 = (h1/len(reading_list))*100
print(percent_sd1)

percent_sd2 = (h2/len(reading_list))*100
print(percent_sd2)

percent_sd3 = (h3/len(reading_list))*100
print(percent_sd3)

graph = ff.create_distplot([reading_list],["reading marks distribution"],show_hist=False)
graph.show()