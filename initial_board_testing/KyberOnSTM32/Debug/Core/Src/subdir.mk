################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/PQCgenKAT_kem.c \
../Core/Src/aes256ctr.c \
../Core/Src/cbd.c \
../Core/Src/cpucycles.c \
../Core/Src/fips202.c \
../Core/Src/indcpa.c \
../Core/Src/kem.c \
../Core/Src/kex.c \
../Core/Src/main.c \
../Core/Src/ntt.c \
../Core/Src/poly.c \
../Core/Src/polyvec.c \
../Core/Src/randombytes.c \
../Core/Src/reduce.c \
../Core/Src/rng.c \
../Core/Src/sha256.c \
../Core/Src/sha512.c \
../Core/Src/speed_print.c \
../Core/Src/stm32l4xx_hal_msp.c \
../Core/Src/stm32l4xx_it.c \
../Core/Src/symmetric-aes.c \
../Core/Src/symmetric-shake.c \
../Core/Src/syscalls.c \
../Core/Src/sysmem.c \
../Core/Src/system_stm32l4xx.c \
../Core/Src/test_kex.c \
../Core/Src/test_kyber.c \
../Core/Src/test_speed.c \
../Core/Src/test_vectors.c \
../Core/Src/verify.c 

OBJS += \
./Core/Src/PQCgenKAT_kem.o \
./Core/Src/aes256ctr.o \
./Core/Src/cbd.o \
./Core/Src/cpucycles.o \
./Core/Src/fips202.o \
./Core/Src/indcpa.o \
./Core/Src/kem.o \
./Core/Src/kex.o \
./Core/Src/main.o \
./Core/Src/ntt.o \
./Core/Src/poly.o \
./Core/Src/polyvec.o \
./Core/Src/randombytes.o \
./Core/Src/reduce.o \
./Core/Src/rng.o \
./Core/Src/sha256.o \
./Core/Src/sha512.o \
./Core/Src/speed_print.o \
./Core/Src/stm32l4xx_hal_msp.o \
./Core/Src/stm32l4xx_it.o \
./Core/Src/symmetric-aes.o \
./Core/Src/symmetric-shake.o \
./Core/Src/syscalls.o \
./Core/Src/sysmem.o \
./Core/Src/system_stm32l4xx.o \
./Core/Src/test_kex.o \
./Core/Src/test_kyber.o \
./Core/Src/test_speed.o \
./Core/Src/test_vectors.o \
./Core/Src/verify.o 

C_DEPS += \
./Core/Src/PQCgenKAT_kem.d \
./Core/Src/aes256ctr.d \
./Core/Src/cbd.d \
./Core/Src/cpucycles.d \
./Core/Src/fips202.d \
./Core/Src/indcpa.d \
./Core/Src/kem.d \
./Core/Src/kex.d \
./Core/Src/main.d \
./Core/Src/ntt.d \
./Core/Src/poly.d \
./Core/Src/polyvec.d \
./Core/Src/randombytes.d \
./Core/Src/reduce.d \
./Core/Src/rng.d \
./Core/Src/sha256.d \
./Core/Src/sha512.d \
./Core/Src/speed_print.d \
./Core/Src/stm32l4xx_hal_msp.d \
./Core/Src/stm32l4xx_it.d \
./Core/Src/symmetric-aes.d \
./Core/Src/symmetric-shake.d \
./Core/Src/syscalls.d \
./Core/Src/sysmem.d \
./Core/Src/system_stm32l4xx.d \
./Core/Src/test_kex.d \
./Core/Src/test_kyber.d \
./Core/Src/test_speed.d \
./Core/Src/test_vectors.d \
./Core/Src/verify.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/%.o Core/Src/%.su Core/Src/%.cyclo: ../Core/Src/%.c Core/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32L4R5xx -c -I../Core/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src

