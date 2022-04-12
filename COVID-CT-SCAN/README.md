# COVID-CT-SCAN
This Repository consists of a Deep-learning model that can be used to detect whether a person has been infected by COVID-19 or not, by examining the CT-Scan of the person.

<hr>
<h3> About the Data </h3>
The Dataset used is basically a combination of 2 datasets. These 2 datasets are by far the largest 2 COVID CT-Scan Datasets available on the internet. Since there sizes are too
large, here is the link to the same.

1. https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset
2. https://github.com/UCSD-AI4H/COVID-CT/tree/master/Data-split

Before feeding the data to the model, the data has been normalized.

For more details about data, visit the 'Data' Folder <br>
For some sample images, visit the 'Sample Images' Folder <br>

<hr>

<h3> Model Architecture </h3>
The Model consists of 3 ConvBlocks. Each ConvBlock has a 2D convolutional layer, a dropout and a max-pooling layer. The number of kernels vary over the 3 ConvBlocks in such a way that the image dimensions shrink over the 3 blocks, and the number of channels increase. <br><br>
Then the obtained output of these layers is flattened and fed to two fully connected layers, followed by a sigmoid classifier. The activation function for all the convolutional layers and the fully connected layers is 'relu'. Only the last layer uses a 'sigmoid' activation function. The dense layers also have 2 dropouts before each of them. <br><br>

<b> Space Complexity </b> This model has about 51 Lakh trainable parameters over all the layers <br><br>

<b> Why Dropouts? </b> Because they add a regularizing effect to the model and reduce overfiiting. When this model was trained without dropouts, it led to roughly 10% accuracy difference between training accuracy and validation accuracy. But with dropouts, this difference was reduced to 4%. <br><br>

The Adam Optimizer with a standard learning rate of 1e-3 has been used while training. The loss function used is Binary Crossentropy. For more implementation details, refer to 'model.ipynb'. This model gave the best accruacy of 93.60%.

<hr>

<h3> Division of Data </h3>
The Images have been shuffled randomly and divided into 3 parts - Training set, validation set and test set. The effect of changing the ratio of the sizes of the three sets has also been studied. It is suggested to have a 6:2:2 ratio, But 3 more ratios were tried and the best results came for a 14:3:3 distribution

<table align="center">
  <tr>
    <td align="center">
     S. No. </td>
    <td align="center">
     Ratio </td>
    <td align="center">
     Test Set accuracy </td>
  </tr>
  <tr>
    <td align="center">
     1 </td>
    <td align="center">
     8:1:1 </td>
    <td align="center">
     91.02 </td>
  </tr>
  <tr>
    <td align="center">
     2 </td>
    <td align="center">
     14:3:3 </td>
    <td align="center">
     93.60 </td>
  </tr>
  <tr>
    <td align="center">
     3 </td>
    <td align="center">
     6:1:1 </td>
    <td align="center">
     91.58 </td>
  </tr>
  <tr>
    <td align="center">
     4 </td>
    <td align="center">
     6:2:2 </td>
    <td align="center">
     90.24 </td>
  </tr>
 </table>
<hr>

<h3> Effect of Input Resolution </h3>
The Dataset consists of images of different sizes. The model has been trained and tested on 3 different image sizes, (32 X 32), (50 X 50) and (100 X 100), with the best results coming on the (100 X 100) image. <br><br>

<table align="center">
  <tr>
 <td align="center">
   <b> Accuracy </b>
    </td>
    <td align="center">
     (32, 32) </td>
  <td align="center">
     (50, 50) </td>
  <td align="center">
    (100, 100) </td>
  </tr>
  <tr>
    <td align="center">
      Training Accuracy
    </td>
    <td align="center">
      95.71
    </td>
    <td align="center">
      95.98
    </td>
    <td align="center">
      97.43
    </td>
  </tr>
  <tr>
    <td align="center">
      Validation Accuracy
    </td>
    <td align="center">
      88.35
    </td>
    <td align="center">
      88.35
    </td>
    <td align="center">
      92.36
    </td>
  </tr>
  <tr>
    <td align="center">
      Test Accuracy
    </td>
    <td align="center">
      87.62
    </td>
    <td align="center">
      89.90
    </td>
    <td align="center">
      93.60
    </td>
    
</table>
<hr>
<h3> Image Augmentation </h3>
Image Augmentation was also applied onto the data. Also when an additional ConvBlock and an additional dense layer were added along with image augmentation. With the number of epochs begin 40, the best accuracy came out to be 93.80%. <br><br>

<b> Why the number of epochs is chosen to be 40? </b> Because, the training accuracy approached 1, after 40 epochs.
<hr>

<h3> Results and Drawbacks </h3>
Over several runs from scratch, the test accuracy varied from 90% to 93.60%. These variations occur due to random initializations of the trainable parameters. <br><br>
With Image Augmentation, this accuracy improved to 93.80%. <br><br>
The most major drawback is, that the dataset though a combination of 2 datasets is still quite small. Hence the model may not be able to generalize well over CT-Scans of people from other parts of the world. If a larger dataset is used, then that would definitely improve the model performance.
<hr>

