## VAR Granger causality results

R Studio console output for Granger causality tests using vector
autoregression model on the 10m BST Cassandra data.

Findings from experimenting with max lag variable:

1. setting max lag above 10 has no affect on results:
2. max lag of 8 seems to be a "sweet spot" in that rpm vs apdex is shown to have single-directional causality, but rpm vs duration indicates bi-directional causality. 

**lag.max = 10**
```
> rpm_diff=diff(rpm)
> apdex_diff=diff(apdex_score)
> rpm_apdex=cbind(rpm_diff, apdex_diff)
> rpm_apdex_VAR=VAR(rpm_apdex, p=2, type="const")
> rpm_apdex_VAR=VAR(rpm_apdex, type="const", lag.max = 10, ic = "AIC")
> 
> causality(rpm_apdex_VAR, cause = "rpm_diff")$Granger

    Granger causality H0: rpm_diff do not Granger-cause apdex_diff

data:  VAR object rpm_apdex_VAR
F-Test = 22.585, df1 = 10, df2 = 8000, p-value < 2.2e-16

> causality(rpm_apdex_VAR, cause = "apdex_diff")$Granger

    Granger causality H0: apdex_diff do not Granger-cause rpm_diff

data:  VAR object rpm_apdex_VAR
F-Test = 2.0283, df1 = 10, df2 = 8000, p-value = 0.02682

> duration_diff=diff(duration)
> rpm_duration=cbind(rpm_diff, duration_diff)
> rpm_duration_VAR=VAR(rpm_duration, p=2, type="const")
> rpm_duration_VAR=VAR(rpm_duration, type="const", lag.max = 10, ic = "AIC")
> 
> causality(rpm_duration_VAR, cause = "rpm_diff")$Granger

    Granger causality H0: rpm_diff do not Granger-cause duration_diff

data:  VAR object rpm_duration_VAR
F-Test = 10.288, df1 = 9, df2 = 8006, p-value = 6.661e-16

> causality(rpm_duration_VAR, cause = "duration_diff")$Granger

    Granger causality H0: duration_diff do not Granger-cause rpm_diff

data:  VAR object rpm_duration_VAR
F-Test = 2.5045, df1 = 9, df2 = 8006, p-value = 0.007374
```
**lag.max = 11**
```
> rpm_apdex_VAR=VAR(rpm_apdex, type="const", lag.max = 11, ic = "AIC")
> causality(rpm_apdex_VAR, cause = "rpm_diff")$Granger

    Granger causality H0: rpm_diff do not Granger-cause apdex_diff

data:  VAR object rpm_apdex_VAR
F-Test = 24.023, df1 = 11, df2 = 7994, p-value < 2.2e-16

> causality(rpm_apdex_VAR, cause = "apdex_diff")$Granger

    Granger causality H0: apdex_diff do not Granger-cause rpm_diff

data:  VAR object rpm_apdex_VAR
F-Test = 1.875, df1 = 11, df2 = 7994, p-value = 0.03764

> 
> rpm_duration_VAR=VAR(rpm_duration, type="const", lag.max = 11, ic = "AIC")
> causality(rpm_duration_VAR, cause = "rpm_diff")$Granger

    Granger causality H0: rpm_diff do not Granger-cause duration_diff

data:  VAR object rpm_duration_VAR
F-Test = 10.288, df1 = 9, df2 = 8006, p-value = 6.661e-16

> causality(rpm_duration_VAR, cause = "duration_diff")$Granger

    Granger causality H0: duration_diff do not Granger-cause rpm_diff

data:  VAR object rpm_duration_VAR
F-Test = 2.5045, df1 = 9, df2 = 8006, p-value = 0.007374
```
**lag.max = 20**
```
> rpm_apdex_VAR=VAR(rpm_apdex, type="const", lag.max = 20, ic = "AIC")
> causality(rpm_apdex_VAR, cause = "rpm_diff")$Granger

    Granger causality H0: rpm_diff do not Granger-cause apdex_diff

data:  VAR object rpm_apdex_VAR
F-Test = 23.89, df1 = 15, df2 = 7970, p-value < 2.2e-16

> causality(rpm_apdex_VAR, cause = "apdex_diff")$Granger

    Granger causality H0: apdex_diff do not Granger-cause rpm_diff

data:  VAR object rpm_apdex_VAR
F-Test = 2.0932, df1 = 15, df2 = 7970, p-value = 0.007855

> 
> rpm_duration_VAR=VAR(rpm_duration, type="const", lag.max = 20, ic = "AIC")
> causality(rpm_duration_VAR, cause = "rpm_diff")$Granger

    Granger causality H0: rpm_diff do not Granger-cause duration_diff

data:  VAR object rpm_duration_VAR
F-Test = 10.288, df1 = 9, df2 = 8006, p-value = 6.661e-16

> causality(rpm_duration_VAR, cause = "duration_diff")$Granger

    Granger causality H0: duration_diff do not Granger-cause rpm_diff

data:  VAR object rpm_duration_VAR
F-Test = 2.5045, df1 = 9, df2 = 8006, p-value = 0.007374

```
**lag.max = 8**
```
> rpm_apdex_VAR=VAR(rpm_apdex, type="const", lag.max = 8, ic = "AIC")
> causality(rpm_apdex_VAR, cause = "rpm_diff")$Granger

    Granger causality H0: rpm_diff do not Granger-cause apdex_diff

data:  VAR object rpm_apdex_VAR
F-Test = 22.952, df1 = 8, df2 = 8012, p-value < 2.2e-16

> causality(rpm_apdex_VAR, cause = "apdex_diff")$Granger

    Granger causality H0: apdex_diff do not Granger-cause rpm_diff

data:  VAR object rpm_apdex_VAR
F-Test = 1.6718, df1 = 8, df2 = 8012, p-value = 0.0998

> 
> rpm_duration_VAR=VAR(rpm_duration, type="const", lag.max = 8, ic = "AIC")
> causality(rpm_duration_VAR, cause = "rpm_diff")$Granger

    Granger causality H0: rpm_diff do not Granger-cause duration_diff

data:  VAR object rpm_duration_VAR
F-Test = 11.046, df1 = 8, df2 = 8012, p-value = 1.221e-15

> causality(rpm_duration_VAR, cause = "duration_diff")$Granger

    Granger causality H0: duration_diff do not Granger-cause rpm_diff

data:  VAR object rpm_duration_VAR
F-Test = 2.6764, df1 = 8, df2 = 8012, p-value = 0.00618
```


