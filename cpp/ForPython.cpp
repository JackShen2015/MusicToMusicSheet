//
// Created by jack on 17-4-24.
//

#include "MusicProcessingTools.h"

extern "C" {
MusicProcessingTools musicProcessingTools;
float getBasicHz(long *input, int n) {
    return musicProcessingTools.GetBasicHz(input, n);
}
long getEnerge(long *input, int n) {
    return musicProcessingTools.Energy(input, n);
}
}