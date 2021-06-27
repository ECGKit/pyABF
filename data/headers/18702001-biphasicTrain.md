# 18702001-biphasicTrain.abf

## ABF Class Methods

* abf.launchInClampFit()
* abf.saveABF1()
* abf.setSweep()
* abf.sweepD()

## ABF Class Variables

* abfDateTime = `2018-07-02 09:30:03.526000`
* abfDateTimeString = `2018-07-02T09:30:03.526`
* abfFileComment = ``
* abfFilePath = `C:/some/path/to/18702001-biphasicTrain.abf`
* abfFolderPath = `C:/some/path`
* abfID = `18702001-biphasicTrain`
* abfVersion = `{'major': 2, 'minor': 6, 'bugfix': 0, 'build': 0}`
* abfVersionString = `2.6.0.0`
* adcNames = `['IN 0', 'IN 1']`
* adcUnits = `['pA', 'A']`
* channelCount = `2`
* channelList = `[0, 1]`
* creator = `Clampex 10.7.0.3`
* creatorVersion = `{'major': 10, 'minor': 7, 'bugfix': 0, 'build': 3}`
* creatorVersionString = `10.7.0.3`
* dacNames = `['Cmd 0', 'Cmd 1']`
* dacUnits = `['mV', 'mV']`
* data = `array (2d) with values like: -10.74219, -10.98633, -10.98633, ..., -1.03577, -1.03607, -1.03546`
* dataByteStart = `6656`
* dataLengthMin = `0.06666666666666667`
* dataLengthSec = `4.0`
* dataPointByteSize = `2`
* dataPointCount = `120000`
* dataPointsPerMs = `20`
* dataRate = `20000`
* dataSecPerPoint = `5e-05`
* fileGUID = `452C5D61-DBF2-4EC4-B403-D74EBE8FE65D`
* fileUUID = `C98B845B-396A-046F-D1A6-45E1918E7A67`
* holdingCommand = `[-70.0, -10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* md5 = `C98B845B396A046FD1A645E1918E7A67`
* nOperationMode = `5`
* protocol = `0201 memtest`
* protocolPath = `\\Spike\locked\Protocols\permanent\0201 memtest.pro`
* stimulusByChannel = `[Stimulus(abf, 0), Stimulus(abf, 1)]`
* stimulusFileFolder = `C:/some/path/to/18702001-biphasicTrain.abf`
* sweepC = `array (1d) with values like: -70.00000, -70.00000, -70.00000, ..., -70.00000, -70.00000, -70.00000`
* sweepChannel = `0`
* sweepCount = `3`
* sweepDerivative = `array (1d) with values like: -4882.81250, 0.00000, -17089.84375, ..., -19531.25000, -21972.65625, -21972.65625`
* sweepEpochs = `Sweep epoch waveform: Step -70.00 [0:312], Step -80.00 [312:4312], Step -70.00 [4312:8312], Ramp -80.00 [8312:9312], Ramp -70.00 [9312:10312], Step -70.00 [10312:20000]`
* sweepIntervalSec = `1.0`
* sweepLabelC = `Membrane Potential (mV)`
* sweepLabelD = `Digital Output (V)`
* sweepLabelX = `Time (seconds)`
* sweepLabelY = `Clamp Current (pA)`
* sweepLengthSec = `1.0`
* sweepList = `[0, 1, 2]`
* sweepNumber = `0`
* sweepPointCount = `20000`
* sweepTimesMin = `array (1d) with values like: 0.00000, 0.01667, 0.03333`
* sweepTimesSec = `array (1d) with values like: 0.00000, 1.00000, 2.00000`
* sweepUnitsC = `mV`
* sweepUnitsX = `sec`
* sweepUnitsY = `pA`
* sweepX = `array (1d) with values like: 0.00000, 0.00005, 0.00010, ..., 0.99985, 0.99990, 0.99995`
* sweepY = `array (1d) with values like: -10.74219, -10.98633, -10.98633, ..., -9.03320, -10.00976, -11.10840`
* tagComments = `[]`
* tagSweeps = `[]`
* tagTimesMin = `[]`
* tagTimesSec = `[]`
* userList = `None`
* userListEnable = `[]`
* userListParamToVary = `[]`
* userListParamToVaryName = `[]`
* userListRepeat = `[]`

## Epochs for Channel 0


```
                    EPOCH         A         B         C         D
                     Type      Step      Step      Ramp      Ramp
              First Level    -80.00    -70.00    -80.00    -70.00
              Delta Level      0.00      0.00      0.00      0.00
  First Duration (points)      4000      4000      1000      1000
  Delta Duration (points)         0         0         0         0
     Digital Pattern #3-0      0000      0000      0000      0000
     Digital Pattern #7-4      0000      0000      0000      0000
    Train Period (points)         0         0         0         0
     Pulse Width (points)         0         0         0         0
