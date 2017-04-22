//
// Created by jack on 17-4-8.
//
#include <iostream>
#include <math.h>

//#define N 10
#define PI 3.1415926
#define Fs 44100


template<class T>
int getArrayLen(T &array) {
    return (sizeof(array) / sizeof(array[0]));
}

//获得最大值
int getMax(float *input, int N) {
    float MAX = input[0];
    int num = 0;
    for (int i = 0; i < N; i++) {
        if (MAX < input[i]) {
            MAX = input[i];
            num = i;
        }
    }
    return num;
}

//获得最小值
int getMin(float *input, int N) {
    float MIN = input[0];
    int num = 0;
    for (int i = 0; i < N; ++i) {
        if (MIN > input[i]) {
            MIN = input[i];
            num = i;
        }
    }
    return num;
}


//DCT运算
float *DCT(float *input, int N) {
    float ALPHA = (float) sqrt(1.0 / N);
    //std::cout << "ALPHA:" << ALPHA << std::endl;
    float BETA = (float) sqrt(2.0 / N);
    //std::cout << "BETA:" << BETA << std::endl;

    //std::cout << "N:" << N << std::endl;

    float *output = new float[N];

    for (int i = 0; i < N; i++) {
        float temp = 0.0f;
        switch (i) {
            case 0: {
                for (int j = 0; j < N; j++) {
                    temp += input[j];
                    //std::cout << temp << std::endl;
                }
                temp *= ALPHA;
                //std::cout << "temp=0:" << temp << std::endl;
                //output[i] = temp;
                break;
            }
            default: {
                for (int j = 0; j < N; j++) {
                    temp += input[j] * cos((j + 0.5) * i * PI / N);
                }
                temp *= BETA;
                break;
            }

        }

        output[i] = temp;
    }

    return output;
}

//获得基音
float getBasicHz(float *input, int N) {
    float *output = DCT(input, N);

    int MAX = getMax(output, N);
    int MIN = getMin(output, N);

    float Ub = (MAX + MIN) / 2.0;

//    std::cout << "Ub:" << Ub << std::endl;
//
//    std::cout << "MAX:" << MAX << std::endl;
//    std::cout << "MIN:" << MIN << std::endl;
//
//    std::cout<<"Result:"<<(Ub*Fs)/(2*N)<<std::endl;

    return (Ub * Fs) / (2 * N);
}

extern "C" {
float cgetBasicHz(float *input, int N) {
    return getBasicHz(input, N);
}
}


//int main() {
//    int N = 10;
//    float *p = new float[N];
//    float pRaw[N] = {1210, -1310, 1140, 120, -10, 11340, 10, 2100, 11122, 12310};
//
//    //std::cout << getArrayLen(pRaw) << std::endl;
//
//    for (int i = 0; i < N; i++) {
//        p[i] = pRaw[i];
//    }
//
//    float *output = DCT(p, N);
//
//    for (int i = 0; i < N; i++) {
//        std::cout << output[i] << "\t";
//    }
//    std::cout << std::endl;
//
//    std::cout << "MAX:" << getMax(output, N) << std::endl;
//    std::cout << "MIN:" << getMin(output, N) << std::endl;
//
//    std::cout << "BasicHz:" << getBasicHz(p, N) << std::endl;
//
//    std::cout << sizeof(float) << std::endl;
//    return 0;
//}