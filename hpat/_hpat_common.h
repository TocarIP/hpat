#ifndef HPAT_COMMON_H_
#define HPAT_COMMON_H_


// class CTypeEnum(Enum):
//     Int8 = 0
//     UInt8 = 1
//     Int32 = 2
//     UInt32 = 3
//     Int64 = 4
//     UInt64 = 5
//     Float32 = 6
//     Float64 = 7


struct HPAT_CTypes {
    enum HPAT_CTypeEnum {
        INT8 = 0,
        UINT8 = 1,
        INT32 = 2,
        UINT32 = 3,
        INT64 = 4,
        UINT64 = 7,
        FLOAT32 = 5,
        FLOAT64 = 6,
    };
};

#endif /* HPAT_COMMON_H_ */
