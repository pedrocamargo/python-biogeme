FROM python:3.6

RUN \
  curl -O http://biogeme.epfl.ch/distrib/biogeme-2.6a.tar.gz && \
  tar xvzf biogeme-2.6a.tar.gz && \
  cd biogeme-2.6a && \
  ./configure --enable-bison --enable-python && \
  make && \
  make install && \
  cd .. && \
  rm -rf biogeme-2.6a*
