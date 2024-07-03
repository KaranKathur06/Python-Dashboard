import streamlit as st 
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
import datetime
import plotly.figure_factory as ff

st.set_page_config(page_title="SUPERSTORE!!" , page_icon=":bar_chart:" , layout="wide")
st.title(" :bar_chart: Super Store Dataset")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)


os.chdir(r"C:\\STUDY\\PROGRAMS\\PYTHON\\DMDW_Project")   
df = pd.read_csv("SuperStoreDataSet.csv", encoding="ISO-8859-1")


col1,col2 = st.columns((2)) 
df["Order Date"] = pd.to_datetime(df["Order Date"])

#GETTING THE MIN AND MAX DATE
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()


with col1:
    date1 = pd.to_datetime(st.date_input("STARTING DATE", startDate))


with col2:
    date2 = pd.to_datetime(st.date_input("ENDING DATE", endDate))

df = df[(df["Order Date"]>=date1) & (df["Order Date"]<=date2)].copy()                          



#CREATE FOR REGION
st.sidebar.header("CHOOSE YOUR FILTER: ")
region = st.sidebar.multiselect("CHOOSE YOU REGION",df["Region"].unique())

if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]


#CREATE FOR STATE
state = st.sidebar.multiselect("CHOOSE YOUR STATE" ,df2["State"].unique())

if not state:
    df3 = df2.copy()
else:
    df3=df[df["State"].isin(state)]

#CREATE FOR CITY
city = st.sidebar.multiselect("CHOOSE YOUR CITY" ,df2["City"].unique())

#FILTER THE DATA BASED ON REGION, STATE AND CITY

if not region and not state and not city:
    filtered_df = df 
elif not state and not city:
    filtereddf = df[df["Region"].isin(region)]
    
elif not region and not state:
    filtered_df = df[df["State"].isin(state)]
elif state and city:
    filtered_df = df3[df["State"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df = df3[df["Region"].isin(region) & df3["City"].isin(city)]    
elif region & state:
    filtered_df = df3[df["Region"].isin(region) & df3["State"].isin(state)]    
elif city:
    filtered_df = df3[df3["City"].isin(city)]
else:
    filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df["City"].isin(city)] 

category_df =filtered_df.groupby(by=["Category"],as_index =False )["Sales"].sum()

with col1:
    st.subheader("SALES BY CATEGORY")
    fig = px.bar(category_df, x = "Category", y = "Sales", text = ['${:,.2f}'.format(x) for x in category_df["Sales"]],
                 template = "seaborn")
    st.plotly_chart(fig,use_container_width=True, height = 200)

with col2:
    st.subheader("SALES BY REGION")
    fig = px.pie(filtered_df, values = "Sales", names = "Region", hole = 0.5)
    fig.update_traces(text = filtered_df["Region"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)
    
cl1, cl2 = st.columns((2))
with cl1:
    with st.expander("CATEGORY VIEWDATA"):
        st.write(category_df.style.background_gradient(cmap="Blues"))
        csv = category_df.to_csv(index = False).encode('utf-8')
        st.download_button("DOWNLOAD DATAFILE", data = csv, file_name = "Category.csv", mime = "text/csv", help = 'CLICK HERE TO DOWNLOAD CSV FILE')

with cl2:
    with st.expander("REGION VIEWDATA"):
        region = filtered_df.groupby(by = "Region", as_index = False)["Sales"].sum()
        st.write(region.style.background_gradient(cmap="Oranges"))
        csv = region.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Region.csv", mime = "text/csv",help = 'CLICK HERE TO DOWNLOAD CSV FILE')



filtered_df["MONTH YEAR"] = filtered_df["Order Date"].dt.to_period("M")
st.subheader('TIME SERIES ANALYSIS')

linechart = pd.DataFrame(filtered_df.groupby(filtered_df["MONTH YEAR"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x = "MONTH YEAR", y="Sales", labels = {"Sales": "Amount"},height=500, width = 1000,template="gridon")
st.plotly_chart(fig2,use_container_width=True)

with st.expander("VIEW DATA OF TIME SALES:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('DOWNLOAD DATA', data = csv, file_name = "TimeSeries.csv", mime ='text/csv')



st.subheader("HIERARCHICAL VIEW OF SALES USING TREEMAP")
fig3 = px.treemap(filtered_df, path = ["Region","Category","Sub-Category"], values = "Sales",hover_data = ["Sales"],
                  color = "Sub-Category")
fig3.update_layout(width = 800, height = 650)
st.plotly_chart(fig3, use_container_width=True)



chart1, chart2 = st.columns((2))
with chart1:
    st.subheader('SEGMENT WISE SALES')
    fig = px.pie(filtered_df, values = "Sales", names = "Segment", template = "plotly_dark")
    fig.update_traces(text = filtered_df["Segment"], textposition = "inside")
    st.plotly_chart(fig,use_container_width=True)

with chart2:
    st.subheader('CATEGORY WISE SALES')
    fig = px.pie(filtered_df, values = "Sales", names = "Category", template = "gridon")
    fig.update_traces(text = filtered_df["Category"], textposition = "inside")
    st.plotly_chart(fig,use_container_width=True)


st.subheader(":point_right: MONTH WISE SUB-CATEGORY SALES SUMMARY")
with st.expander("SUMMERY TABLE"):
    df_sample = df[0:5][["Region","State","City","Category","Sales","Profit","Quantity"]]
    fig = ff.create_table(df_sample, colorscale = "Cividis")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("MONTH WISE SUB-CATEGORY TABLE")
    filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    sub_category_Year = pd.pivot_table(data = filtered_df, values = "Sales", index = ["Sub-Category"],columns = "month")
    st.write(sub_category_Year.style.background_gradient(cmap="Blues"))


#CREATE A SCATTER PLOT
data1 = px.scatter(filtered_df, x = "Sales", y = "Profit", size = "Quantity")
data1['layout'].update(title="RALATIONSHIP BETWEEN SALES AND PROFITS USING SCATTER PLOT!!",
                       titlefont = dict(size=20),xaxis = dict(title="Sales",titlefont=dict(size=19)),
                       yaxis = dict(title = "Profit", titlefont = dict(size=19)))
st.plotly_chart(data1,use_container_width=True)

with st.expander("View Data"):
    st.write(filtered_df.iloc[:500,1:20:2].style.background_gradient(cmap="Oranges"))

#DOWNLOAD ORIGINAL DATASET
csv = df.to_csv(index = False).encode('utf-8')
st.download_button('DOWNLOAD THE DATA', data = csv, file_name = "Data.csv",mime = "text/csv")   