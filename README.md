# pivotTableStreamlit
Making tables and pivots tables with streamline

The code is for demonstrating how to make filters on a random data sets of 12,000 points and make plots from it
The main goal is to show the data to a webpage and manipulate it online


## Installation

As mentioned in the documentation page it is recommended to install the strealit in a separate environment

https://docs.streamlit.io/en/stable/troubleshooting/clean-install.html?highlight=cannot%20run%20streamline%20in%20terminal#install-streamlit-on-macos-linux

## pip install

```python
    pip install streamlit
```


## using docker 
After cloning the repo you can run the below command

```Bash
    docker build -t pivot:latest . -f Dockerfile

    docker run -p 8501:8501 pivot:latest
```
An image will be creared called pivot (you can change the name to your liking)
Now you can open the streamlit page locally under https://localhost:8501

