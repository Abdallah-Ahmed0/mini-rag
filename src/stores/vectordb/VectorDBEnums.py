from enum import Enum

class VectorDBENum(Enum):
    QDRANT = "QDRANT"

class DistanceMethodEnum(Enum):
    COSINE = "cosine"
    DOT = "dot"