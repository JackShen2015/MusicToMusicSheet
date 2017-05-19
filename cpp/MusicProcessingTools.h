//
// Created by jack on 17-4-24.
//

#ifndef THREAD_MUSICPROCESSINGTOOLS_H
#define THREAD_MUSICPROCESSINGTOOLS_H

#define PI 3.1415926
#define Fs 44100


class MusicProcessingTools {
public:
    float GetBasicHz(long *a, int n);

    long Energy(long *a, int n);

    float *DCT(long *a, int n);
};


#endif //THREAD_MUSICPROCESSINGTOOLS_H
