import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

#########
#Page Title
##########

image = Image.open('dna.png')
st.image(image)
st.write("""
         #DNA Nucleotide Count Web App
  ***
         """)
st.caption("This app counts the nucleotide composition of query DNA!")

####---##
# Input a text box
##____#######

st.header("Enter DNA sequence")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input,height=150)
sequence = sequence.splitlines()
sequence = sequence[1:]#skips the sequence first line
sequence = ''.join(sequence) # concatenates list to string

st.write("""  *** """)

st.header("""INPUT (DNA query) """)
sequence

st.header("OUTPUT(DNA Nucleoide COunt)")

st.subheader('1.Print dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ("T",seq.count('T')),
        ('G',seq.count('G')),
        ("C",seq.count('C')),

    ])
    return d

X= DNA_nucleotide_count(sequence)
# X_label = list(X)
# X_values = list(X.values)

X

#######2. print text

st.subheader('2. Print text')
st.write('There are ' +str(X['A']) +'adenin(A)')
st.write('There are ' +str(X['T']) +'thymine(T)')
st.write('There are ' +str(X['G']) +'guanin(G)')
st.write('There are ' +str(X['C']) +'cytosine(C)')


### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
