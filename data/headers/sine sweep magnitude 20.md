# sine sweep magnitude 20.abf

## ABF Class Methods

* abf.launchInClampFit()
* abf.saveABF1()
* abf.setSweep()
* abf.sweepD()

## ABF Class Variables

* abfDateTime = `2013-12-17 15:27:56.218000`
* abfDateTimeString = `2013-12-17T15:27:56.218`
* abfFileComment = ``
* abfFilePath = `C:/some/path/to/sine sweep magnitude 20.abf`
* abfFolderPath = `C:/some/path`
* abfID = `sine sweep magnitude 20`
* abfVersion = `{'major': 2, 'minor': 0, 'bugfix': 0, 'build': 0}`
* abfVersionString = `2.0.0.0`
* adcNames = `['IN 0']`
* adcUnits = `['?']`
* channelCount = `1`
* channelList = `[0]`
* creator = `clampex 10.2.0.14`
* creatorVersion = `{'major': 10, 'minor': 2, 'bugfix': 0, 'build': 14}`
* creatorVersionString = `10.2.0.14`
* dacNames = `['Cmd 0']`
* dacUnits = `['mV']`
* data = `array (2d) with values like: 0.00000, 0.00000, 0.00001, ..., 15.83387, 16.07412, 16.31025`
* dataByteStart = `3584`
* dataLengthMin = `0.16666666666666666`
* dataLengthSec = `10.0`
* dataPointByteSize = `4`
* dataPointCount = `100000`
* dataPointsPerMs = `10`
* dataRate = `10000`
* dataSecPerPoint = `0.0001`
* fileGUID = `FA90BECA-056E-4757-9776-ADFD6095348D`
* fileUUID = `B6743DB6-39EC-4F7B-E616-3F90C65DD941`
* holdingCommand = `[-70.0, 0.0, 0.0, 0.0]`
* md5 = `B6743DB639EC4F7BE6163F90C65DD941`
* nOperationMode = `5`
* protocol = `None`
* protocolPath = `None`
* stimulusByChannel = `[Stimulus(abf, 0)]`
* stimulusFileFolder = `C:/some/path/to/sine sweep magnitude 20.abf`
* sweepC = `array (1d) with values like: -70.00000, -70.00000, -70.00000, ..., -70.00000, -70.00000, -70.00000`
* sweepChannel = `0`
* sweepCount = `1`
* sweepDerivative = `array (1d) with values like: 0.02000, 0.06000, 0.10000, ..., 2402.49634, 2361.33569, 2361.33569`
* sweepEpochs = `Sweep epoch waveform: Step -70.00 [0:1562], Step -70.00 [1562:100000]`
* sweepIntervalSec = `10.0`
* sweepLabelC = `Cmd 0 (mV)`
* sweepLabelD = `Digital Output (V)`
* sweepLabelX = `Time (seconds)`
* sweepLabelY = `IN 0 (?)`
* sweepLengthSec = `10.0`
* sweepList = `[0]`
* sweepNumber = `0`
* sweepPointCount = `100000`
* sweepTimesMin = `array (1d) with values like: 0.00000`
* sweepTimesSec = `array (1d) with values like: 0.00000`
* sweepUnitsC = `mV`
* sweepUnitsX = `sec`
* sweepUnitsY = `?`
* sweepX = `array (1d) with values like: 0.00000, 0.00010, 0.00020, ..., 9.99970, 9.99980, 9.99990`
* sweepY = `array (1d) with values like: 0.00000, 0.00000, 0.00001, ..., 15.83387, 16.07412, 16.31025`
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
                    EPOCH
                     Type
              First Level
              Delta Level
  First Duration (points)
  Delta Duration (points)
     Digital Pattern #3-0
     Digital Pattern #7-4
    Train Period (points)
     Pulse Width (points)
