
```
$ wget https://gist.githubusercontent.com/qhduan/a2fb254c10ff1130d33ac2581ac9ce13/raw/0bf67fb1d9f42855e09fef0e1ce249258b52dd3e/gdown.pl

$ perl gdown.pl https://drive.google.com/open?id=1MdQkOIcolZP7b3GSfsJ28XIP8lnxOEkV gpt_model_tf2.tar

$ tar xvf gpt_model_tf2.tar

$ mv gpt_model_tf2 1 && mkdir -p gpt && mv 1 gpt/

# for testing

$ docker run -it --rm -p 8506:8501 qhduan/gpt
$ python3 gpt.py

```


