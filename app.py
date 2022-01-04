from typing import Dict
from flask import Flask,render_template ,request
import pickle
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
## Initialize the app ---------------------------------------

app = Flask(__name__)
model = pickle.load(open('hotel.pkl','rb'))


@app.route('/')
def homepage():
    return render_template('home.html')

# GLOBAL VARIABLES------------------------------------------
month=''
year=''
meal1=''

market_segment1=''
distribution_channel1=''
reserved_room_type1=''
deposit_type1=''
customer_type1=''
arrival_month_year1=''
market_segment2=''


#functions --------------------------------------------------

z1=[]
def reserved_room_type(x):
    if x=='A':
        return [0,0,0,0,0,0,0,0,0]
    else:
        dict1 = {'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'L':0,'P':0}
        dict1[x] = 1
    
    for i in dict1:
        z1.append(dict1[i])
    return z1

# z2=[]
# def reserved_room_type(x):
#     if x=='A':
#         return [0,0,0,0,0,0,0,0,0]
#     else:
#         dict1 = {'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'L':0,'P':0}
#         dict1[x] = 1
    
#     for i in dict1:
#         z2.append(dict1[i])
#     return z2


z3=[]
def meal(y):
    x = 'meal_'+ y
    if x=='meal_BB':
        return [0,0,0,0]
    else:
        dict3={'meal_FB':0, 'meal_HB':0, 'meal_SC':0,'meal_Undefined':0}
        dict3[x]=1
        for i in dict3:
            z3.append(dict3[i])
        return z3

z4=[]
def arrival_month_year(x1,x2):
    p = 'arrival_month_year_'+x1+' '+str(x2)
    if p=='arrival_month_year_April 2016':
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
        dict4={'arrival_month_year_April 2017':0,'arrival_month_year_August 2015':0,'arrival_month_year_August 2016':0,
        'arrival_month_year_August 2017':0, 'arrival_month_year_December 2015':0,'arrival_month_year_December 2016':0, 
        'arrival_month_year_February 2016':0,'arrival_month_year_February 2017':0, 'arrival_month_year_January 2016':0,
        'arrival_month_year_January 2017':0, 'arrival_month_year_July 2015':0,'arrival_month_year_July 2016':0, 
        'arrival_month_year_July 2017':0,'arrival_month_year_June 2016':0, 'arrival_month_year_June 2017':0,
        'arrival_month_year_March 2016':0, 'arrival_month_year_March 2017':0,'arrival_month_year_May 2016':0, 
        'arrival_month_year_May 2017':0,'arrival_month_year_November 2015':0, 'arrival_month_year_November 2016':0,
        'arrival_month_year_October 2015':0, 'arrival_month_year_October 2016':0,'arrival_month_year_September 2015':0,
        'arrival_month_year_September 2016':0}
        dict4[p]=1
        for i in dict4:
            z4.append(dict4[i])
        return z4


z5=[]

def market_segment(y):
    x = 'market_segment_'+ y
    if x=='market_segment_Aviation':
        return [0,0,0,0,0,0,0]
    else:
        dict5={'market_segment_Complementary':0, 'market_segment_Corporate':0, 'market_segment_Direct':0,'market_segment_Groups':0,'market_segment_Offline TA/TO':0,'market_segment_Online TA':0, 'market_segment_Undefined':0}
        dict5[x]=1
        for i in dict5:
            z5.append(dict5[i])
        return z5

z6=[]
def distribution_channel(y):
    x = 'distribution_channel_'+ y
    if x=='distribution_channel_Corporate':
        return [0,0,0,0,0,0,0]
    else:
        dict6={'distribution_channel_Direct':0, 'distribution_channel_GDS':0, 'distribution_channel_TA/TO':0,'distribution_channel_Undefined':0}
        dict6[x]=1
        for i in dict6:
            z6.append(dict6[i])
        return z6

z8=[]
def customer_type(y):
    x = 'customer_type_'+ y
    if x=='customer_type_Contract':
        return [0,0,0]
    else:
        dict8={'customer_type_Group':0, 'customer_type_Transient':0,'customer_type_Transient_party':0}
        dict8[x]=1
        for i in dict8:
            z8.append(dict8[i])
        return z8
z7=[]
def deposit_type(y):
    x = 'deposit_type_'+ y
    if x=='deposit_type_No Deposit':
        return [0,0]
    else:
        dict7={'deposit_type_Non Refund':0, 'deposit_type_Refundable':0}
        dict7[x]=1
        
        for i in dict7:
            z7.append(dict7[i])
        return z7

final_input_list=[]
@app.route('/predict' , methods = ['post'])
def predict():
    stays_in_weekend_nights = request.form.get('stays_in_weekend_nights')
    adult = request.form.get('adult')
    children = request.form.get('children')
    babies = request.form.get('babies')
    is_repeated_guest = request.form.get('is_repeated_guest')
    previous_cancellations = request.form.get('previous_cancellations')
    required_car_parking_spaces=request.form.get('required_car_parking_spaces')
    total_of_special_requests=request.form.get('total_of_special_requests')
    hotel=request.form.get('hotel')
    month = request.form.get('month')
    year = request.form.get('year')
    arrival_month_year1 = arrival_month_year(month,year)
    meal1=request.form.get('meal')
    meal2=meal(meal1)
    market_segment1=request.form.get('market_segment')
    
    #print(stays_in_weekend_nights,adult,children,babies,is_repeated_guest,previous_cancellations,required_car_parking_spaces,total_of_special_requests,hotel)
    #arrival_month_year(month,year)
    #meal(meal1)
    market_segment2=market_segment(market_segment1)
    distribution_channel1 = request.form.get('distribution_channel')
    distribution_channel2=distribution_channel(distribution_channel1)
    reserved_room_type1 = request.form.get('reserved_room_type')
    reserved_room_type2=reserved_room_type(reserved_room_type1)
    deposit_type1 = request.form.get('deposit_type')
    deposit_type2 = deposit_type(deposit_type1)
    customer_type1 = request.form.get('customer_type')
    customer_type2=customer_type(customer_type1)
    lead_time = request.form.get('lead_time')
    arrival_date_day_of_month=request.form.get('arrival_date_day_of_month')
    stays_in_week_nights=request.form.get('stays_in_week_nights')
    agent=request.form.get('agent')
    # print(lead_time,arrival_date_day_of_month,stays_in_week_nights,agent)


    # final_input_list=[[stays_in_weekend_nights],[adult],[children],[babies],[is_repeated_guest],[previous_cancellations],[required_car_parking_spaces],
    # [total_of_special_requests],[hotel],arrival_month_year1,meal2,market_segment2,distribution_channel1,reserved_room_type2,customer_type2,[lead_time]
    # ,[arrival_date_day_of_month],[stays_in_week_nights],[agent]]
    
    print(stays_in_weekend_nights,adult,children,babies,is_repeated_guest,previous_cancellations,required_car_parking_spaces,
    total_of_special_requests,hotel,arrival_month_year1,meal2,market_segment2,distribution_channel2,reserved_room_type2,deposit_type2,customer_type2,lead_time
    ,arrival_date_day_of_month,stays_in_week_nights,agent)


    final_input_list=[stays_in_weekend_nights,adult,children,babies,is_repeated_guest,previous_cancellations,required_car_parking_spaces,
    total_of_special_requests,hotel,arrival_month_year1,meal2,market_segment2,distribution_channel2,reserved_room_type2,deposit_type2,
    customer_type2,lead_time,arrival_date_day_of_month,stays_in_week_nights,agent]


    final_input = []
    
    for i in range(0,len(final_input_list)):
    
        if type(final_input_list[i]) == list:
            #print(final_input_list[i])
            final_input.extend(final_input_list[i])
        else:
            #print(final_input_list[i])
            final_input.append(final_input_list[i])
        final_input = list(map(int,final_input))
    # for i in final_input_list:
    #     final_input.extend(list(i))
    # final_input = list(map(int,final_input))
    print(final_input)

    output = model.predict(np.array(final_input).reshape((1,len(final_input))))
    print(output)
    if output[0]:
        output_final = 'Hotel Booking was Cancelled'
    else:
        output_final = 'Hotel Booking was Not Cancelled'
    # return render_template('app.html')
    return render_template('form.html', pred = f"'{output_final}'")
#running the app-------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
