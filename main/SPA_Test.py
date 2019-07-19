#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/07/10 10:00
# @Author  : Feng
# @Site    : 
# @File    : SPA.py
# @Software: PyCharm Community Edition
# @Contact : xiaofeng5197@163.com

# 导入模块
import SPA
import datetime

# 类定义

# 函数定义

# 主程序

mSPA = SPA.SPAData()
mSPA.year = 2003
mSPA.month = 10
mSPA.day = 17
mSPA.hour = 12
mSPA.minute = 30
mSPA.second = 30
mSPA.timezone      = -7.0;
mSPA.delta_ut1     = 0;
mSPA.delta_t       = 67;
mSPA.longitude     = -105.1786;
mSPA.latitude      = 39.742476;
mSPA.elevation     = 1830.14;
mSPA.pressure      = 820;
mSPA.temperature   = 11;
mSPA.slope         = 30;
mSPA.azm_rotation  = -10;
mSPA.atmos_refract = 0.5667;

ret = SPA.spa_calculate(mSPA)

if ret == 0:
    print("JulianDay:   %.6f" % mSPA.jd)
    print("L:           %.6e deg" % mSPA.l)
    print("B:           %.6e deg" % mSPA.b)
    print("R:           %.6f AU" % mSPA.r)
    print("H:           %.6f deg" % mSPA.h)
    print("DeltaPsi:    %.6e deg" % mSPA.del_psi)
    print("DeltaEpsilon:%.6e deg" % mSPA.del_epsilon)
    print("Epsilon:     %.6f deg" % mSPA.epsilon)
    print("Zenith:      %.6f deg" % mSPA.zenith)
    print("Azimuth:     %.6f deg" % mSPA.azimuth)
    print("Incidence:   %.6f deg" % mSPA.incidence)
    min = 60.0 * (mSPA.sunrise - int(mSPA.sunrise))
    sec = 60.0 * (min - int(min))
    print("Sunrise:     %02d:%02d:%02d LocalTime" % (int(mSPA.sunrise), int(min), int(sec)))
    min = 60.0 * (mSPA.sunset - int(mSPA.sunset))
    sec = 60.0 * (min - int(min))
    print("Sunrise:     %02d:%02d:%02d LocalTime" % (int(mSPA.sunset), int(min), int(sec)))
else:
    print("SPA Error Code:%d" % ret)

"""
/////////////////////////////////////////////
// The output of this program should be:
//
//Julian Day:    2452930.312847
//L:             2.401826e+01 degrees
//B:             -1.011219e-04 degrees
//R:             0.996542 AU
//H:             11.105902 degrees
//Delta Psi:     -3.998404e-03 degrees
//Delta Epsilon: 1.666568e-03 degrees
//Epsilon:       23.440465 degrees
//Zenith:        50.111622 degrees
//Azimuth:       194.340241 degrees
//Incidence:     25.187000 degrees
//Sunrise:       06:12:43 Local Time
//Sunset:        17:20:19 Local Time
//
/////////////////////////////////////////////
"""