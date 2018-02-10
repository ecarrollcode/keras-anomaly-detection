import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras_anomaly_detection.library.plot_utils import visualize_reconstruction_error
from keras_anomaly_detection.library.recurrent import LstmAutoEncoder

DO_TRAINING = False

# modified from visualize_reconstruction_error in plot_utils.py
def create_plot(reconstruction_error, threshold, other_point=None):
    plt.plot(reconstruction_error, marker='o', ms=3.5, linestyle='',
             label='Point')

    plt.plot(other_point, marker='o', ms=3.5, linestyle='', label="Error Rate")
    plt.hlines(threshold, xmin=0, xmax=len(reconstruction_error)-1, colors="r", zorder=100, label='Threshold')
    plt.legend()
    plt.title("Reconstruction error")
    plt.ylabel("Reconstruction error")
    plt.xlabel("Data point index")
    plt.show()

def main():
    data_dir_path = './data/nr/28days'
    model_dir_path = './models'
    csv_data = pd.read_csv(data_dir_path + '/10m/ts-1-RPM-UI-2017-09-27.csv', header=0)
    # csv_data = csv_data.values
    csv_data = csv_data.astype('float32')
    error_rate = csv_data['error_pct'].tolist()
    rpm_np_data = csv_data.as_matrix()
    scaler = MinMaxScaler(feature_range=(0, 1))
    rpm_np_data = scaler.fit_transform(csv_data)

    ae = LstmAutoEncoder()

    # fit the data and save model into model_dir_path
    if DO_TRAINING:
        ae.fit(rpm_np_data[:4033, :], model_dir_path=model_dir_path, estimated_negative_sample_ratio=0.9, epochs=50)

    # load back the model saved in model_dir_path detect anomaly
    ae.load_model(model_dir_path)
    anomaly_information = ae.anomaly(rpm_np_data[:4033, :])
    reconstruction_error = []
    for idx, (is_anomaly, dist) in enumerate(anomaly_information):
        # print('# ' + str(idx) + ' is ' + ('abnormal' if is_anomaly else 'normal') + ' (dist: ' + str(dist) + ')')
        reconstruction_error.append(dist)

    create_plot(reconstruction_error, ae.threshold, error_rate)


if __name__ == '__main__':
    main()
