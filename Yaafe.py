# -*- coding:utf-8 -*-

from yaafelib import FeaturePlan, Engine, AudioFileProcessor
import essentia


def init():
    global engine
    fp = FeaturePlan(sample_rate=44100, resample=True
                    # , time_start=20, time_limit=40
                     )  # 采样率
    fp.addFeature('mfcc:MFCC')  # MFCC
    fp.addFeature("energy:Energy")  # 能量
    fp.addFeature("zcr:ZCR")  # 过零率
    fp.addFeature("lpc:LPC")  # LPC线性预测系数
    fp.addFeature("mfcc_d1: MFCC blockSize=1024 stepSize=512 > Derivate DOrder=1")  # MFCC一阶倒数
    fp.addFeature("sharpness:PerceptualSharpness")
    fp.addFeature("spectralRolloff: SpectralRolloff")  # 谱流量
    fp.addFeature("spectralFlatness: SpectralFlatness")  # 谱平坦度
    # fp.addFeature("lsf:LSF blockSize=1024  stepSize=512")

    df = fp.getDataFlow()
    engine = Engine()
    engine.load(df)
    print "初始化"


def startEngine(path):
    global afp, featureYaafe, featureEssentia
    afp = AudioFileProcessor()
    afp.processFile(engine, path)

    featureYaafe = engine.readAllOutputs()

    print "Yaafe提取成功"


def getMFCC():
    mfcc = featureYaafe.get('mfcc')

    mfccMean = mfcc.mean(axis=0)  # 平均数
    mfccMean = mfccMean.reshape(-1)

    mfccVar = mfcc.var(axis=0)  # 方差
    mfccVar = mfccVar.reshape(-1, )

    mfccMax = mfcc.max(axis=0)  # 最大值
    mfccMax = mfccMax.reshape(-1, )

    print "MFCC"
    print "平均值:", mfccMean
    print "方差:", mfccVar
    print "最大值:", mfccMax


def getLPC():
    lpc = featureYaafe.get('lpc')
    lpcMean = lpc.mean(axis=0)  # 均值
    lpcVar = lpc.var(axis=0)  # 方差

    print "LPC"
    print "均值：", lpcMean
    print "方差：", lpcVar


def getZCR():
    zcr = featureYaafe.get("zcr")

    zcrMean = zcr.mean(axis=0)  # 均值
    zcrVar = zcr.var(axis=0)  # 方差

    print "ZCR"
    print "均值：", zcrMean
    print "方差：", zcrVar


def getFeature(MusicInfo):
    fn = MusicInfo
    if fn == 'MFCC':
        return featureYaafe.get('mfcc').T
    elif fn == 'LPC':
        return featureYaafe.get('lpc').T
    elif fn == 'MFCC_D1':
        return featureYaafe.get("mfcc_d1").T
    elif fn == 'Sharpness':
        return featureYaafe.get("sharpness").T
    elif fn == "ZCR":
        return featureYaafe.get("zcr").T
    elif fn == "Energy":
        return featureYaafe.get("energy").T
    elif fn == "SpectralRolloff":
        return featureYaafe.get("spectralRolloff").T
    elif fn == "spectralFlatness":
        return featureYaafe.get("spectralFlatness").T
    else:
        return None
