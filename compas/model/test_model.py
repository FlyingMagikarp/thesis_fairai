import tensorflow as tf
from datetime import datetime
import sys

#sys.stdout = open('../results/compas_results.txt', 'w')
def set_priors_in_list(dlist, nr_priors):
    for i in dlist:
        i[0] = nr_priors
    return dlist


def set_misdemeanor_in_list(dlist, nr_misd):
    for i in dlist:
        i[-1] = nr_misd
    return dlist


# Two_yr_Recidivism,Number_of_Priors,score_factor, == 3, score_factor might get removed
# Age_Above_FourtyFive,Age_Below_TwentyFive, == 3 possible configs
# African_American,Asian,Hispanic,Native_American,Other, == 6 possible configs, also 6 fields with new dataset
# Female,Misdemeanor == 2
def get_test_data(data_type):
    data = {}

    ### male
    data['caucasian_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0,          0, 0,    1, 0, 0, 0, 0, 0,    0, 0],
        [0,          1, 0,    1, 0, 0, 0, 0, 0,    0, 0],
        [0,          0, 1,    1, 0, 0, 0, 0, 0,    0, 0]
    ]

    data['african_american_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0,          0, 0,    0, 1, 0, 0, 0, 0,    0, 0],
        [0,          1, 0,    0, 1, 0, 0, 0, 0,    0, 0],
        [0,          0, 1,    0, 1, 0, 0, 0, 0,    0, 0]
    ]

    data['asian_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0,          0, 0,    0, 0, 1, 0, 0, 0,    0, 0],
        [0,          1, 0,    0, 0, 1, 0, 0, 0,    0, 0],
        [0,          0, 1,    0, 0, 1, 0, 0, 0,    0, 0]
    ]

    data['hispanic_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0,          0, 0,    0, 0, 0, 1, 0, 0,    0, 0],
        [0,          1, 0,    0, 0, 0, 1, 0, 0,    0, 0],
        [0,          0, 1,    0, 0, 0, 1, 0, 0,    0, 0]
    ]

    data['native_american_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0,          0, 0,    0, 0, 0, 0, 1, 0,    0, 0],
        [0,          1, 0,    0, 0, 0, 0, 1, 0,    0, 0],
        [0,          0, 1,    0, 0, 0, 0, 1, 0,    0, 0]
    ]

    data['other_male'] = [
        #prio, scor  age      races             gender, misdemeanor
        [0,          0, 0,    0, 0, 0, 0, 0, 1,    0, 0],
        [0,          1, 0,    0, 0, 0, 0, 0, 1,    0, 0],
        [0,          0, 1,    0, 0, 0, 0, 0, 1,    0, 0]
    ]

    ### female
    data['caucasian_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0,           0, 0,   1, 0, 0, 0, 0, 0,     1, 0],
        [0,           1, 0,   1, 0, 0, 0, 0, 0,     1, 0],
        [0,           0, 1,   1, 0, 0, 0, 0, 0,     1, 0]
    ]

    data['african_american_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0,           0, 0,   0, 1, 0, 0, 0, 0,     1, 0],
        [0,           1, 0,   0, 1, 0, 0, 0, 0,     1, 0],
        [0,           0, 1,   0, 1, 0, 0, 0, 0,     1, 0]
    ]

    data['asian_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0,           0, 0,   0, 0, 1, 0, 0, 0,     1, 0],
        [0,           1, 0,   0, 0, 1, 0, 0, 0,     1, 0],
        [0,           0, 1,   0, 0, 1, 0, 0, 0,     1, 0]
    ]

    data['hispanic_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0,           0, 0,   0, 0, 0, 1, 0, 0,     1, 0],
        [0,           1, 0,   0, 0, 0, 1, 0, 0,     1, 0],
        [0,           0, 1,   0, 0, 0, 1, 0, 0,     1, 0]
    ]

    data['native_american_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0,           0, 0,   0, 0, 0, 0, 1, 0,     1, 0],
        [0,           1, 0,   0, 0, 0, 0, 1, 0,     1, 0],
        [0,           0, 1,   0, 0, 0, 0, 1, 0,     1, 0]
    ]

    data['other_female'] = [
        # prio, scor  age      races             gender, misdemeanor
        [0,           0, 0,   0, 0, 0, 0, 0, 1,     1, 0],
        [0,           1, 0,   0, 0, 0, 0, 0, 1,     1, 0],
        [0,           0, 1,   0, 0, 0, 0, 0, 1,     1, 0]
    ]


    if data_type == 'baseline':
        return data
    if data_type == 'norace':
        for key, value in data.items():
            for v in value:
                v.pop(4)
                v.pop(4)
                v.pop(4)
                v.pop(4)
                v.pop(4)
                v.pop(4)
        return data
    if data_type == 'nogender':
        for key, value in data.items():
            for v in value:
                v.pop(10)
        return data

    return data


def init_logfile():
    date = datetime.now()
    time_suffix = str(date.year) + '-' + str(date.month) + '-' + str(date.day) + '-' + str(date.hour) + '-' + str(date.minute) + '-' + str(date.second)
    filename = '../results/compas_results_baseline_{}.txt'.format(time_suffix)
    with open(filename, 'w') as f:
        f.write(time_suffix + '\n')
    return filename


def log_string(filename, string):
    with open(filename, 'a') as f:
        f.write(string)
        f.write('\n')


def log_predictions(filename, preds):
    with open(filename, 'a') as f:
        f.write('25+' + str(preds[0])+'\n')
        f.write('45+' + str(preds[1])+'\n')
        f.write('18+' + str(preds[2])+'\n')

start_time = datetime.now()

models = [
    {'model': tf.keras.models.load_model('./models/baseline'), 'model_type': 'baseline'}#,
    #{'model': tf.keras.models.load_model('./models/norace'), 'model_type': 'norace'},
    #{'model': tf.keras.models.load_model('./models/nogender'), 'model_type': 'nogender'}
]

fn = init_logfile()
for i in range(4):
    for j in range(4):
        log_string(fn, '#'+str(i)+'-'+str(j)+'#')
        for model_info in models:
            model = model_info['model']
            type = model_info['model_type']

            data = get_test_data(type)

            print('Model: ', type)
            log_string(fn, 'Model: '+type)
            print('##########')
            log_string(fn, '##########')
            for key, value in data.items():
                print(key)
                log_string(fn, key)
                value = set_priors_in_list(value, i)
                value = set_misdemeanor_in_list(value, j)
                print(value)
                predictions = model.predict(value)
                log_predictions(fn, predictions)
                print(model.predict(value))
                log_string(fn, '###')
            print('##########')
            log_string(fn, '##########')
            log_string(fn, '##########')

print('Done analysis')
print('Time:')
print(datetime.now() - start_time)
#sys.stdout.close()