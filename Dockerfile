FROM tensorflow/serving
EXPOSE 8500
EXPOSE 8501
ENV MODEL_NAME=gpt
COPY ./gpt /models/gpt
