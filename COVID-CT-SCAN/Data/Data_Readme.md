<h2> About the Data </h2>
The Dataset used to train the model is basically a combination of two datasets. <br> <br>

The first one is a public available SARS-CoV-2 CT scan dataset, containing 1252 CT scans that are positive for SARS-CoV-2 infection (COVID-19) and 1230 CT scans for patients non-infected by SARS-CoV-2, 2482 CT scans in total. 
These data have been collected from real patients in hospitals from Sao Paulo, Brazil. The aim of this dataset is to encourage the research and development of artificial intelligent methods which are able to identify if a person 
is infected by SARS-CoV-2 through the analysis of his/her CT scans. <br>

The Second one is a smaller dataset, as compared to the one mentioned above. It consists of 349 CT-Scans, of COVID positive patients and 396 CT-Scans of non-infected patients. These two datasets
are by-far the two largest CT-Scan datasets available. <br>

Thus, there are overall <b> 1601 </b> CT-scans of COVID Positive patients and <b> 1626 </b> CT-Scans of COVID Negative patients. <br>

Further the CT-Scan images are resized into 3 categories:
<ol>
  1. (32 X 32) Images <br>
  2. (50 X 50) Images <br>
  3. (100 X 100) Images <br>
</ol>

Upon training the model, and observing the results, it was observed that greater the image size, better was the performance of the model on the test set. <br>

As a sample, the csv files corresponding to the (32 X 32) images are provided in the Data Folder. The 'X32.csv' file refers to the image data, and 'y32.csv' file refers
to the verdict. <br>

The (50 X 50) and (100 X 100) csv files are too large to commit. All of these have been prepared using the 'DataPrepare.py' file. By varying the image size and shape, we can
generate all these files. <br> 


