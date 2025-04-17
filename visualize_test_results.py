import matplotlib.pyplot as plt
import yaml

def plot_test_results(results_file):
    """
    Plots test metrics from the results file.
    Args:
        results_file (str): Path to the results YAML file generated during validation.
    """
    with open(results_file, 'r') as f:
        results = yaml.safe_load(f)

    # Extract metrics
    precision = results['metrics']['precision']
    recall = results['metrics']['recall']
    mAP = results['metrics']['mAP']
    classes = results['metrics']['classes']

    # Plot precision, recall, and mAP per class
    plt.figure(figsize=(10, 5))
    plt.bar(classes, precision, label='Precision', alpha=0.6)
    plt.bar(classes, recall, label='Recall', alpha=0.6)
    plt.bar(classes, mAP, label='mAP', alpha=0.6)
    plt.xlabel('Classes')
    plt.ylabel('Metrics')
    plt.title('Precision, Recall, and mAP per Class')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    results_file = "runs/val/exp/results.yaml"  # Update this path if needed
    plot_test_results(results_file)
