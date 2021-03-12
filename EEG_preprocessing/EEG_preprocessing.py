#import dataset from EEGLAB
from oct2py import octave

octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/guifunc')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/popfunc')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/adminfunc')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/sigprocfunc')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/miscfunc')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/statistics')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/studyfunc')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/supportfiles')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/functions/timefreqfunc')
octave.addpath('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/plugins/firfilt')

EEG = octave.pop_loadset('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/project/Depression_REST/Matlab_Files/507_Depression_REST.mat')
#EEG = octave.pop_loadset('C:/Program Files/MATLAB/eeglab_current/eeglab2021.0/sample_data/eeglab_data.set') #example use sample_data/eeglab_data_epochs_ica.set

#plot first trail of channel 1
import matplotlib.pyplot as plt
#plt.plot(EEG.data[10][0:249000])
#plt.show()

EEG_data = EEG
EEG_data.data = EEG.data[:][0:248000]
EEG2 = octave.pop_eegfiltnew(EEG_data, 0.5, 100, [], 0, [], 0) 

plt.plot(EEG2.data[0][0:248000])
plt.show()

#AnalyName = 'ica';

#pop_rejechan # reject channel function
#Reject large artifact time points

#when the raw data is embeded in the .set file
#import scipy.io as sio
#EEG = sio.loadmat('eeglabfile.set')

#If the raw data is stored in a separate .fdt file
#import mne
#EEG = mne.io.read_epochs_eeglab('eeglabfile.set')