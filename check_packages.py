import importlib

required_packages = [
    "torch",
    "numpy",
    "matplotlib",
    "opencv-python",
    "PyYAML",
    "ultralytics",
    "flask",  # Eğer API geliştirecekseniz
    "fastapi",  # Alternatif API geliştirme kütüphanesi
    "tensorboard",  # İsteğe bağlı
    "thop",  # İsteğe bağlı
]

for package in required_packages:
    try:
        importlib.import_module(package)
        print(f"{package} is installed.")
    except ImportError:
        print(f"{package} is NOT installed. Install it using 'pip install {package}'")
