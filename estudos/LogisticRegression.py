import random
import numpy as np
import matplotlib.pyplot as plt


class LogisticRegression:
    def __init__(self, dataFilePath, outputPath, alpha=0.01, maxIter=500, threshold=0.5,
                 errorThreshold=0.001):
        self.dataFilePath = dataFilePath
        self.outputPath = outputPath
        self.alpha = alpha
        self.maxIter = maxIter
        self.errorThreshold = errorThreshold
        self.threshold = threshold

        self.loadDataFromFile()
        self.initWeights()

    def loadDataFromFile(self):
        datasetLoaded = np.loadtxt(self.dataFilePath, delimiter=",")
        self.nExamples = datasetLoaded.shape[0]
        self.nAttributes = len(datasetLoaded[0])

        self.dataset = np.ones(shape=(self.nExamples, self.nAttributes))
        self.dataset[:, 1:] = datasetLoaded[:, :-1]
        self.target = datasetLoaded[:, -1]
        self.target.shape = (self.nExamples, 1)

    def initWeights(self):
        # THETA = [THETA0, THETA1, THETA2, ... , THETA9] - transposto
        self.weights = np.zeros(shape=(self.nAttributes, 1))
        for i in range(0, self.nAttributes):
            self.weights[i][0] = random.random()

    def sigmoidFunction(self):
        linearFunction = self.dataset.dot(self.weights)  # THETA(t) * x
        sigmoidFunction = (1.0 / (1 + np.exp(-linearFunction)))
        return sigmoidFunction

    def calculateCost(self):
        output = self.sigmoidFunction()
        cost = self.target * np.log(output) + (1 - self.target) * np.log(1 - output)
        cost = -np.average(cost)
        return cost

    def calculateError(self):
        output = self.sigmoidFunction()
        error = output - self.target
        return error

    def gradientDescent(self):
        error = self.calculateError()
        for i in range(self.nAttributes):
            temp = self.dataset[:, i]
            temp.shape = (self.nExamples, 1)
            currentErrors = error * temp
            self.weights[i][0] = self.weights[i][0] - self.alpha * (1.0 / self.nExamples) * currentErrors.sum()

    def classifyData(self, originalPoint):
        originalPoint.insert(0, 1)
        point = np.array(originalPoint)
        linearFunction = point.dot(self.weights)
        sigmoidFunction = (1.0 / (1 + np.exp(-linearFunction)))

        if sigmoidFunction >= self.threshold:
            output = 1
        else:
            output = 0

        return output

    def plotCostGraph(self, errorsList):

        xAxisValues = range(0, self.maxIter + 1)
        plt.plot(xAxisValues, errorsList)
        plt.xlabel("Iteration")
        plt.ylabel("Mean Absolute Error")
        plt.savefig(self.outputPath + "/error_logreg.png")
        plt.show()

    def run(self):
        cost = self.calculateCost()
        count = 0
        errors = list()
        errors.append(abs(cost))
        print(cost)

        while abs(cost) > self.errorThreshold and count < self.maxIter:
            self.gradientDescent()
            count += 1
            cost = self.calculateCost()
            errors.append(abs(cost))
            print(cost)

        print(self.weights)
        self.plotCostGraph(errors)


if __name__ == '__main__':
    logReg = LogisticRegression("./breast-cancer-wisconsin-modified.csv",
                                "./graficos/bcw",
                                maxIter=2000, threshold=0.5, alpha=0.001)
    logReg.run()

    data_to_classify = [[1, 1, 1, 1, 2, 1, 1, 1, 8, 0], [1, 1, 1, 3, 2, 1, 1, 1, 1, 0],
                        [5, 10, 10, 5, 4, 5, 4, 4, 1, 1], [3, 1, 1, 1, 2, 1, 1, 1, 1, 0],
                        [3, 1, 1, 1, 2, 1, 2, 1, 2, 0], [3, 1, 1, 1, 3, 2, 1, 1, 1, 0],
                        [2, 1, 1, 1, 2, 1, 1, 1, 1, 0], [5, 10, 10, 3, 7, 3, 8, 10, 2, 1],
                        [4, 8, 6, 4, 3, 4, 10, 6, 1, 1], [4, 8, 8, 5, 4, 5, 10, 4, 1, 1]]
    count = 1
    for data in data_to_classify:
        result_class = logReg.classifyData(data[:-1])
        print("RESULT: " + str(result_class) + " - REAL: " + str(data[-1]))
