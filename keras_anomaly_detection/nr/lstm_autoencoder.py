import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras_anomaly_detection.library.plot_utils import visualize_reconstruction_error
from keras_anomaly_detection.library.recurrent import LstmAutoEncoder

DO_TRAINING = True

# modified from visualize_reconstruction_error in plot_utils.py
def create_plot(reconstruction_error, threshold, other_point=None):
    # plt.plot(reconstruction_error, marker='o', ms=3.5, linestyle='',
    #          label='Point')

    # plt.plot(other_point, marker='o', ms=3.5, linestyle='', label="Error Rate")
    # plt.hlines(threshold, xmin=0, xmax=len(reconstruction_error)-1, colors="r", zorder=100, label='Threshold')
    # plt.legend()
    # plt.title("Reconstruction error")
    # plt.ylabel("Reconstruction error")
    # plt.xlabel("Data point index")
    # plt.show()

    LABELS = ["Normal", "Anomaly"]
    sns.set(style='whitegrid', palette='muted', font_scale=1.5)


    y_pred = [1 if e > threshold else 0 for e in df.reconstruction_error.values]
    conf_matrix = confusion_matrix(df.true_class, y_pred)

    plt.figure(figsize=(12, 12))
    sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d");
    plt.title("Confusion matrix")
    plt.ylabel('True class')
    plt.xlabel('Predicted class')
    plt.savefig("RPM-UI-anomaly-conf-matrix.png")
    plt.show()

def main():
    data_dir_path = './data/nr/28days'
    model_dir_path = './models'
    cpm_csv_data = pd.read_csv(data_dir_path + '/1m/twitter_labeled_ts-1-RPM-UI-2017-10-01.csv', header=0)
    labled_data = pd.read_csv(data_dir_path + '/1m/cpm_ts-1-RPM-UI-2017-10-01.csv', header=0)
    y_test = labled_data['class']
    cpm_csv_data = cpm_csv_data.fillna(0)
    cpm_csv_data = cpm_csv_data.astype('float32')
    cpm_np_data = cpm_csv_data.as_matrix()
    scaler = MinMaxScaler(feature_range=(0, 1))
    cpm_np_data = scaler.fit_transform(cpm_csv_data)

    ae = LstmAutoEncoder()

    # fit the data and save model into model_dir_path
    if DO_TRAINING:
        ae.fit(cpm_np_data[:40321, :], model_dir_path=model_dir_path, estimated_negative_sample_ratio=0.9, epochs=20)

    # load back the model saved in model_dir_path detect anomaly
    ae.load_model(model_dir_path)
    anomaly_information = ae.anomaly(cpm_np_data[:40321, :])
    reconstruction_error = []
    for idx, (is_anomaly, dist) in enumerate(anomaly_information):
        # print('# ' + str(idx) + ' is ' + ('abnormal' if is_anomaly else 'normal') + ' (dist: ' + str(dist) + ')')
        reconstruction_error.append(dist)

    error_df = pd.DataFrame({'reconstruction_error': reconstruction_error,
                             'true_class': y_test})
    create_plot(error_df, ae.threshold)


if __name__ == '__main__':
    main()
