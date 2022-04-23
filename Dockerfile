FROM python:3.6.7

RUN pip install pip --upgrade

ARG UNAME=seat
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME
USER $UNAME
RUN mkdir -p /home/seat
COPY ./requirements /home/seat/mower/requirements
ENV PATH "/home/seat/.local/bin:${PATH}"
RUN pip install --user -r /home/seat/mower/requirements/dev.txt
WORKDIR /home/seat/mower

CMD ["sleep", "infinity"]