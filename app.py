import streamlit as st

st.set_page_config(page_title="Route Optimization For Bus Fleet", page_icon=":tada:", layout="wide")

st.subheader("Route Optimization For Bus Fleet")
st.title("Select a name from the given box below")

option = st.selectbox(
     'Who would you like to be contacted?',
     ('Prabhath','Likhit','Tharun', 'Reddy','Chandu','Venkatesh','Sharath','Nandini','Tulasi','Nikhil', 'Niketh','Bhagiradh','Mani','Eshwar','Ujwhal','Sashank','Deepak'),)

st.write('You selected:', option)
data={
    0:'Prabhath',
    1:'Likhit',
    2:'Tharun', 
    3:'Reddy',
    4:'Chandu',
    5:'Venkatesh',
    6:'Sharath',
    7:'Nandini',
    8:'Tulasi',
    9:'Nikhil', 
    10:'Niketh',
    14:'Bhagiradh',
    11:'Mani',
    12:'Eshwar',
    13:'Ujwhal',
    15:'Sashank',
    16:'Deepak'
}
arr1 = [0, 5, 7, 1, 4, 3, 15, 11, 12]
arr2 = [0, 9, 8, 6, 2, 10, 16, 14, 13]
# i=1
# for key, value in data.items():
#     if option == value:
#         i=key
#     if (i in arr1):
#         text = ''
#         for i in arr1:
#             text+='->'+data[i]
#     else:
#         text = ''
#         for i in arr2:
#             text+='->'+data[i]
#     st.subheader('Your Bus Route Order')
#     st.subheader(text)


st.subheader('Path Of the Bus')
names1=[]
names2=[]
for i in arr1:
    names1.append(data[i])
for i in arr2:
    names2.append(data[i])


if option in names1:
    text = ''
    for i in names1:
        text +='->'+i
    st.text(text)
else:
    text = ''
    for i in names2[1:]:
        text+='->'+i
    st.text(text)