```

## ABF2 Header

> The first several bytes of an ABF2 file contain variables     located at specific byte positions from the start of the file. 

* abfDateTime = `2013-12-17 15:27:56.218000`
* abfDateTimeString = `2013-12-17T15:27:56.218`
* abfVersionDict = `{'major': 2, 'minor': 0, 'bugfix': 0, 'build': 0}`
* abfVersionFloat = `2.0`
* abfVersionString = `2.0.0.0`
* creatorVersionDict = `{'major': 10, 'minor': 2, 'bugfix': 0, 'build': 14}`
* creatorVersionFloat = `102.014`
* creatorVersionString = `10.2.0.14`
* fFileVersionNumber = `[0, 0, 0, 2]`
* lActualEpisodes = `1`
* nCRCEnable = `0`
* nDataFormat = `1`
* nFileType = `1`
* nSimultaneousScan = `1`
* sFileGUID = `FA90BECA-056E-4757-9776-ADFD6095348D`
* sFileSignature = `ABF2`
* uCreatorNameIndex = `1`
* uCreatorVersion = `[14, 0, 2, 10]`
* uFileCRC = `0`
* uFileGUID = `[202, 190, 144, 250, 110, 5, 87, 71, 151, 118, 173, 253, 96, 149, 52, 141]`
* uFileInfoSize = `512`
* uFileStartDate = `20131217`
* uFileStartTimeMS = `55676218`
* uModifierNameIndex = `2`
* uModifierVersion = `167903246`
* uProtocolPathIndex = `3`
* uStopwatchTime = `696`

## SectionMap

> Reading three numbers (int, int, long) at specific byte locations     yields the block position, byte size, and item count of specific     data stored in sections. Note that a block is 512 bytes. Some of     these sections are not read by this class because they are either     not useful for my applications, typically unused, or have an     unknown memory structure. 

* ADCPerDACSection = `[0, 0, 0]`
* ADCSection = `[2, 128, 1]`
* AnnotationSection = `[0, 0, 0]`
* DACSection = `[3, 256, 4]`
* DataSection = `[7, 4, 100000]`
* DeltaSection = `[0, 0, 0]`
* EpochPerDACSection = `[0, 0, 0]`
* EpochSection = `[0, 0, 0]`
* MathSection = `[0, 0, 0]`
* ProtocolSection = `[1, 512, 1]`
* ScopeSection = `[0, 0, 0]`
* StatsRegionSection = `[5, 128, 1]`
* StatsSection = `[0, 0, 0]`
* StringsSection = `[6, 113, 12]`
* SynchArraySection = `[789, 8, 1]`
* TagSection = `[0, 0, 0]`
* UserListSection = `[0, 0, 0]`
* VoiceTagSection = `[0, 0, 0]`

## ProtocolSection

> This section contains information about the recording settings.     This is useful for determining things like sample rate and     channel scaling factors. 

* bEnableFileCompression = `0`
* fADCRange = `10.0`
* fADCSequenceInterval = `100.0`
* fAverageWeighting = `0.10000000149011612`
* fCellID = `[0.0, 0.0, 0.0]`
* fDACRange = `10.0`
* fEpisodeStartToStart = `0.0`
* fFirstRunDelayS = `0.0`
* fRunStartToStart = `0.0`
* fScopeOutputInterval = `0.0`
* fSecondsPerRun = `10.0`
* fStatisticsPeriod = `1.0`
* fSynchTimeUnit = `20.0`
* fTrialStartToStart = `0.0`
* fTriggerThreshold = `0.0`
* lADCResolution = `32768`
* lAverageCount = `1`
* lDACResolution = `32768`
* lEpisodesPerRun = `1`
* lFileCommentIndex = `0`
* lFinishDisplayNum = `0`
* lNumSamplesPerEpisode = `100000`
* lNumberOfTrials = `1`
* lPreTriggerSamples = `20`
* lRunsPerTrial = `1`
* lSamplesPerTrace = `16384`
* lStartDisplayNum = `1`
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
* nManualInfoStrategy = `0`
* nOperationMode = `5`
* nScopeTriggerOut = `0`
* nShowPNRawData = `0`
* nSignalType = `0`
* nStatisticsClearStrategy = `0`
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

* bEnabledDuringPN = `[0]`
* fADCDisplayAmplification = `[1.0]`
* fADCDisplayOffset = `[0.0]`
* fADCProgrammableGain = `[1.0]`
* fInstrumentOffset = `[0.0]`
* fInstrumentScaleFactor = `[0.0005000000237487257]`
* fPostProcessLowpassFilter = `[100000.0]`
* fSignalGain = `[1.0]`
* fSignalHighpassFilter = `[1.0]`
* fSignalLowpassFilter = `[5000.0]`
* fSignalOffset = `[0.0]`
* fTelegraphAccessResistance = `[0.0]`
* fTelegraphAdditGain = `[10.0]`
* fTelegraphFilter = `[2000.0]`
* fTelegraphMembraneCap = `[0.0]`
* lADCChannelNameIndex = `[4]`
* lADCUnitsIndex = `[0]`
* nADCNum = `[0]`
* nADCPtoLChannelMap = `[0]`
* nADCSamplingSeq = `[0]`
* nHighpassFilterType = `[0]`
* nLowpassFilterType = `[0]`
* nPostProcessLowpassFilterType = `['\x00']`
* nStatsChannelPolarity = `[0]`
* nTelegraphEnable = `[1]`
* nTelegraphInstrument = `[24]`
* nTelegraphMode = `[0]`
* sTelegraphInstrument = `['MultiClamp 700']`

## DACSection

> Information about the DAC (what gets clamped).     There is 1 item per DAC. 

* fBaselineDuration = `[1.0, 1.0, 1.0, 1.0]`
* fBaselineLevel = `[0.0, 0.0, 0.0, 0.0]`
* fDACCalibrationFactor = `[1.0008957386016846, 1.001062273979187, 1.0010067224502563, 1.0009512901306152]`
* fDACCalibrationOffset = `[1.0, -1.0, -3.0, 1.0]`
* fDACFileOffset = `[0.0, 0.0, 0.0, 0.0]`
* fDACFileScale = `[1.0, 1.0, 1.0, 1.0]`
* fDACHoldingLevel = `[-70.0, 0.0, 0.0, 0.0]`
* fDACScaleFactor = `[20.0, 20.0, 20.0, 20.0]`
* fInstrumentHoldingLevel = `[0.0, 0.0, 0.0, 0.0]`
* fMembTestPostSettlingTimeMS = `[100.0, 100.0, 100.0, 100.0]`
* fMembTestPreSettlingTimeMS = `[100.0, 100.0, 100.0, 100.0]`
* fPNHoldingLevel = `[0.0, 0.0, 0.0, 0.0]`
* fPNInterpulse = `[0.0, 0.0, 0.0, 0.0]`
* fPNSettlingTime = `[100.0, 100.0, 100.0, 100.0]`
* fPostTrainLevel = `[0.0, 0.0, 0.0, 0.0]`
* fPostTrainPeriod = `[10.0, 10.0, 10.0, 10.0]`
* fStepDuration = `[1.0, 1.0, 1.0, 1.0]`
* fStepLevel = `[0.0, 0.0, 0.0, 0.0]`
* lConditNumPulses = `[0, 0, 0, 0]`
* lDACChannelNameIndex = `[5, 7, 9, 11]`
* lDACChannelUnitsIndex = `[6, 8, 10, 12]`
* lDACFileEpisodeNum = `[0, 0, 0, 0]`
* lDACFileNumEpisodes = `[0, 0, 0, 0]`
* lDACFilePathIndex = `[0, 0, 0, 0]`
* lDACFilePtr = `[0, 0, 0, 0]`
* nConditEnable = `[0, 0, 0, 0]`
* nDACFileADCNum = `[0, 0, 0, 0]`
* nDACNum = `[0, 1, 2, 3]`
* nInterEpisodeLevel = `[0, 0, 0, 0]`
* nLTPPresynapticPulses = `[0, 0, 0, 0]`
* nLTPUsageOfDAC = `[0, 0, 0, 0]`
* nLeakSubtractADCIndex = `[0, 0, 0, 0]`
* nLeakSubtractType = `[0, 0, 0, 0]`
* nMembTestEnable = `[0, 0, 0, 0]`
* nPNNumADCChannels = `[0, 0, 0, 0]`
* nPNNumPulses = `[4, 4, 4, 4]`
* nPNPolarity = `[1, 1, 1, 1]`
* nPNPosition = `[0, 0, 0, 0]`
* nTelegraphDACScaleFactorEnable = `[1, 1, 0, 0]`
* nWaveformEnable = `[1, 0, 0, 0]`
* nWaveformSource = `[1, 1, 1, 1]`

## EpochPerDACSection

> This section contains waveform protocol information. These are most of     the values set when using the epoch the waveform editor. Note that digital     output signals are not stored here, but are in EpochSection. 

* fEpochInitLevel = `[]`
* fEpochLevelInc = `[]`
* lEpochDurationInc = `[]`
* lEpochInitDuration = `[]`
* lEpochPulsePeriod = `[]`
* lEpochPulseWidth = `[]`
* nDACNum = `[]`
* nEpochNum = `[]`
* nEpochType = `[]`

## EpochSection

> This section contains the digital output signals for each epoch. This     section has been overlooked by some previous open-source ABF-reading     projects. Note that the digital output is a single byte, but represents     8 bits corresponding to 8 outputs (7->0). When working with these bits,     I convert it to a string like "10011101" for easy eyeballing. 

* nEpochDigitalOutput = `[]`
* nEpochNum = `[]`

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

* lLength = `[100000]`
* lStart = `[0]`

## StringsSection

> Part of the ABF file contains long strings. Some of these can be broken     apart into indexed strings.      The first string is the only one which seems to contain useful information.     This contains information like channel names, channel units, and abf     protocol path and comments. The other strings are very large and I do not     know what they do.      Strings which contain indexed substrings are separated by \x00 characters. 

* strings = `not shown due to non-ASCII characters`

## StringsIndexed

> This object provides easy access to strings which are scattered around     the header files. The StringsSection contains strings, but various headers     contain values which point to a certain string index. This class connects     the two, and provides direct access to those strings by their indexed name. 

* indexedStrings = `['', 'clampex', 'clampfit', '(untitled)', 'IN 0', 'Cmd 0', 'mV', 'Cmd 1', 'mV', 'Cmd 2', 'mV', 'Cmd 3', 'mV', '']`
* lADCChannelName = `['IN 0']`
* lADCUnits = `['']`
* lDACChannelName = `['Cmd 0', 'Cmd 1', 'Cmd 2', 'Cmd 3']`
* lDACChannelUnits = `['mV', 'mV', 'mV', 'mV']`
* lDACFilePath = `['', '', '', '']`
* lFileComment = ``
* nLeakSubtractADC = `['', '', '', '']`
* uCreatorName = `clampex`
* uModifierName = `clampfit`
* uProtocolPath = `(untitled)`
