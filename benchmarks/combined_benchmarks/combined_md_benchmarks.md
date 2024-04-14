# Speed Evaluation
| scheme | implementation | key generation [cycles] | encapsulation [cycles] | decapsulation [cycles] |
| ------ | -------------- | ----------------------- | ---------------------- | ---------------------- |
| kyber512 reference (3 executions) | clean | AVG: 652,873 <br /> MIN: 652,784 <br /> MAX: 652,924 | AVG: 863,682 <br /> MIN: 863,593 <br /> MAX: 863,733 | AVG: 947,459 <br /> MIN: 947,370 <br /> MAX: 947,510 |
| kyber512 reference (3 executions) | m4fspeed | AVG: 466,988 <br /> MIN: 466,752 <br /> MAX: 467,164 | AVG: 573,402 <br /> MIN: 573,165 <br /> MAX: 573,577 | AVG: 514,095 <br /> MIN: 513,858 <br /> MAX: 514,271 |
| kyber512 reference (3 executions) | m4fstack | AVG: 466,758 <br /> MIN: 466,621 <br /> MAX: 466,933 | AVG: 575,359 <br /> MIN: 575,223 <br /> MAX: 575,534 | AVG: 516,118 <br /> MIN: 515,982 <br /> MAX: 516,293 |
| kyber512 speed (3 executions) | clean | AVG: 613,817 <br /> MIN: 613,697 <br /> MAX: 613,885 | AVG: 814,066 <br /> MIN: 813,946 <br /> MAX: 814,134 | AVG: 918,143 <br /> MIN: 918,023 <br /> MAX: 918,211 |
| kyber512 speed (3 executions) | m4fspeed | AVG: 431,293 <br /> MIN: 431,129 <br /> MAX: 431,411 | AVG: 527,142 <br /> MIN: 526,980 <br /> MAX: 527,260 | AVG: 488,127 <br /> MIN: 487,964 <br /> MAX: 488,245 |
| kyber512 speed (3 executions) | m4fstack | AVG: 430,893 <br /> MIN: 430,586 <br /> MAX: 431,111 | AVG: 528,931 <br /> MIN: 528,625 <br /> MAX: 529,148 | AVG: 489,975 <br /> MIN: 489,669 <br /> MAX: 490,192 |
| kyber512 small (3 executions) | clean | AVG: 639,016 <br /> MIN: 638,735 <br /> MAX: 639,184 | AVG: 845,494 <br /> MIN: 845,213 <br /> MAX: 845,662 | AVG: 944,075 <br /> MIN: 943,794 <br /> MAX: 944,243 |
| kyber512 small (3 executions) | m4fspeed | AVG: 456,436 <br /> MIN: 456,262 <br /> MAX: 456,525 | AVG: 558,515 <br /> MIN: 558,341 <br /> MAX: 558,605 | AVG: 514,007 <br /> MIN: 513,834 <br /> MAX: 514,097 |
| kyber512 small (3 executions) | m4fstack | AVG: 455,902 <br /> MIN: 455,788 <br /> MAX: 455,966 | AVG: 560,174 <br /> MIN: 560,060 <br /> MAX: 560,239 | AVG: 515,720 <br /> MIN: 515,606 <br /> MAX: 515,785 |
| kyber512 lowsize (3 executions) | clean | AVG: 639,021 <br /> MIN: 638,965 <br /> MAX: 639,076 | AVG: 845,498 <br /> MIN: 845,443 <br /> MAX: 845,553 | AVG: 944,079 <br /> MIN: 944,024 <br /> MAX: 944,134 |
| kyber512 lowsize (3 executions) | m4fspeed | AVG: 456,499 <br /> MIN: 456,276 <br /> MAX: 456,934 | AVG: 558,578 <br /> MIN: 558,354 <br /> MAX: 559,013 | AVG: 514,071 <br /> MIN: 513,847 <br /> MAX: 514,505 |
| kyber512 lowsize (3 executions) | m4fstack | AVG: 456,008 <br /> MIN: 455,891 <br /> MAX: 456,099 | AVG: 560,280 <br /> MIN: 560,161 <br /> MAX: 560,370 | AVG: 515,826 <br /> MIN: 515,707 <br /> MAX: 515,916 |
| kyber512 bi32speed (3 executions) | clean | AVG: 556,047 <br /> MIN: 555,788 <br /> MAX: 556,207 | AVG: 740,344 <br /> MIN: 740,085 <br /> MAX: 740,504 | AVG: 858,333 <br /> MIN: 858,074 <br /> MAX: 858,493 |
| kyber512 bi32speed (3 executions) | m4fspeed | AVG: 372,989 <br /> MIN: 372,895 <br /> MAX: 373,087 | AVG: 452,886 <br /> MIN: 452,792 <br /> MAX: 452,983 | AVG: 427,780 <br /> MIN: 427,686 <br /> MAX: 427,877 |
| kyber512 bi32speed (3 executions) | m4fstack | AVG: 372,467 <br /> MIN: 372,197 <br /> MAX: 372,612 | AVG: 454,548 <br /> MIN: 454,278 <br /> MAX: 454,693 | AVG: 429,502 <br /> MIN: 429,232 <br /> MAX: 429,647 |
| kyber512 bi32small (3 executions) | clean | AVG: 605,807 <br /> MIN: 605,686 <br /> MAX: 605,944 | AVG: 802,490 <br /> MIN: 802,369 <br /> MAX: 802,627 | AVG: 909,661 <br /> MIN: 909,540 <br /> MAX: 909,798 |
| kyber512 bi32small (3 executions) | m4fspeed | AVG: 422,704 <br /> MIN: 422,560 <br /> MAX: 422,805 | AVG: 514,981 <br /> MIN: 514,836 <br /> MAX: 515,083 | AVG: 479,057 <br /> MIN: 478,911 <br /> MAX: 479,159 |
| kyber512 bi32small (3 executions) | m4fstack | AVG: 422,180 <br /> MIN: 421,990 <br /> MAX: 422,376 | AVG: 516,649 <br /> MIN: 516,458 <br /> MAX: 516,845 | AVG: 480,786 <br /> MIN: 480,595 <br /> MAX: 480,982 |