```

## Epochs for Channel 1


```

```

## ABF2 Header

> The first several bytes of an ABF2 file contain variables     located at specific byte positions from the start of the file. 

* abfDateTime = `2018-07-02 09:30:03.526000`
* abfDateTimeString = `2018-07-02T09:30:03.526`
* abfVersionDict = `{'major': 2, 'minor': 6, 'bugfix': 0, 'build': 0}`
* abfVersionFloat = `2.6`
* abfVersionString = `2.6.0.0`
* creatorVersionDict = `{'major': 10, 'minor': 7, 'bugfix': 0, 'build': 3}`
* creatorVersionFloat = `10.703`
* creatorVersionString = `10.7.0.3`
* fFileVersionNumber = `[0, 0, 6, 2]`
* lActualEpisodes = `3`
* nCRCEnable = `0`
* nDataFormat = `0`
* nFileType = `1`
* nSimultaneousScan = `1`
* sFileGUID = `452C5D61-DBF2-4EC4-B403-D74EBE8FE65D`
* sFileSignature = `ABF2`
* uCreatorNameIndex = `1`
* uCreatorVersion = `[3, 0, 7, 10]`
* uFileCRC = `0`
* uFileGUID = `[97, 93, 44, 69, 242, 219, 196, 78, 180, 3, 215, 78, 190, 143, 230, 93]`
* uFileInfoSize = `512`
* uFileStartDate = `20180702`
* uFileStartTimeMS = `34203526`
* uModifierNameIndex = `0`
* uModifierVersion = `0`
* uProtocolPathIndex = `2`
* uStopwatchTime = `1611`

## SectionMap

> Reading three numbers (int, int, long) at specific byte locations     yields the block position, byte size, and item count of specific     data stored in sections. Note that a block is 512 bytes. Some of     these sections are not read by this class because they are either     not useful for my applications, typically unused, or have an     unknown memory structure. 

* ADCPerDACSection = `[0, 0, 0]`
* ADCSection = `[2, 128, 2]`
* AnnotationSection = `[0, 0, 0]`
* DACSection = `[3, 256, 8]`
* DataSection = `[13, 2, 120000]`
* DeltaSection = `[0, 0, 0]`
* EpochPerDACSection = `[7, 48, 7]`
* EpochSection = `[8, 32, 4]`
* MathSection = `[0, 0, 0]`
* ProtocolSection = `[1, 512, 1]`
* ScopeSection = `[11, 769, 1]`
* StatsRegionSection = `[9, 128, 1]`
* StatsSection = `[0, 0, 0]`
* StringsSection = `[10, 191, 22]`
* SynchArraySection = `[482, 8, 3]`
* TagSection = `[0, 0, 0]`
* UserListSection = `[0, 0, 0]`
* VoiceTagSection = `[0, 0, 0]`

## ProtocolSection

> This section contains information about the recording settings.     This is useful for determining things like sample rate and     channel scaling factors. 

* bEnableFileCompression = `0`
* fADCRange = `10.0`
* fADCSequenceInterval = `50.0`
* fAverageWeighting = `0.10000000149011612`
* fCellID = `[0.0, 0.0, 0.0]`
* fDACRange = `10.0`
* fEpisodeStartToStart = `0.0`
* fFirstRunDelayS = `0.0`
* fRunStartToStart = `0.0`
* fScopeOutputInterval = `0.0`
* fSecondsPerRun = `7200.0`
* fStatisticsPeriod = `1.0`
* fSynchTimeUnit = `6.25`
* fTrialStartToStart = `0.0`
* fTriggerThreshold = `0.0`
* lADCResolution = `32768`
* lAverageCount = `1`
* lDACResolution = `32768`
* lEpisodesPerRun = `3`
* lFileCommentIndex = `0`
* lFinishDisplayNum = `12000`
* lNumSamplesPerEpisode = `40000`
* lNumberOfTrials = `1`
* lPreTriggerSamples = `40`
* lRunsPerTrial = `1`
* lSamplesPerTrace = `40000`
* lStartDisplayNum = `0`
* lStatisticsMeasurements = `5`
* lTimeHysteresis = `1`
* nActiveDACChannel = `0`
* nAllowExternalTags = `0`
* nAlternateDACOutputState = `0`
* nAlternateDigitalOutputState = `0`
* nAutoAnalyseEnable = `1`
* nAutoTriggerStrategy = `1`
* nAverageAlgorithm = `0`
* nAveragingMode = `0`
* nChannelStatsStrategy = `0`
* nCommentsEnable = `0`
* nDigitalDACChannel = `0`
* nDigitalEnable = `0`
* nDigitalHolding = `0`
* nDigitalInterEpisode = `0`
* nDigitalTrainActiveLogic = `1`
* nDigitizerADCs = `16`
* nDigitizerDACs = `4`
* nDigitizerSynchDigitalOuts = `8`
* nDigitizerTotalDigitalOuts = `16`
* nDigitizerType = `6`
* nExperimentType = `2`
* nExternalTagType = `2`
* nFirstEpisodeInRun = `0`
* nLTPType = `0`
* nLevelHysteresis = `64`
* nManualInfoStrategy = `1`
* nOperationMode = `5`
* nScopeTriggerOut = `0`
* nShowPNRawData = `0`
* nSignalType = `0`
* nStatisticsClearStrategy = `1`
* nStatisticsDisplayStrategy = `0`
* nStatisticsSaveStrategy = `0`
* nStatsEnable = `0`
* nTrialTriggerSource = `-1`
* nTriggerAction = `0`
* nTriggerPolarity = `0`
* nTriggerSource = `-3`
* nUndoPromptStrategy = `0`
* nUndoRunCount = `0`
* sDigitizerType = `Digidata 1440`
* sUnused = `['\x00', '\x00', '\x00']`
* uFileCompressionRatio = `1`

## ADCSection

> Information about the ADC (what gets recorded).     There is 1 item per ADC. 

* bEnabledDuringPN = `[0, 0]`
* fADCDisplayAmplification = `[6.578846454620361, 1.0]`
* fADCDisplayOffset = `[4.0, 0.0]`
* fADCProgrammableGain = `[1.0, 1.0]`
* fInstrumentOffset = `[0.0, 0.0]`
* fInstrumentScaleFactor = `[0.0005000000237487257, 1.0]`
* fPostProcessLowpassFilter = `[100000.0, 100000.0]`
* fSignalGain = `[1.0, 1.0]`
* fSignalHighpassFilter = `[1.0, 1.0]`
* fSignalLowpassFilter = `[5000.0, 5000.0]`
* fSignalOffset = `[0.0, 0.0]`
* fTelegraphAccessResistance = `[0.0, 0.0]`
* fTelegraphAdditGain = `[5.0, 1.0]`
* fTelegraphFilter = `[2000.0, 1000.0]`
* fTelegraphMembraneCap = `[0.0, 0.0]`
* lADCChannelNameIndex = `[3, 5]`
* lADCUnitsIndex = `[4, 6]`
* nADCNum = `[0, 1]`
* nADCPtoLChannelMap = `[0, 1]`
* nADCSamplingSeq = `[0, 0]`
* nHighpassFilterType = `[0, 0]`
* nLowpassFilterType = `[0, 0]`
* nPostProcessLowpassFilterType = `['\x00', '\x00']`
* nStatsChannelPolarity = `[1, 0]`
* nTelegraphEnable = `[1, 0]`
* nTelegraphInstrument = `[24, 0]`
* nTelegraphMode = `[0, 0]`
* sTelegraphInstrument = `['MultiClamp 700', 'Unknown instrument (manual or user defined telegraph table).']`

## DACSection

> Information about the DAC (what gets clamped).     There is 1 item per DAC. 

* fBaselineDuration = `[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]`
* fBaselineLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACCalibrationFactor = `[1.001173496246338, 1.0012290477752686, 1.001173496246338, 1.001173496246338, 1.0, 1.0, 1.0, 1.0]`
* fDACCalibrationOffset = `[-4.0, -4.0, -7.0, -6.0, 0.0, 0.0, 0.0, 0.0]`
* fDACFileOffset = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACFileScale = `[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]`
* fDACHoldingLevel = `[-70.0, -10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fDACScaleFactor = `[20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]`
* fInstrumentHoldingLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fMembTestPostSettlingTimeMS = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fMembTestPreSettlingTimeMS = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fPNHoldingLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPNInterpulse = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPNSettlingTime = `[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]`
* fPostTrainLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* fPostTrainPeriod = `[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]`
* fStepDuration = `[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]`
* fStepLevel = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
* lConditNumPulses = `[1, 0, 0, 0, 0, 0, 0, 0]`
* lDACChannelNameIndex = `[7, 9, 11, 13, 15, 17, 19, 21]`
* lDACChannelUnitsIndex = `[8, 10, 12, 14, 16, 18, 20, 22]`
* lDACFileEpisodeNum = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFileNumEpisodes = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFilePathIndex = `[0, 0, 0, 0, 0, 0, 0, 0]`
* lDACFilePtr = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nConditEnable = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nDACFileADCNum = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nDACNum = `[0, 1, 2, 3, 4, 5, 6, 7]`
* nInterEpisodeLevel = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLTPPresynapticPulses = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLTPUsageOfDAC = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLeakSubtractADCIndex = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nLeakSubtractType = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nMembTestEnable = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nPNNumADCChannels = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nPNNumPulses = `[4, 4, 4, 4, 4, 4, 4, 4]`
* nPNPolarity = `[1, 1, 1, 1, 1, 1, 1, 1]`
* nPNPosition = `[0, 0, 0, 0, 0, 0, 0, 0]`
* nTelegraphDACScaleFactorEnable = `[1, 0, 0, 0, 0, 0, 0, 0]`
* nWaveformEnable = `[1, 1, 0, 0, 0, 0, 0, 0]`
* nWaveformSource = `[1, 1, 1, 1, 0, 0, 0, 0]`

## EpochPerDACSection

> This section contains waveform protocol information. These are most of     the values set when using the epoch the waveform editor. Note that digital     output signals are not stored here, but are in EpochSection. 

* fEpochInitLevel = `[-80.0, -70.0, -80.0, -70.0, -20.0, -10.0, 25.0]`
* fEpochLevelInc = `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10.0]`
* lEpochDurationInc = `[0, 0, 0, 0, 0, 0, 0]`
* lEpochInitDuration = `[4000, 4000, 1000, 1000, 1000, 4000, 10000]`
* lEpochPulsePeriod = `[0, 0, 0, 0, 0, 0, 1000]`
* lEpochPulseWidth = `[0, 0, 0, 0, 0, 0, 200]`
* nDACNum = `[0, 0, 0, 0, 1, 1, 1]`
* nEpochNum = `[0, 1, 2, 3, 0, 1, 2]`
* nEpochType = `[1, 1, 2, 2, 1, 1, 7]`

## EpochSection

> This section contains the digital output signals for each epoch. This     section has been overlooked by some previous open-source ABF-reading     projects. Note that the digital output is a single byte, but represents     8 bits corresponding to 8 outputs (7->0). When working with these bits,     I convert it to a string like "10011101" for easy eyeballing. 

* nEpochDigitalOutput = `[0, 0, 0, 0]`
* nEpochNum = `[0, 1, 2, 3]`

## TagSection

> Tags are comments placed in ABF files during the recording. Physically     they are located at the end of the file (after the data).      Later we will populate the times and sweeps (human-understandable units)     by multiplying the lTagTime by fSynchTimeUnit from the protocol section. 

* lTagTime = `[]`
* nTagType = `[]`
* nVoiceTagNumberorAnnotationIndex = `[]`
* sComment = `[]`
* sweeps = `[]`
* timesMin = `[]`
* timesSec = `[]`

## SynchArraySection

> Contains start time (in fSynchTimeUnit units) and length (in      multiplexed samples) of each portion of the data if the data      are not part of a continuous gap-free acquisition. 

* lLength = `[40000, 40000, 40000]`
* lStart = `[0, 160000, 320000]`

## StringsSection

> Part of the ABF file contains long strings. Some of these can be broken     apart into indexed strings.      The first string is the only one which seems to contain useful information.     This contains information like channel names, channel units, and abf     protocol path and comments. The other strings are very large and I do not     know what they do.      Strings which contain indexed substrings are separated by \x00 characters. 

* strings = `not shown due to non-ASCII characters`

## StringsIndexed

> This object provides easy access to strings which are scattered around     the header files. The StringsSection contains strings, but various headers     contain values which point to a certain string index. This class connects     the two, and provides direct access to those strings by their indexed name. 

* indexedStrings = `[, Clampex, \\Spike\locked\Protocols\permanent\0201 memtest.pro, ..., AO #7, mV, ]`
* lADCChannelName = `['IN 0', 'IN 1']`
* lADCUnits = `['pA', 'A']`
* lDACChannelName = `['Cmd 0', 'Cmd 1', 'Cmd 2', 'Cmd 3', 'AO #4', 'AO #5', 'AO #6', 'AO #7']`
* lDACChannelUnits = `['mV', 'mV', 'mV', 'mV', 'mV', 'mV', 'mV', 'mV']`
* lDACFilePath = `['', '', '', '', '', '', '', '']`
* lFileComment = ``
* nLeakSubtractADC = `['', '', '', '', '', '', '', '']`
* uCreatorName = `Clampex`
* uModifierName = ``
* uProtocolPath = `\\Spike\locked\Protocols\permanent\0201 memtest.pro`
