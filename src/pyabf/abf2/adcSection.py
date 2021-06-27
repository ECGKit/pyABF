from pyabf.abf2.section import Section
from pyabf.names import getTelegraphName


class ADCSection(Section):
    """
    Information about the ADC (what gets recorded).
    There is 1 item per ADC.
    """

    def __init__(self, fb):
        Section.__init__(self, fb, 92)

        self.nADCNum = [None]*self._entryCount
        self.nTelegraphEnable = [None]*self._entryCount
        self.nTelegraphInstrument = [None]*self._entryCount
        self.sTelegraphInstrument = [None]*self._entryCount
        self.fTelegraphAdditGain = [None]*self._entryCount
        self.fTelegraphFilter = [None]*self._entryCount
        self.fTelegraphMembraneCap = [None]*self._entryCount
        self.nTelegraphMode = [None]*self._entryCount
        self.fTelegraphAccessResistance = [None]*self._entryCount
        self.nADCPtoLChannelMap = [None]*self._entryCount
        self.nADCSamplingSeq = [None]*self._entryCount
        self.fADCProgrammableGain = [None]*self._entryCount
        self.fADCDisplayAmplification = [None]*self._entryCount
        self.fADCDisplayOffset = [None]*self._entryCount
        self.fInstrumentScaleFactor = [None]*self._entryCount
        self.fInstrumentOffset = [None]*self._entryCount
        self.fSignalGain = [None]*self._entryCount
        self.fSignalOffset = [None]*self._entryCount
        self.fSignalLowpassFilter = [None]*self._entryCount
        self.fSignalHighpassFilter = [None]*self._entryCount
        self.nLowpassFilterType = [None]*self._entryCount
        self.nHighpassFilterType = [None]*self._entryCount
        self.fPostProcessLowpassFilter = [None]*self._entryCount
        self.nPostProcessLowpassFilterType = [None]*self._entryCount
        self.bEnabledDuringPN = [None]*self._entryCount
        self.nStatsChannelPolarity = [None]*self._entryCount
        self.lADCChannelNameIndex = [None]*self._entryCount
        self.lADCUnitsIndex = [None]*self._entryCount

        for i in range(self._entryCount):
            fb.seek(self._byteStart + i*self._entrySize)
            self.nADCNum[i] = self.readInt16()  # 0
            self.nTelegraphEnable[i] = self.readInt16()  # 2
            self.nTelegraphInstrument[i] = self.readInt16()  # 4
            self.fTelegraphAdditGain[i] = self.readShort()  # 6
            self.fTelegraphFilter[i] = self.readShort()  # 10
            self.fTelegraphMembraneCap[i] = self.readShort()  # 14
            self.nTelegraphMode[i] = self.readInt16()  # 18
            self.fTelegraphAccessResistance[i] = self.readShort()  # 20
            self.nADCPtoLChannelMap[i] = self.readInt16()  # 24
            self.nADCSamplingSeq[i] = self.readInt16()  # 26
            self.fADCProgrammableGain[i] = self.readShort()  # 28
            self.fADCDisplayAmplification[i] = self.readShort()  # 32
            self.fADCDisplayOffset[i] = self.readShort()  # 36
            self.fInstrumentScaleFactor[i] = self.readShort()  # 40
            self.fInstrumentOffset[i] = self.readShort()  # 44
            self.fSignalGain[i] = self.readShort()  # 48
            self.fSignalOffset[i] = self.readShort()  # 52
            self.fSignalLowpassFilter[i] = self.readShort()  # 56
            self.fSignalHighpassFilter[i] = self.readShort()  # 60
            self.nLowpassFilterType[i] = self.readByte()  # 64
            self.nHighpassFilterType[i] = self.readByte()  # 65
            self.fPostProcessLowpassFilter[i] = self.readShort()  # 66
            self.nPostProcessLowpassFilterType[i] = self.readChar()  # 70
            self.bEnabledDuringPN[i] = self.readByte()  # 71
            self.nStatsChannelPolarity[i] = self.readInt16()  # 72
            self.lADCChannelNameIndex[i] = self.readInt32()  # 74
            self.lADCUnitsIndex[i] = self.readInt32()  # 78

            self.sTelegraphInstrument[i] =\
                getTelegraphName(self.nTelegraphInstrument[i])
