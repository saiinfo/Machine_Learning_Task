
dataset link:
https://drive.google.com/file/d/1AEX_Ugf0KBjSbx08AV5RY6QJwrjUSqa5/view?usp=drive_link, 

1>binary valence classification:(positive,negative)#binaryvalence.
implement binary valence classification for each dataset according to participants

2>personmodel
implement mullticlass classification for each dataset according to participants

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