# Memory Evaluation
| Scheme | Implementation | Key Generation [bytes] | Encapsulation [bytes] | Decapsulation [bytes] |
| ------ | -------------- | ---------------------- | --------------------- | --------------------- |
| kyber512 reference | clean | 6,116 | 8,764 | 9,532 |
| kyber512 reference | m4fspeed | 4,312 | 5,408 | 5,416 |
| kyber512 reference | m4fstack | 2,252 | 2,332 | 2,348 |
| kyber512 speed | clean | 5,976 | 8,632 | 9,400 |
| kyber512 speed | m4fspeed | 4,152 | 5,256 | 5,264 |
| kyber512 speed | m4fstack | 2,120 | 2,208 | 2,224 |
| kyber512 small | clean | 5,976 | 8,632 | 9,400 |
| kyber512 small | m4fspeed | 4,152 | 5,256 | 5,264 |
| kyber512 small | m4fstack | 2,080 | 2,168 | 2,184 |
| kyber512 lowsize | clean | 5,976 | 8,632 | 9,400 |
| kyber512 lowsize | m4fspeed | 4,152 | 5,256 | 5,264 |
| kyber512 lowsize | m4fstack | 2,080 | 2,168 | 2,184 |
| kyber512 bi32speed | clean | 5,988 | 8,644 | 9,412 |
| kyber512 bi32speed | m4fspeed | 4,164 | 5,268 | 5,276 |
| kyber512 bi32speed | m4fstack | 2,092 | 2,180 | 2,196 |
| kyber512 bi32small | clean | 5,984 | 8,640 | 9,408 |
| kyber512 bi32small | m4fspeed | 4,172 | 5,276 | 5,284 |
| kyber512 bi32small | m4fstack | 2,100 | 2,188 | 2,204 |

