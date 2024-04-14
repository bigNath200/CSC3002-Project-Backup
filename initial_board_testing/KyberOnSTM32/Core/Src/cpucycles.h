#ifndef CPUCYCLES_H
#define CPUCYCLES_H

#include <stdint.h>

#ifdef USE_DWT_CYCCNT

static inline uint32_t cpucycles(void) {
  return DWT_CYCCNT;
}

#else

static inline uint32_t cpucycles(void) {
  uint32_t result;

  __asm__ volatile ("isb; mrs %0, cntvct" : "=r" (result));

  return result;
}

#endif

uint32_t cpucycles_overhead(void);

#endif
