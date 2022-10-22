# License Plate Detection with Yolov5

距离上次车牌检测模型更新已经过了一年多的时间，这段时间也有很多快速、准确的模型提出，我们利用单物体检测算法Yolov5进行了车牌检测模型的训练，通过测试，检测效果和适用性都更突出，支持的模型也更为丰富。

我们开源版本的检测算法经过了多个版本迭代，考虑到检测的效率跟准确率，原始版本逐步淘汰，从最初的基于LBP和Harr特征的车牌检测，感兴趣的小伙伴可以参考train-detector(https://github.com/openalpr/train-detector) 这个仓库；到后来逐步的采用深度学习的方式，包括基于mobilenet-ssd的算法进行检测(https://gitee.com/zeusees/Mobilenet-SSD-License-Plate-Detection) ，基于Retinaface框架进行检测（ https://gitee.com/zeusees/license-plate-detector ），后续请尽量采用新模型进行测试。

该版本的检测模型的训练，结合了CCPD数据集跟我们自有的数据，能够做到更多车牌种类的支持。

### Pytorch模型测试
##### Clone and install
1. git clone https://github.com/zeusees/License-Plate-Detector.git

2. Pytorch version 1.7.0 

3. Python 3.8

4. python detect_plate.py


### 基于C++的NCNN模型测试
##### Source Code Compile
1. cd Prj-ncnn

2. cmake .

3. make


### 支持车牌种类

- 蓝色单层车牌
- 黄色单层车牌
- 绿色新能源车牌、民航车牌
- 黑色单层车牌
- 白色警牌、军牌、武警车牌
- 黄色双层车牌
- 绿色农用车牌
- 白色双层军牌


### 测试结果

![](imgs/res.jpg)


### 参考
- [基于OpenCV和ONNXRuntime工程](https://github.com/hpc203/yolov5-detect-car_plate_corner)
- [yolov5-face](https://github.com/deepcam-cn/yolov5-face)
- [CCPD](https://github.com/detectRecog/CCPD)

