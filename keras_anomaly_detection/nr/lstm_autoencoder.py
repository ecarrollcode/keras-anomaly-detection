import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras_anomaly_detection.library.plot_utils import visualize_reconstruction_error
from keras_anomaly_detection.library.recurrent import LstmAutoEncoder

DO_TRAINING = False


def main():
    data_dir_path = './data/nr/28days'
    model_dir_path = './models'
    csv_data = pd.read_csv(data_dir_path + '/10m/ts-1-RPM-UI-2017-09-27.csv', header=0)
    # csv_data = csv_data.values
    csv_data = csv_data.astype('float32')
    rpm_np_data = csv_data.as_matrix()
    scaler = MinMaxScaler(feature_range=(0, 1))
    rpm_np_data = scaler.fit_transform(csv_data)
    print(rpm_np_data.shape)

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

    visualize_reconstruction_error(reconstruction_error, ae.threshold)


if __name__ == '__main__':
    main()
