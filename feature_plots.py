#%% Imports
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd
import glob

#%% ## Organize data from "/unified-hdf-feature-data" directory, create 4 batchs of 1000 files
data_directory = glob.glob("/domino/datasets/unified-hdf-feature-data/*.hdf5")

#Change these.................................................
batch_size = 2
file_limit = 20

print("Number of Files Loaded:")
batch_number = 1 # ex. batch1
start = 100
current_position = batch_size
batchs = []
for batch in data_directory:
    globals()[f"batch{batch_number}"] = [] # ex. batch1[]
    
    if current_position > file_limit:
        break
    
    # add files to batch
    [globals()[f"batch{batch_number}"].append(file) for file in data_directory[start:current_position]] # ex. batch1[0:1000]

    # add batchs to list
    batchs.append(globals()[f"batch{batch_number}"])# ex. batchs[batch1, batch2]
    
    batch_number+=1
    start+=batch_size
    print(current_position, end=" ")
    current_position+=batch_size

# %% Clean/Prepare Data
# 1. Combine files in batchs[batch1] into 1 DF
# 2. Add "File" column for the range 
# 3. Add all DFs to a list for plotting
# 4. Combine into single DF
print("Batchs Loaded:")
start = 0
all_batchs = []
for batch in batchs:
     # combine files in batchs[batch1] into 1 DF
    df = pd.concat((map(pd.read_hdf, batch)))
    
    # add "File" column for the range 
    df.insert(0, "Files", f"{start}-{start + batch_size}", True ) # ex. [Files][0-1000]
    start+=batch_size
    
    # add all DFs to a list for plotting
    all_batchs.append(df)
    
    print(f"{start - batch_size}-{start}", end=" ") # reverse because batch_size has been incremented
    
# combine into single DF
df = pd.concat(all_batchs)
df = pd.DataFrame(df.reset_index(drop=True))

# %% plotly
# Define the traces
trace0 = df[df['class']=='df1']['heading_participant']
trace1 = df[df['class']=='df2']['heading participant']

# Define a data variable
hist_data = [trace0, trace1]
group_labels = ['df1','df2','heading_participant']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename='heading_participant.html')