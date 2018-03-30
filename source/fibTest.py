import xlrd


def loadDataSet():
    '''
    输入：无
    功能：产生简单的数据集
    输出：dataset
    '''
    workbook = xlrd.open_workbook(r'D://Apriori_backup.xlsx')
    sheet1 = workbook.sheet_by_name('Sheet1')

    print(sheet1.nrows)
    d = {sheet1.cell(0, 0).value: [sheet1.cell(0, 1).value]}
    for i in range(1,sheet1.nrows):
        a = set()
        order_id = sheet1.cell(i, 0).value
        item_id = sheet1.cell(i, 1).value
        if order_id in d.keys():
            print(type(d[order_id]))
            a = set(d[order_id])
            a.add(item_id)

            d[order_id].append(list(a))
        else:
            d[order_id] = list(a)
    print(d)
    print("=================================================")
    tmp = []
    for i in d.values():
        tmp.append(i)
    print(tmp[:2])
    return tmp


def createC1(dataset):
    '''
    输入：数据集
    功能：产生类似[[1], [2], [3], [4], [5]]，C1中包含的元素为数据集中出现的元素
    输出：C1
    '''
    C1 = []
    for transction in dataset:
        # print transction
        for item in transction:
            if not [item] in C1:
                C1.append([item])  # 使用列表作为C1元素是因为后续需要使用集合操作
    C1.sort()
    return map(frozenset, C1)


def scanDataSet(DataSet, Ck, minSupport):
    '''
    输入：DataSet应为每条记录是set类型数据（被用于判断是否是其子集操作），Ck中的每个项集为frozenset型数据（被用于字典关键字）
         Ck为候选频繁项集，minSupport为判断是否为频繁项集的最小支持度（认为给定）
    功能：从候选项集中找出支持度support大于minSupport的频繁项集
    输出：频繁项集集合returnList,以及频繁项集对应的支持度support
    '''
    subSetCount = {}
    for transction in DataSet:  # 取出数据集dataset中的每行记录
        for subset in Ck:  # 取出候选频繁项集Ck中的每个项集
            if subset.issubset(transction):  # 判断Ck中项集是否是数据集每条记录数据集合中的子集
                if not subSetCount.has_key(subset):
                    subSetCount[subset] = 1
                else:
                    subSetCount[subset] += 1
    numItem = float(len(DataSet))
    returnList = []
    returnSupportData = {}
    for key in subSetCount:
        support = subSetCount[key] / numItem
        if support >= minSupport:
            returnList.insert(0, key)
            returnSupportData[key] = support
    return returnList, returnSupportData


def createCk(Lk, k):
    returnList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2];
            L2 = list(Lk[j])[:k - 2]
            L1.sort();
            L2.sort()
            if L1 == L2:  # 只需取前k-2个元素相等的候选频繁项集即可组成元素个数为k+1的候选频繁项集！！
                returnList.append(Lk[i] | Lk[j])
    return returnList


def apriori(dataset, minSupport=0.5):
    C1 = createC1(dataset)
    DataSet = map(set, dataset)
    L1, returnSupportData = scanDataSet(DataSet, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        # 由上一时刻的频繁项集Lk-1，两两组合形成下一时刻没有重复的频繁项集，下一时刻候选频繁项集中元素个数会比上一时刻的多1
        Ck = createCk(L[k - 2], k)
        # 从候选频繁项集中选出支持度大于minsupport的频繁项集Lk
        Lk, supportLk = scanDataSet(DataSet, Ck, minSupport)
        # 将该频繁项集及其支持度添加到returnSupportData字典中记录，其中频繁项集为关键字，支持度为关键字所对应的项
        returnSupportData.update(supportLk)
        # 将频繁项集添加到列表L中记录
        L.append(Lk)
        # 逐一增加频繁项集中的元素个数
        k += 1
    return L, returnSupportData


# ------------------关联规则生成函数--------------#
def generateRules(L, supportData, minConference=0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        for subSet in L[i]:
            H1 = [frozenset([item]) for item in subSet]
            if (i > 1):
                rulesFromConseq(subSet, H1, supportData, bigRuleList, minConference)
            else:
                calculationConf(subSet, H1, supportData, bigRuleList, minConference)
    return bigRuleList


def calculationConf(subSet, H, supportData, brl, minConference=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[subSet] / supportData[subSet - conseq]
    if conf >= minConference:
        print(subSet - conseq, '-->', conseq, 'conf:', conf)
        brl.append((subSet - conseq, conseq, conf))
        prunedH.append(conseq)
    return prunedH


def rulesFromConseq(subSet, H, supportData, brl, minConference):
    m = len(H[0])
    # 如果频繁项集中每项元素个数大于买m+1,即，可以分出m+1个元素在规则等式右边则执行
    if (len(subSet) > (m + 1)):
        # 利用函数createCk生成包含m+1个元素的候选频繁项集后件
        Hm = createCk(H, (m + 1))
        # 计算前件（subSet - Hm）--> 后件（Hm）的可信度，并返回可信度大于minConference的后件
        Hm = calculationConf(subSet, Hm, supportData, brl, minConference)
        # 当候选后件集合中只有一个后件的可信度大于最小可信度，则结束递归创建规则
        if (len(Hm) > 1):
            rulesFromConseq(subSet, Hm, supportData, brl, minConference)


# ------------------关联规则生成函数end--------------#
if __name__ == '__main__':
    dataset = loadDataSet()
    L, returnSupportData = apriori(dataset, minSupport=0.5)
    rule = generateRules(L, returnSupportData, minConference=0.5)
