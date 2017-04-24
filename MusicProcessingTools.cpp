//
// Created by jack on 17-4-24.
//

#include "MusicProcessingTools.h"
#include <iostream>
#include <math.h>

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


float MusicProcessingTools::GetBasicHz(long *input, int N) {
    float *output = DCT(input, N);

    int MAX = getMax(output, N);
    int MIN = getMin(output, N);

    float Ub = (float) ((MAX + MIN) / 2.0);

    return (Ub * Fs) / (2 * N);
}

long MusicProcessingTools::Energy(long *input, int N) {
    long result=0;
    for(int i=0;i<N;i++){
        result=input[i];
    }
    return result;
}

float *MusicProcessingTools::DCT(long *input, int N) {
    float ALPHA = (float) sqrt(1.0 / N);
    float BETA = (float) sqrt(2.0 / N);

    float *output = new float[N];

    for (int i = 0; i < N; i++) {
        float temp = 0.0f;
        switch (i) {
            case 0: {
                for (int j = 0; j < N; j++) {
                    temp += input[j];
                }
                temp *= ALPHA;
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