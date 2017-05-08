RMC测试用数据库
================

此数据库为RMC测试专用。根据算例使用情况按需更新。

连续能量点截面NNDC库
=====================

数据来源
---------

NNDC发布的ENDF/B VII.1核截面库

 -  293.6K中子核截面库： http://www.nndc.bnl.gov/endf/b7.1/aceFiles/ENDF-B-VII.1-neutron-293.6K.tar.gz

 - 热化库：http://www.nndc.bnl.gov/endf/b7.1/aceFiles/ENDF-B-VII.1-tsl.tar.gz


使用方式
=========

  .. code-block:: sh

        git clone --branch=master https://github.com/thu-real/RMC_TestNucData.git testdatalib
        cp -r testdatalib/* $HOME/nucdata/
        rm -rf testdatalib
        python $HOME/nucdata/update_xsdir.py