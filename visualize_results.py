import matplotlib.pyplot as plt
import yaml

def plot_results(results_file):
    """
    Plots training and validation metrics from the results file.
    Args:
        results_file (str): Path to the results YAML file generated during training.
    """
    with open(results_file, 'r') as f:
        results = yaml.safe_load(f)

    # Extract metrics
    epochs = range(len(results['metrics']['train_loss']))
    train_loss = results['metrics']['train_loss']
    val_loss = results['metrics']['val_loss']
    precision = results['metrics']['precision']
    recall = results['metrics']['recall']
    mAP = results['metrics']['mAP']

    # Plot losses
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, train_loss, label='Train Loss')
    plt.plot(epochs, val_loss, label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.show()

    # Plot precision, recall, and mAP
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, precision, label='Precision')
    plt.plot(epochs, recall, label='Recall')
    plt.plot(epochs, mAP, label='mAP')
    plt.xlabel('Epochs')
    plt.ylabel('Metrics')
    plt.title('Precision, Recall, and mAP')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    results_file = "runs/train/exp/results.yaml"  # Update this path if needed
    plot_results(results_file)
