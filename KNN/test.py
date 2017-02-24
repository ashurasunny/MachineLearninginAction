import knn
import matplotlib
import matplotlib.pyplot as plt


def test2_1():
    group,labels = knn.createDataSet()
    print classify0([0,0],group,labels,3)


def test2_2_2():
    datingDataMat,datingLabels = knn.file2matrix('datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*np.array(datingLabels),15.0*np.array(datingLabels))
    plt. show()

def test2_2_3():
    datingDataMat, datingLabels = knn.file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = knn.autoNorm(datingDataMat)
    print 'normMat:',normMat
    print 'ranges:',ranges
    print 'minVals:',minVals