clean-Core-2f-Src:
	-$(RM) ./Core/Src/PQCgenKAT_kem.cyclo ./Core/Src/PQCgenKAT_kem.d ./Core/Src/PQCgenKAT_kem.o ./Core/Src/PQCgenKAT_kem.su ./Core/Src/aes256ctr.cyclo ./Core/Src/aes256ctr.d ./Core/Src/aes256ctr.o ./Core/Src/aes256ctr.su ./Core/Src/cbd.cyclo ./Core/Src/cbd.d ./Core/Src/cbd.o ./Core/Src/cbd.su ./Core/Src/cpucycles.cyclo ./Core/Src/cpucycles.d ./Core/Src/cpucycles.o ./Core/Src/cpucycles.su ./Core/Src/fips202.cyclo ./Core/Src/fips202.d ./Core/Src/fips202.o ./Core/Src/fips202.su ./Core/Src/indcpa.cyclo ./Core/Src/indcpa.d ./Core/Src/indcpa.o ./Core/Src/indcpa.su ./Core/Src/kem.cyclo ./Core/Src/kem.d ./Core/Src/kem.o ./Core/Src/kem.su ./Core/Src/kex.cyclo ./Core/Src/kex.d ./Core/Src/kex.o ./Core/Src/kex.su ./Core/Src/main.cyclo ./Core/Src/main.d ./Core/Src/main.o ./Core/Src/main.su ./Core/Src/ntt.cyclo ./Core/Src/ntt.d ./Core/Src/ntt.o ./Core/Src/ntt.su ./Core/Src/poly.cyclo ./Core/Src/poly.d ./Core/Src/poly.o ./Core/Src/poly.su ./Core/Src/polyvec.cyclo ./Core/Src/polyvec.d ./Core/Src/polyvec.o ./Core/Src/polyvec.su ./Core/Src/randombytes.cyclo ./Core/Src/randombytes.d ./Core/Src/randombytes.o ./Core/Src/randombytes.su ./Core/Src/reduce.cyclo ./Core/Src/reduce.d ./Core/Src/reduce.o ./Core/Src/reduce.su ./Core/Src/rng.cyclo ./Core/Src/rng.d ./Core/Src/rng.o ./Core/Src/rng.su ./Core/Src/sha256.cyclo ./Core/Src/sha256.d ./Core/Src/sha256.o ./Core/Src/sha256.su ./Core/Src/sha512.cyclo ./Core/Src/sha512.d ./Core/Src/sha512.o ./Core/Src/sha512.su ./Core/Src/speed_print.cyclo ./Core/Src/speed_print.d ./Core/Src/speed_print.o ./Core/Src/speed_print.su ./Core/Src/stm32l4xx_hal_msp.cyclo ./Core/Src/stm32l4xx_hal_msp.d ./Core/Src/stm32l4xx_hal_msp.o ./Core/Src/stm32l4xx_hal_msp.su ./Core/Src/stm32l4xx_it.cyclo ./Core/Src/stm32l4xx_it.d ./Core/Src/stm32l4xx_it.o ./Core/Src/stm32l4xx_it.su ./Core/Src/symmetric-aes.cyclo ./Core/Src/symmetric-aes.d ./Core/Src/symmetric-aes.o ./Core/Src/symmetric-aes.su ./Core/Src/symmetric-shake.cyclo ./Core/Src/symmetric-shake.d ./Core/Src/symmetric-shake.o ./Core/Src/symmetric-shake.su ./Core/Src/syscalls.cyclo ./Core/Src/syscalls.d ./Core/Src/syscalls.o ./Core/Src/syscalls.su ./Core/Src/sysmem.cyclo ./Core/Src/sysmem.d ./Core/Src/sysmem.o ./Core/Src/sysmem.su ./Core/Src/system_stm32l4xx.cyclo ./Core/Src/system_stm32l4xx.d ./Core/Src/system_stm32l4xx.o ./Core/Src/system_stm32l4xx.su ./Core/Src/test_kex.cyclo ./Core/Src/test_kex.d ./Core/Src/test_kex.o ./Core/Src/test_kex.su ./Core/Src/test_kyber.cyclo ./Core/Src/test_kyber.d ./Core/Src/test_kyber.o ./Core/Src/test_kyber.su ./Core/Src/test_speed.cyclo ./Core/Src/test_speed.d ./Core/Src/test_speed.o ./Core/Src/test_speed.su ./Core/Src/test_vectors.cyclo ./Core/Src/test_vectors.d ./Core/Src/test_vectors.o ./Core/Src/test_vectors.su ./Core/Src/verify.cyclo ./Core/Src/verify.d ./Core/Src/verify.o ./Core/Src/verify.su

.PHONY: clean-Core-2f-Src