# Hashing Evaluation
| Scheme | Implementation | Key Generation [%] | Encapsulation [%] | Decapsulation [%] |
| ------ | -------------- | ------------------ | ----------------- | ----------------- |
| kyber512 reference | clean | 56.6% | 54.0% | 39.2% |
| kyber512 reference | m4fspeed | 79.0% | 81.2% | 72.1% |
| kyber512 reference | m4fstack | 79.0% | 81.0% | 71.8% |
| kyber512 speed | clean | 53.9% | 51.3% | 37.3% |
| kyber512 speed | m4fspeed | 77.2% | 79.6% | 70.6% |
| kyber512 speed | m4fstack | 77.3% | 79.3% | 70.4% |
| kyber512 small | clean | 55.7% | 53.1% | 39.1% |
| kyber512 small | m4fspeed | 78.4% | 80.7% | 72.1% |
| kyber512 small | m4fstack | 78.5% | 80.4% | 71.8% |
| kyber512 lowsize | clean | 55.7% | 53.1% | 39.1% |
| kyber512 lowsize | m4fspeed | 78.5% | 80.8% | 72.1% |
| kyber512 lowsize | m4fstack | 78.5% | 80.5% | 71.9% |
| kyber512 bi32speed | clean | 49.1% | 46.5% | 33.0% |
| kyber512 bi32speed | m4fspeed | 73.7% | 76.3% | 66.5% |
| kyber512 bi32speed | m4fstack | 73.8% | 76.0% | 66.3% |
| kyber512 bi32small | clean | 53.3% | 50.6% | 36.8% |
| kyber512 bi32small | m4fspeed | 76.8% | 79.1% | 70.1% |
| kyber512 bi32small | m4fstack | 76.9% | 78.9% | 69.9% |

# Size Evaluation
| Scheme | Implementation | .text [bytes] | .data [bytes] | .bss [bytes] | Total [bytes] |
| ------ | -------------- | ------------- | ------------- | ------------ | ------------- |
| kyber512 reference | clean | 4,772 | 0 | 0 | 4,772 |
| kyber512 reference | m4fspeed | 15,320 | 0 | 0 | 15,320 |
| kyber512 reference | m4fstack | 12,816 | 0 | 0 | 12,816 |
| kyber512 speed | clean | 4,812 | 0 | 0 | 4,812 |
| kyber512 speed | m4fspeed | 15,444 | 0 | 0 | 15,444 |
| kyber512 speed | m4fstack | 12,880 | 0 | 0 | 12,880 |
| kyber512 small | clean | 4,812 | 0 | 0 | 4,812 |
| kyber512 small | m4fspeed | 15,444 | 0 | 0 | 15,444 |
| kyber512 small | m4fstack | 12,880 | 0 | 0 | 12,880 |
| kyber512 lowsize | clean | 4,812 | 0 | 0 | 4,812 |
| kyber512 lowsize | m4fspeed | 15,444 | 0 | 0 | 15,444 |
| kyber512 lowsize | m4fstack | 12,880 | 0 | 0 | 12,880 |
| kyber512 bi32speed | clean | 4,812 | 0 | 0 | 4,812 |
| kyber512 bi32speed | m4fspeed | 15,444 | 0 | 0 | 15,444 |
| kyber512 bi32speed | m4fstack | 12,880 | 0 | 0 | 12,880 |
| kyber512 bi32small | clean | 4,812 | 0 | 0 | 4,812 |
| kyber512 bi32small | m4fspeed | 15,444 | 0 | 0 | 15,444 |
| kyber512 bi32small | m4fstack | 12,880 | 0 | 0 | 12,880 |

