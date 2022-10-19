# hackerdojo-pythonistas
Hacker Dojo Python Sessions (sponsored by Intel)


# Intro

Welcome to the Python sessions at [Hacker Dojo](https://hackerdojo.org). The Hacker Dojo is a community of engineers, artists, scientists, activists, entrepreneurs and other creative people centered around a co-working and social facility. Feel free to drop by and see for yourself what the Dojo is all about.

These sessions are sponsored by [Intel](https://www.intel.com). Take a look at this post about [How to put your Python skills to work](https://medium.com/intel-tech/how-to-put-your-python-skills-to-work-in-ai-3c581b916a41).

You will learn about the [Edge AI Certification](https://www.intel.com/content/www/us/en/developer/tools/devcloud/edge/learn/certification.html?utm_campaign=python_campaign_q322&utm_source=Medium&utm_medium=Blog&utm_content=python_blog&utm_term=edge_ai_cert) and the [30-Day AI Dev Challenge](https://devchallenge.intel.com/na_30_start?utm_campaign=python_campaign_q322&utm_source=Medium&utm_medium=Blog&utm_content=python_blog&utm_term=5_reasons_header)

Consider joining the challenge!

# Prerequisites

Please have installed: 

- VS Code (or any other python-friendly IDE)
    - Install extensions for python development: Python (by Microsoft, it includes Pylance and some other useful tools).
    - Configure `Black` as a formatter and enable `Format on Save` option.
    - (Optional) Add black argument: `--line-length=110`.
- Python 3.8+


# Sessions
Here's the summary of each session:

[Session 1](session_1/README.md)


# Major Dependencies

- Jupyter lab/notebook
    `python3 -m pip install jupyter-lab` or `python3 -m pip install notebook`
- OpenCV 
    - Linux: Use your preferred package manager or install from source
    - Mac: Use homebrew
    - Windows: Follow the instructions on this blog post: `https://learnopencv.com/install-opencv-on-windows/`
- OpenVINO
    - For x86_64 follow: `https://docs.openvino.ai/latest/openvino_docs_install_guides_install_runtime.html`
    - For Apple Silicon (build from source):  `https://github.com/openvinotoolkit/openvino/wiki`