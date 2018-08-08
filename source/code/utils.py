import matplotlib.pyplot as plt
from sklearn.metrics import auc, precision_recall_curve, roc_curve


def plot_roc_curves(y_true, y_pred_map):
    f, axs = plt.subplots(1, len(y_pred_map.keys()), figsize=(30, 5))
    aucs = []
    for i, est_name in enumerate(y_pred_map):
        fpr, tpr, thresholds = roc_curve(y_true, y_pred_map[est_name])
        aucs.append(auc(fpr, tpr))
        axs[i].plot(fpr, tpr)
        axs[i].set_xlabel('FPR')
        axs[i].set_ylabel('TPR')
        axs[i].set_title('Estimator: {}, AUC: {}'.format(est_name, auc(fpr, tpr)))
    plt.tight_layout()
    plt.show()
    return aucs


def plot_pr_curves(y_true, y_pred_map):
    f, axs = plt.subplots(1, len(y_pred_map.keys()), figsize=(30, 5))
    aucs = []
    for i, est_name in enumerate(y_pred_map):
        precision, recall, thresholds = precision_recall_curve(y_true, y_pred_map[est_name])
        aucs.append(auc(precision, recall, reorder=True))
        axs[i].plot(precision, recall)
        axs[i].set_xlabel('Precision')
        axs[i].set_ylabel('Recall')
        axs[i].set_title('Estimator: {}, AUC: {}'.format(est_name, auc(precision, recall, reorder=True)))
    plt.tight_layout()
    plt.show()
    return aucs
