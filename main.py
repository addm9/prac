import numpy as np
from pandas.core.frame import DataFrame
import glob

X_train = []  # trainset
Y_train = []  # label of trainse
TestX_train = []  # testdset
TestY_train = []  # label of testsetimport numpy as np



def Inputdataset(X_train, Y_train, TestX_train, TestY_train):
    # --------import traindata--------------------------
    useless_train= 0
    XZ_train = []
    XF_train = []  # trainset with label0
    Set = []
    # input trainset with label1
    Path = r"/Users/peijialong/Desktop/MCSaut/python/label1"  # set path
    Set,useless=dataproc(Path, Set)
    XZ_train = Set
    # print(XZ_train.__len__())
    Y_train = Y_train + [[1]] * len(XZ_train)
    # print(Y_train.__len__())
    X_train = X_train + XZ_train
    useless_train= useless_train+useless
    Set = []
    Path = r"/Users/peijialong/Desktop/MCSaut/python/label0"  # set path
    Set,useless=dataproc(Path, Set)
    XF_train = Set
    # print(XF_train.__len__())
    Y_train = Y_train + [[0]] * len(XF_train)
    # print(Y_train.__len__())
    X_train = X_train + XF_train

    # transfor list into np.narray
    X_train = DataFrame(X_train)
    # print(X_train.shape)
    Y_train = np.array(Y_train)
    # print(Y_train.shape)
    useless_train= useless_train+useless

    # --------import testdata----------------------------

    TestXZ_train = []  # testset with label1
    TestXF_train = []  # testset with label0
    Set = []

    Path = r"/Users/peijialong/Desktop/MCSaut/python/testlabel1"  # set path
    Set,useless=dataproc(Path, Set)
    TestXZ_train = Set
    # print(XZ_train.__len__())
    TestY_train = TestY_train + [[1]] * len(TestXZ_train)
    # print(Y_train.__len__())
    TestX_train = TestX_train + TestXZ_train
    # print(len(TestX_train))

    Set = []
    Path = r"/Users/peijialong/Desktop/MCSaut/python/testlabel0"  # set path
    Set,useless=dataproc(Path, Set)
    TestXF_train = Set
    # print(XZ_train.__len__())
    TestY_train = TestY_train + [[0]] * len(TestXF_train)
    # print(Y_train.__len__())
    TestX_train = TestX_train + TestXF_train
    # print(len(TestX_train))

    # transfor list into np.narray
    TestX_train = DataFrame(TestX_train)
    # print(X_train.shape)
    TestY_train = np.array(TestY_train)
    # print(Y_train.shape)
    return X_train, Y_train, TestX_train, TestY_train, useless_train


def dataproc(path, Set, useless=0):
    dirs = glob.glob(path + '/*.txt')  # get all file in a folder
    #print(len(dirs))
    for i in dirs:  # Read the name of file and input
        train = np.loadtxt(open(i, "rb"), skiprows=0)
        # filter dataset not 7 lines
        if train.shape[0] == 7:
            # print(train[1:].shape, i)  # Print the dimensions of the matrix
            temp = train[1:]  # Remove attribute "time"
            # print(temp)
            # print(temp[:,:-1])
            if temp.shape[1] > 170:  # Remove row more than 170
                temp = temp[:, :170]
            temp = temp.flatten()  # Pull the data matrix into a vector
            mean, std = temp.mean(), temp.std()
            temp = ((temp - mean) / std)
            # print(temp)
            Set.append(list(temp))
        else:
            useless = useless + 1

    return Set,useless


X_train, Y_train, TestX_train, TestY_train, useless_train = Inputdataset(X_train, Y_train, TestX_train, TestY_train)
