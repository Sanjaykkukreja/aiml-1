from . import Record_audio
import numpy as np
import warnings
import os
import joblib
warnings.filterwarnings("ignore")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

n_mfcc = 30
n_mels = 128
frames = 15

list_task = [['Idly', ' Dosa', ' Wada', 'Puri ', 'Chapathi'],[0, 1, 2, 3, 4]];
menu_prompts = ["menu_list.wav", "quantity_list.wav"]
#list_task[0] is list of menu items
#list_task[0] is list of quantity allowed

####################################################################################
#Train a classifier using the given training data to classify the samples
#One way is to regress the features to the get the labels
#get a confidence metric to evalaute your prediction
####################################################################################
import pdb
T = 0.75 # confidence threshold, replace the value accordingly to your confidence measure
class order():
	#classify the input given the features and model. 
	#Change the function definition accordingly to suite your classifier 
	#It should return predicted label and a confident measure for your prediction
	def classify_input(self, features, model):
		predicted_label = model.predict(features)
		confidence_measure = model.predict_proba(features)
		return int(predicted_label[0]), round(np.amax(confidence_measure))

	def confirm_input(self, digit,confidence,flag):
		print("digit you said is ", digit)
		if(confidence > T) and (digit < len(list_task[flag])):
			return digit,list_task[flag][digit]
		return -99, -99


	def take_user_input(self, flag):
		#audio_file_path = Record_audio.record_voice("userinput", "1", 1, "./")
		#print(audio_file_path)
		features = Record_audio.get_features(BASE_DIR +'/Hackathon-setup/1_userinput_1.wav', sr=8000)
		#features = Record_audio.get_features(BASE_DIR + "/Hackathon-setup/team_data/3_b13h1g05_1581757672.wav", sr=8000)
		features = np.reshape(features,(1,-1))	
		# Extract features from the user input
		#calling classify_input to get the prediction and confidence measure by giving features and model, you have to complete the classify_input method
	#	model = joblib.load(os.path.join(BASE_DIR,'Hackathon-setup/mlpTrainModel'))a
		model = joblib.load(os.path.join(BASE_DIR, 'Hackathon-setup/finalized_model_group_5_joblib.sav'))
		digit,confidence = self.classify_input(features,model)
		digit,choice = self.confirm_input(digit,confidence,flag)
		return digit,choice
'''
input_order = order()
flag = 0
digit1,choice1 = input_order.take_user_input(flag)
flag = 1
digit2,choice2 = input_order.take_user_input(flag)
#print ('You Said digit: '+str(digit)+ ' to confirm your Order of ' + str(choice).upper())
print('you said digit ' + str(digit2) + ' and ' + str(digit1) + ' to confirm your order of ' + str(choice2) + ' quantity of ' + str(choice1))
'''
