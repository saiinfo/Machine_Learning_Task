
dataset link:
https://drive.google.com/file/d/1AEX_Ugf0KBjSbx08AV5RY6QJwrjUSqa5/view?usp=drive_link, 
Audio Classification with Convolutional Neural Networks (CNN) - README
Overview
This script is designed for audio classification using Convolutional Neural Networks (CNN) . It processes audio data from a specified directory, extracts audio features (e.g., MFCCs, chroma, spectral contrast),(featureextraction: MFCCs, chroma, spectral contrast, mel spectrogram, FFT, RMSE) and trains a CNN model for audio classification. The model is trained and evaluated multiple cnn model, and F1 scores are calculated to assess its performance.

Requirements
Before running the script, make sure you have the following dependencies installed:

Python
NumPy
Pandas
Librosa
Scikit-learn
TensorFlow
You can install these packages using pip if you don't have them already:


pip install numpy pandas librosa scikit-learn tensorflow


Usage
Directory Setup: Modify the script_dir and wav_dir variables to point to your audio dataset's directory.
python

script_dir = r"C:\Users\pawan\Desktop\mv\downloaddataset"
wav_dir = os.path.join(script_dir, "downloaded_wav_files")
Feature Extraction: Implement the extract_audio_features function to extract audio features based on your dataset's requirements. In the provided script, MFCCs, chroma, and spectral contrast features are extracted as an example.

Data Preparation: Ensure you have a Pandas DataFrame (dataset) that contains the 'Filename' and 'Label' columns. Update the script to match your dataset's structure.

Filter Labels (Optional): If your dataset contains labels not present in your training data, you can filter them out.

Model Configuration: Adjust the create_model function to define the architecture of your CNN model. You may need to change the input shape and the number of classes based on your data.

Training Parameters: Customize the training parameters , such as the number of epochs, batch size, and validation split.

Label Encoding: If your labels are strings, encode them into integers using LabelEncoder.

Run the Script: Execute the script.  will train the model for each session and calculate the F1 score for each session. The mean F1 score across sessions will be printed at the end.

Example Data
An example dataset (p1_datasets) is used in the script to demonstrate the process. You should replace it with your own dataset.

Output
The script prints the F1 score for each session and the mean F1 score across sessions, providing an evaluation of the model's performance.

Customization
Customize the feature extraction process and model architecture to better suit your specific audio classification task.

Error Handling
The script includes error handling for missing audio files and issues that may occur during feature extraction. Any errors are printed to the console.

Important Notes
Make sure your dataset is correctly structured with the 'Filename' and 'Label' columns.
Adapt feature extraction, label encoding, and model architecture to your specific dataset and classification task.



>binary valence classification:(positive,negative)#binaryvalence.
implement binary valence classification for each dataset according to the participants

2>personmodel
implement multiclass classification for each dataset according to the participants

3>fp1,fp2,fp3,fp5,fp6,fp8,fp11,fp16
tested different feature extraction methods on each dataset associated with participants for accuracy test
best model accuracy
fp1=Mfcc(75%)and combined_4(mfcc,mel,chroma,spectral_contrast)(75%)
fp2=mfcc+contrast(61%)
fp3=mfcc+mel(78%)
fp5=mfcc+contrast(58%) and combined_4(59%)
fp6=mek(42%) and combined_4(41%)
fp8=combined_4(78%)
fp11=mfcc+contrast(59%)
fp16=mfcc+contrast(74%)
