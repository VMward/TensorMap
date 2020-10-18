# TensorMap

[![PyPI Version](https://img.shields.io/badge/Version-0.0.1-3775A9?style=plastic&logo=PyPi)](https://pypi.org/project/pylearn/)
[![Code Coverage](https://img.shields.io/badge/CodeCoverage-99p-F01F7A?style=plastic&logo=CodeCov)](https://github.com/social-learning/TensorMap)
[![Github](https://img.shields.io/badge/GitHub-TensorMap-181717?style=plastic&logo=GitHub)](https://github.com/social-learning/TensorMap)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-CodeForAll-0077B5?style=plastic&logo=LinkedIn)](https://www.linkedin.com/company/codeforall/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.3.1-FF6F00?style=plastic&logo=TensorFlow)](https://https://www.tensorflow.org/)
[![OpenAIGym](https://img.shields.io/badge/OpenAIGym-0.12.5-0081A5?style=plastic&logo=OpenAI-Gym)](https://gym.openai.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.6.0-EE4C2C?style=plastic&logo=PyTorch)](https://pytorch.org/)

## Installation
Use the package manager [pip](https://pypi.org/project/TensorMap/) `pip install TensorMap` to install TensorMap.

## Usage
```
import TensorMap as tm
tm.visualize(sample.load_data("fort_collins_demo_data"))
```
## Contributing
1. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

    Please make sure to update tests as appropriate.
    
1. If you would like to become an administrator or bundle the code directly, please request a GitHub API key and a PyPi token.

    Setup Tools - Install the following
* `python3 -m pip install --user --upgrade setuptools wheel`
* `python3 -m pip install --user --upgrade twine`
    
    Run the Following command in order:
* Generating distribution archives `python3 setup.py sdist bdist_wheel`
* Upload the distribution archives `python3 -m twine upload --repository testpypi dist/*`

## Testing and Setup
1. It is suggested that you create a virtual env `python3 -m venv /path/` or house it in a docker container before continuing
1. Download Dependencies `pip install requirements.txt `