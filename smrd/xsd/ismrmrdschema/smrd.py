from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "http://www.ismrm.org/ISMRMRD"


@dataclass
class accelerationFactorType:
    kspace_encoding_step_1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    kspace_encoding_step_2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


class calibrationModeType(Enum):
    EMBEDDED = "embedded"
    INTERLEAVED = "interleaved"
    SEPARATE = "separate"
    EXTERNAL = "external"
    OTHER = "other"


@dataclass
class coilLabelType:
    coilNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    coilName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class diffusionGradientDirectionType:
    rl: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    ap: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    fh: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class experimentalConditionsType:
    H1resonanceFrequency_Hz: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    larmorConstantHzPerT: Optional[int] = field(
        default=None,
        metadata={
            "name": "LarmorConstant_Hz_Per_T",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class fieldOfViewMmType:
    class Meta:
        name = "fieldOfView_mmType"

    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


class interleavingDimensionType(Enum):
    PHASE = "phase"
    REPETITION = "repetition"
    CONTRAST = "contrast"
    AVERAGE = "average"
    OTHER = "other"


@dataclass
class limitType:
    minimum: int = field(
        default=0,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    maximum: int = field(
        default=0,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    center: int = field(
        default=0,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class matrixSizeType:
    x: int = field(
        default=1,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    y: int = field(
        default=1,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    z: int = field(
        default=1,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class measurementDependencyType:
    dependencyType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    measurementID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


class measurementInformationTypePatientPosition(Enum):
    HFP = "HFP"
    HFS = "HFS"
    HFDR = "HFDR"
    HFDL = "HFDL"
    FFP = "FFP"
    FFS = "FFS"
    FFDR = "FFDR"
    FFDL = "FFDL"


@dataclass
class multiBandType:
    factor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    totalSlices: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    spacing: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class referencedImageSequenceType:
    referencedSOPInstanceUID: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class studyInformationType:
    studyDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    studyTime: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    studyID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    accessionNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    referringPhysicianName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    studyDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    studyInstanceUID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class subjectInformationType:
    patientName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    patientWeight_kg: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    patientID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    patientBirthdate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    patientGender: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "pattern": r"[MFO]",
        }
    )


class trajectoryType(Enum):
    CARTESIAN = "cartesian"
    EPI = "epi"
    RADIAL = "radial"
    GOLDENANGLE = "goldenangle"
    SPIRAL = "spiral"
    OTHER = "other"


@dataclass
class userParameterBase64Type:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    value: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class userParameterDoubleType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class userParameterLongType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class userParameterStringType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


class waveformInformationTypeWaveformType(Enum):
    ECG = "ecg"
    PULSE = "pulse"
    RESPIRATORY = "respiratory"
    TRIGGER = "trigger"
    GRADIENTWAVEFORM = "gradientwaveform"
    OTHER = "other"


@dataclass
class acquisitionSystemInformationType:
    systemVendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    systemModel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    systemFieldStrength_T: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    relativeReceiverNoiseBandwidth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    receiverChannels: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    coilLabel: List[coilLabelType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    institutionName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    stationName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class diffusionType:
    user0: Optional[int] = field(
        default=None,
        metadata={
            "name": "user_0",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    user1: Optional[int] = field(
        default=None,
        metadata={
            "name": "user_1",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    bvalue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    direction: Optional[diffusionGradientDirectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class encodingLimitsType:
    kspace_encoding_step_0: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    kspace_encoding_step_1: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    kspace_encoding_step_2: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    average: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    slice: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    contrast: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    phase: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    repetition: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    set: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    segment: Optional[limitType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    user0: Optional[limitType] = field(
        default=None,
        metadata={
            "name": "user_0",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    user1: Optional[limitType] = field(
        default=None,
        metadata={
            "name": "user_1",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    user2: Optional[limitType] = field(
        default=None,
        metadata={
            "name": "user_2",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    user3: Optional[limitType] = field(
        default=None,
        metadata={
            "name": "user_3",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    user4: Optional[limitType] = field(
        default=None,
        metadata={
            "name": "user_4",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    user5: Optional[limitType] = field(
        default=None,
        metadata={
            "name": "user_5",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    user6: Optional[limitType] = field(
        default=None,
        metadata={
            "name": "user_6",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    user7: Optional[limitType] = field(
        default=None,
        metadata={
            "name": "user_7",
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class encodingSpaceType:
    matrixSize: Optional[matrixSizeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    fieldOfView_mm: Optional[fieldOfViewMmType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class measurementInformationType:
    measurementID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    seriesDate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    seriesTime: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    patientPosition: Optional[measurementInformationTypePatientPosition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    initialSeriesNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    protocolName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    seriesDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    measurementDependency: List[measurementDependencyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    seriesInstanceUIDRoot: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    frameOfReferenceUID: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    referencedImageSequence: Optional[referencedImageSequenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class parallelImagingType:
    accelerationFactor: Optional[accelerationFactorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    calibrationMode: Optional[calibrationModeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    interleavingDimension: Optional[interleavingDimensionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    multiBand: Optional[multiBandType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class trajectoryDescriptionType:
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    userParameterLong: List[userParameterLongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    userParameterDouble: List[userParameterDoubleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    userParameterString: List[userParameterStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class userParametersType:
    userParameterLong: List[userParameterLongType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    userParameterDouble: List[userParameterDoubleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    userParameterString: List[userParameterStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    userParameterBase64: List[userParameterBase64Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class diffusionDescriptionType:
    diffusion: List[diffusionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "min_occurs": 1,
        }
    )


@dataclass
class encodingType:
    encodedSpace: Optional[encodingSpaceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    reconSpace: Optional[encodingSpaceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    encodingLimits: Optional[encodingLimitsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    trajectory: Optional[trajectoryType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    trajectoryDescription: Optional[trajectoryDescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    parallelImaging: Optional[parallelImagingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    echoTrainLength: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class waveformInformationType:
    waveformName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    waveformType: Optional[waveformInformationTypeWaveformType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )
    userParameters: Optional[userParametersType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
            "required": True,
        }
    )


@dataclass
class sequenceParametersType:
    TR: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    TE: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    TI: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    flipAngle_deg: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    sequence_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    echo_spacing: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )
    diffusionDescription: Optional[diffusionDescriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ismrm.org/ISMRMRD",
        }
    )


@dataclass
class ismrmrdHeaderType:
    class Meta:
        name = "ismrmrdHeader"
        namespace = "http://www.ismrm.org/ISMRMRD"

    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subjectInformation: Optional[subjectInformationType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    studyInformation: Optional[studyInformationType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    measurementInformation: Optional[measurementInformationType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    acquisitionSystemInformation: Optional[acquisitionSystemInformationType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    experimentalConditions: Optional[experimentalConditionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    encoding: List[encodingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    sequenceParameters: Optional[sequenceParametersType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    userParameters: Optional[userParametersType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    waveformInformation: List[waveformInformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 32,
        }
    )
